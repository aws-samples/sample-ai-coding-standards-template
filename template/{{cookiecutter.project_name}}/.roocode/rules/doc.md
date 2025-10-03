---
inclusion: fileMatch
fileMatchPattern: "docs/*.md"
---
# Documentation

## Architecture

- Document significant design decisions using ADRs
- Include status, context, decision, consequences in ADRs
- Create visual diagrams using MermaidJS (sequence, architecture, flowchart, UML)
- Reference related ADRs to show decision dependencies
- Name project documentation files consistently:
  - `README.md` - Project overview and getting started guide
  - `ARCHITECTURE.md` - System architecture overview
  - `CONTRIBUTING.md` - Contribution guidelines
  - `DEPLOYMENT.md` - Deployment procedures
  - `API.md` - API documentation
- Always use absolute paths when referencing files in documentation (e.g., `/src/components/Button.tsx` not `components/Button.tsx`)
- Include file extensions in all file references
- When documenting directory structures, use tree format with trailing slashes for directories
