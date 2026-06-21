---
description: "Run quality gates on current changes. Checks for: secrets, debug logging, dead code, test coverage, conventions. Provides a fix list for any issues found."
argument-hint: ""
allowed-tools: Read, Write, Bash, Grep
---

# Review Command

Run all quality gates on the current state of the codebase.

## Checks

1. **Secret scan** — `rg` for tokens, passwords, API keys in staged/diff files
2. **Debug logging** — `rg` for console.log, print, debug statements
3. **Dead code** — Check for commented-out code blocks
4. **Test check** — Verify tests exist for modified files
5. **Conventions** — Check naming, file structure against codebase patterns
6. **Entropy check** — Can this be done with less code?

## Output

Issue list with severity: HIGH / MEDIUM / LOW
