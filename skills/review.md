# Review

Compare current branch to main: `git diff main...HEAD`
Check for:
- Logic errors and unhandled edge cases
- Security issues: SQL injection, XSS, unvalidated inputs, hardcoded secrets
- Missing error handling for operations that can fail
- Functions doing more than one thing
- Missing tests for new functionality
Report line numbers for each issue. Suggest specific fixes.
Rate: Ready / Needs Minor Work / Needs Major Work.
Be honest — do not approve code that has real problems.
