---
# Trigger - when should this workflow run?
on:
  workflow_dispatch:  # Manual trigger

# Engine configuration - using copilot engine
engine: copilot
model: gpt-4o

# Permissions - grant copilot-requests write access for native token integration
permissions:
  contents: read
  issues: read
  pull-requests: read
  copilot-requests: write

# Network access
network: defaults

# Safe outputs configuration - keep empty to avoid unsupported custom tool calls
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

Be clear, professional, and concise in your report. Do not attempt to call external API tools or custom tool wrappers; simply write the report directly to the file via standard file modification.