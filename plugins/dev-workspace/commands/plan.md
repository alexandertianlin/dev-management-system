---
description: "Create a PRD-driven plan with task breakdown. Asks clarifying questions, writes PRD, generates tasks."
argument-hint: "<feature description>"
allowed-tools: Read, Write, Bash, AskUser
---

# Plan Command

Create a PRD-driven implementation plan for a feature.

## Workflow

1. Analyze the user's feature request
2. Ask 3-5 clarifying questions (numbered with letter options)
3. Write PRD to `dev/workspace/plans/prd.md`
4. Present PRD to user for approval
5. Generate high-level tasks
6. Present tasks → wait for "Go"
7. Break into sub-tasks
8. Save to `dev/workspace/tasks/README.md`

## PRD Template Sections
- Overview, Problem, Goals, User Stories
- Functional Requirements (Must/Should/Nice)
- Non-Goals, Success Metrics
- Design/Technical Considerations
- Open Questions

## Task Format
```markdown
- [ ] 1.0 Parent Task
  - [ ] 1.1 Sub-task
  - [ ] 1.2 Sub-task
```

Save to `dev/workspace/tasks/README.md` with Relevant Files section.
