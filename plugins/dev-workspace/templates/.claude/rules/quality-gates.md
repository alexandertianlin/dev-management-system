# Quality Gates

Every development task MUST pass through these quality gates.

## Gate 1: PRD & Planning (Before Coding)
- [ ] PRD exists with goals, user stories, and acceptance criteria
- [ ] PRD approved by user
- [ ] Task list generated with checkboxes
- [ ] Architecture design documented for complex features

## Gate 2: Pattern Discovery (During Planning)
- [ ] Checked for existing patterns that can be reused
- [ ] Codebase examined for similar implementations
- [ ] Conventions identified and followed

## Gate 3: Entropy Check (Before Writing)
- [ ] Can we remove code instead of adding it?
- [ ] Is this the minimal change that solves the problem?
- [ ] Does this make the codebase easier or harder to maintain?

## Gate 4: Self-Review (After Implementation)
- [ ] No secrets or sensitive data leaked
- [ ] No debug logging left behind
- [ ] No dead code or commented-out code
- [ ] Code follows project conventions (naming, file structure)
- [ ] Tests exist and pass
- [ ] No unrelated formatting churn

## Gate 5: Commit Quality
- [ ] Logical commit boundaries (split unrelated changes)
- [ ] Conventional Commits format (type(scope): description)
- [ ] Clear messages describing what changed and why
- [ ] Fastest meaningful verification run (lint/test)

## Gate 6: Session Memory
- [ ] Significant decisions recorded
- [ ] Progress updated in WORKSPACE.md
- [ ] Task list checkboxes updated
- [ ] Session summary saved to history/
