---
name: quality-gates
description: "Enforce code quality gates for all development tasks. Mandatory before every commit: code review, pattern discovery, entropy reduction, security check, test verification. Triggered by: any code change, before commit, before PR, when asked to review code."
---

# Quality Gates

## Mandatory Before Every Commit

Run through all 6 gates before marking any task complete:

### Gate 1: PRD Check
Verify that the PRD exists and was approved before implementation started.

### Gate 2: Pattern Discovery
Check if existing code in the codebase solves similar problems:
- Use `grep`/`rg` to find similar patterns
- Check file structure for established conventions
- Look for existing utilities or helpers

### Gate 3: Entropy Reduction
Ask: "What does the codebase look like after this change?"
- Can I delete code instead of adding it?
- Is this the minimal change?
- Would 2 functions work instead of 14?

### Gate 4: Self-Review Checklist
- [ ] No secrets, tokens, or credentials
- [ ] No `console.log()`, `print()`, `debug()` statements
- [ ] No commented-out code
- [ ] No files with unintended changes (formatting churn)
- [ ] Naming follows existing conventions
- [ ] File placed in correct directory
- [ ] Tests exist for new logic

### Gate 5: Commit Quality
- Commit scope is logical (one concern per commit)
- Subject line uses Conventional Commits: `type(scope): description`
- Body explains what changed and why, not implementation details

### Gate 6: Session Memory
- Update `dev/workspace/WORKSPACE.md` with progress
- Tick completed tasks in `dev/workspace/tasks/README.md`
- For multi-session work: save to `dev/workspace/history/`
