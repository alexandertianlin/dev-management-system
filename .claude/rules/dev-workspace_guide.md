# Dev-Workspace Guidance

This project uses **dev-workspace**, an integrated toolset for AI agents.

## IMPORTANT

**TRUST THE DEV-WORKSPACE SKILL AND COMMANDS.** Use dev-workspace commands to manage your workspace.

## Concept

dev-workspace creates isolated workspaces to keep work and context scoped to the task at hand.

## State

Ask for user guidance at these milestones:
- **Starting new feature** → Create workspace, set up WORKSPACE.md
- **Starting new work** → Sync workspace, check saved context
- **Work finished** → Merge back, archive, commit workspace
- **Major features** → Work finished + quality gates passed

## MANDATORY DEVELOPMENT WORKFLOW

ALL development tasks MUST follow this pipeline:

### Phase 0: Workspace Setup
- Create or verify `dev/workspace/` structure
- Read `dev/workspace/WORKSPACE.md` for branch context

### Phase 1: PRD & Plan
- For any feature > 30 min: start with a PRD
- Write to `dev/workspace/plans/prd.md`
- Get user approval before implementing

### Phase 2: Task Breakdown
- Create task list with checkboxes in `dev/workspace/tasks/README.md`
- Work one task at a time, tick as you go

### Phase 3: Quality Gates
- Check `quality-gates` rule before every commit
- Verify: no secrets, no debug logging, tests pass, conventions followed

### Phase 4: Implement
- One sub-task at a time
- Tick checkboxes: `- [ ]` → `- [x]`

### Phase 5: Commit
- Conventional Commits format
- Logical commit boundaries

### Phase 6: Memory
- Update WORKSPACE.md with progress
- Save session summary to `dev/workspace/history/`

## Workspace Directories
- **context/** — Project context and discoveries
- **plans/** — PRD and architecture docs
- **tasks/** — Task lists with checkboxes ✓
- **history/** — Session summaries
- **reviews/** — Review artifacts
- **research/** — Research output
- **filebox/** — Temporary files

## Skills Added
- **quality-gates** — Code quality enforcement (secrets, tests, conventions)
- **prd-planner** — PRD-driven planning with template

## Chat Histories
Each workspace has conversations recorded in `/history`. Each history file has a max 5-line summary near the top.
