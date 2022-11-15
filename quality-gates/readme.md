Shifting left

- Automated tests
  - Unit tests
    - TDD or not?
    - How to write testable code
  - Higher-level tests
    - ATDD/BDD

- Static code analysis, type-checking, linting
  - Run these checks both in CI pipeline and locally (pre-commit hook). Even better, leverage 
    IDE plugins for instant feedback!
  - essential in a dynamically typed language!
  - Static code analysis is the lowest-hanging fruit - you just set it up, and you don't even 
    have to write the tests yourself!

- Code complexity checks?

Tools:
- pylint:
  - Track config in version control to make sure it behaves identically for everyone
  - Overriding false positives:
    - If you have to override it, don't be lazy and use abbreviated code - Use proper error name 
      (e.g., `pylint: disable='no-member'` rather than `disable=E1101`
    - Since overriding is not primarily for human consumption, it is ok to go beyond the line 
      length limit. Likewise, it's ok to add an inline comment - no need to add an extra line.