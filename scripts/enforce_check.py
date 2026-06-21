#!/usr/bin/env python3
"""Compliance check with pass@N + auto-heal."""
import sys, re, subprocess
from pathlib import Path
from typing import List, Tuple

V = Tuple[str, str, str]
SD = Path(__file__).resolve().parent
DD = SD.parent
CX = DD.parent
SK = CX / "skills"; ME = CX / "memory"; TA = CX / "tasks"

def check_core():
    r = []
    for n in ["_DEVELOPMENT_PROCEDURE.md","_ENFORCEMENT.md","_AGENTS_INTEGRATION.md","_TASK_REGISTRY.md","_INTEGRATION_MANIFEST.md"]:
        if not (DD / n).exists(): r.append(("C-01","L3",n+" 不存在"))
    return r

def check_tasks():
    r = []
    if not TA.is_dir(): r.append(("C-01","L3","tasks/ 不存在")); return r
    for tp in sorted(TA.iterdir()):
        if not tp.is_dir() or tp.name.startswith("_"): continue
        tn = tp.name; spec = tp / "_TASK_SPEC.md"
        if not spec.exists(): r.append(("C-02","L3",tn+": 缺 _TASK_SPEC.md")); continue
        for item in sorted(tp.iterdir()):
            if not item.is_dir() or not item.name.startswith("v"): continue
            vr = item.name
            if not re.match(r"^v\d+\.\d+-[a-z][a-z0-9-]*-20\d{6}$", vr):
                r.append(("C-04","L2",tn+": '"+vr+"' 版本名不合规"))
            if not (item / "_VERSION_SPEC.md").exists():
                r.append(("C-03","L2",tn+"/"+vr+": 缺 _VERSION_SPEC.md"))
            for sb in ("src","config","lib","requirements"):
                if not (item / sb).is_dir(): r.append(("C-06","L1",tn+"/"+vr+": 缺 "+sb+"/"))
        if spec.exists():
            try:
                ct = spec.read_text(encoding="utf-8")
                for s in re.findall(r"skills/([\w-]+)/", ct):
                    if not (SK / s).is_dir(): r.append(("C-07","L2",tn+": skill '"+s+"' 不存在"))
            except: pass
        md = ME / tn
        if md.is_dir() and not [f for f in md.iterdir() if f.name.startswith("memory-") and f.suffix==".md"]:
            r.append(("C-08","L1","memory/"+tn+"/ 无 memory-*.md"))
    return r

def check_sk_mem():
    r = []
    for nm,d in [("skills",SK),("memory",ME)]:
        if not d.is_dir(): r.append(("C-01b","L2",nm+"/ 目录不存在"))
        elif nm=="skills":
            for s in sorted(d.iterdir()):
                if s.is_dir() and not (s/"SKILL.md").exists(): r.append(("C-07","L2","Skill '"+s.name+"': 缺 SKILL.md"))
    return r

def all_chk():
    r=[]; r.extend(check_core()); r.extend(check_tasks()); r.extend(check_sk_mem()); return r

def blocking(v):
    return any(l in ("L2","L3","L4") for _,l,_ in v)

def report(v,ind=""):
    if not v: print(ind+"PASSED"); return
    c=dict(L1=0,L2=0,L3=0,L4=0)
    for _,l,_ in v: c[l]=c.get(l,0)+1
    print(ind+"违规: "+str(len(v)))
    for cid,lv,desc in sorted(v): print("  "+ind+"["+lv+"] "+cid+": "+desc)
    print(ind+"L1="+str(c["L1"])+" L2="+str(c["L2"])+" L3="+str(c["L3"])+" L4="+str(c["L4"]))
    b=c["L2"]+c["L3"]+c["L4"]
    print(ind+("结果: FAILED ("+str(b)+" 项阻止性)" if blocking(v) else "结果: PASSED"))

def stats():
    if TA.is_dir():
        tc=len([d for d in TA.iterdir() if d.is_dir() and not d.name.startswith("_")])
        sc=len([d for d in SK.iterdir() if d.is_dir()]) if SK.is_dir() else 0
        mc=len([d for d in ME.iterdir() if d.is_dir()]) if ME.is_dir() else 0
        print(); print("tasks/:  "+str(tc)+" 个任务"); print("skills/: "+str(sc)+" 个技能"); print("memory/: "+str(mc)+" 个任务记忆")

def main():
    args=set(sys.argv[1:]); quiet="--quiet" in args; heal="--heal" in args
    pn=next((int(sys.argv[i+1]) for i,a in enumerate(sys.argv) if a=="--pass-n" and i+1<len(sys.argv)),1)
    pn=max(1,min(pn,10))
    if not quiet:
        print("=== 开发管理合规检查 ==="); print("Codex 根:     "+str(CX)); print("管理系统:     "+str(DD))
        print("全局任务空间: "+str(TA)); print("全局技能库:   "+str(SK)); print("全局记忆库:   "+str(ME)); print()
    last_v=[]; passes=0
    for att in range(1,pn+1):
        if not quiet and pn>1: print("--- pass@"+str(att)+"/"+str(pn)+" ---")
        v=all_chk(); last_v=v
        if blocking(v):
            passes=0
            if heal:
                try:
                    from auto_heal import auto_heal
                    fxd,fl,_=auto_heal(v,dry_run=False)
                    if fxd>0 and not quiet: print("  [HEAL] 修复 "+str(fxd)+" 项，重试...")
                except: pass
            if not quiet: report(v)
            break
        else:
            passes=att
            if not quiet and att<pn:
                print("  PASSED" if not v else ""); report(v,"")
                if heal:
                    try:
                        from auto_heal import auto_heal
                        auto_heal(v,dry_run=False)
                    except: pass
    if pn>1 and passes==pn and not quiet: print(); print("PASSED 所有 "+str(pn)+" 次检查")
    if not quiet:
        if last_v and blocking(last_v): print("FAILED: 第 "+str(passes+1)+"/"+str(pn)+" 次检查未通过")
        stats()
    sys.exit(0 if passes>=pn else 1)

if __name__=="__main__":
    main()
