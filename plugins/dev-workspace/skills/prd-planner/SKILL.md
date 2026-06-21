---
name: prd-planner
description: "Create PRD-driven implementation plans. Use when asked to plan, architect, or design; starting a complex task; generating PRD or task lists. Follows PRD-first approach: clarify requirements → write PRD → get approval → break into tasks → implement sequentially."
---

# PRD Planner

## Workflow

```
User Request → Clarify → Write PRD → User Approves → Break into Tasks
→ Determine Mode (Quick/Single/Multi) → Implement Sequentially
```

## Step 1: Clarify

Ask 3-5 targeted questions when requirements are ambiguous. Use letter+number format for easy responses:

```
1. What is the primary goal?
   A. Improve X  B. Add Y  C. Fix Z
```

Only ask what can't be inferred. Focus on: scope, constraints, success criteria.

## Step 2: Write PRD

Use the template in `dev/workspace/plans/prd.md`. Fill every section.
Cover: overview, problem, goals, user stories, functional requirements, non-goals, success metrics.

## Step 3: User Approval

Present the PRD to the user. Do NOT proceed to implementation until approved.

## Step 4: Break into Tasks

### Phase 1: High-Level Tasks
- Generate 5±2 parent tasks
- Present to user → wait for "Go"
- Save to `dev/workspace/tasks/README.md`

### Phase 2: Sub-Tasks
- Break each parent into 2-5 sub-tasks
- Use markdown checkboxes: `- [ ] 1.1 sub-task`

## Step 5: Determine Mode

| Mode | Description |
|------|-------------|
| Quick | Direct implementation, no plan needed |
| Single | Plan once, then execute |
| Multi-stage | Iterative planning and execution |

## Step 6: Implement Sequentially

Work through tasks one at a time:
1. Pick first unchecked sub-task
2. Implement it
3. Tick checkbox: `- [ ]` → `- [x]`
4. After each parent task, pause for user review
