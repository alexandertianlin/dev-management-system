# WORKSPACE.md

Branch workspace context for Claude and humans. Not read by the dev-workspace script.

*Load into Claude's context with: `@dev/workspace/WORKSPACE.md`*

## Branch

**Name:**
**Started:**
**Status:**

- [ ] In Progress
- [ ] Discard (workspace and branch abandoned)
- [ ] Complete (ready to merge)

## Purpose

%% Claude: write a brief purpose statement when creating the workspace %%

## Workflow Mode

- [ ] Quick (direct implementation, no PRD needed)
- [ ] Single plan (plan once, execute)
- [ ] Multi-stage plan (iterative planning)

## Quality Gates Status

- [ ] PRD approved (`dev/workspace/plans/prd.md`)
- [ ] Architecture designed (`dev/workspace/plans/architectural.md`)
- [ ] Task list created (`dev/workspace/tasks/README.md`)
- [ ] All tasks verified (secrets, tests, conventions)
- [ ] Session memory saved (`dev/workspace/history/`)

## Track Issues

- [ ] Track GitHub issues
    - <!-- Add issue numbers: #123, #456 -->

## Testing

- [ ] Requires testing
  > Update relevant tests as per testing strategy. All tests must pass before PR.

## Plans

Read at session start before working:

- [ ] `dev/workspace/plans/prd.md`
- [ ] `dev/workspace/plans/architectural.md`
- [ ] `dev/workspace/context/tree.md`

## Completed Tasks

_Tick tasks in `dev/workspace/tasks/README.md` as you complete them._

## Discoveries

- %% Claude: record discoveries here as you work %%
