---
# Trigger - when should this workflow run?
on:
  workflow_dispatch:  # Manual trigger

# Engine configuration - switching to openai to avoid adapter tool restrictions
engine: openai
model: gpt-4o

# Permissions - what can this workflow access?
permissions:
  contents: read
  issues: read
  pull-requests: read

# Network access
network: defaults

# Safe outputs configuration
safe-outputs: {}
---

# my-first-workflow

Analyze this repository and create a helpful health and structure report.

## Instructions

Please perform the following steps:
1. Examine the root directory and list the key files and folders present in the repository.
2. Read the README.md file (if it exists) to understand what this project is about.
3. Create a new file named `REPOSITORY_HEALTH_REPORT.md` in the root of the repository using your file editing capabilities.
4. Inside `REPOSITORY_HEALTH_REPORT.md`, write a clear, professional summary of the repository's current structure, purpose, and contents, along with a few suggestions for next steps or improvements.

Be clear, professional, and concise in your report. Do not attempt to call external API tools or issue creation tools directly; simply write the report directly to the file.

## Notes

- Run `gh aw compile` to generate the GitHub Actions workflow
- See https://github.github.com/gh-aw/ for complete configuration options and tools documentation