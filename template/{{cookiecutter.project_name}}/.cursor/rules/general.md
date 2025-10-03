# General Development Standards

## Documentation

- Update documentation when tasks are completed
- Document significant design decisions using ADRs
- Use appropriate document types for different purposes:
  - **ADR**: Documents WHY architectural decisions were made (technical choices)
  - **SPEC**: Details HOW to implement the solution (technical implementation)
- Reference all document in README.md

## Implementation Approach

- Implement next steps using available tools without confirmation
- Find root causes of issues using appropriate diagnostic tools
- Test and deploy after each change to verify success
- Iterate on components until they work correctly
- Test end-to-end workflows until they function properly
- Follow the structured development process in development_process.md
- Complete one small task at a time before moving to the next

## Technology Choices

- For frontend development: Use React, Tailwind CSS, and Material Tailwind
- For ML demos and interactive interfaces: Use Gradio
- For recurring command execution: Use taskfile.dev
