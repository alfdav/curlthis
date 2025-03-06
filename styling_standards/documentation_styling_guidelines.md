# Documentation Styling Guidelines

## Overview

This document outlines the standardized styling guidelines for documentation in the curlthis project. Following these guidelines ensures consistency across all project documentation and makes it easier for developers to maintain and update the codebase.

## File Headers

### Source Code Files

All source code files should include a standardized header in the docstring format:

```python
"""
Brief description of the module/file

Author: David Diaz (https://github.com/alfdav)
Version: 0.1.0
"""
```

### Memory Bank Files

All memory bank files should use Markdown-style comments for the header:

```markdown
[//]: # (File: filename.md)
[//]: # (Author: David Diaz (https://github.com/alfdav))
[//]: # (Last Updated: YYYY-MM-DD HH:MM (Timezone))
[//]: # (Description: Brief description of the file's purpose)
```

## Memory Bank Updates

When updating memory bank files, follow these guidelines:

1. **Append, Don't Overwrite**: Updates should be appended to the existing content, not overwritten.
2. **Timestamp Format**: Each update must include a timestamp in short format (YYYY-MM-DD HH:MM).
3. **Update Location**: Updates should be placed within the relevant sections of the document.

Example of an update:

```markdown
- Added new feature X (2025-03-06 11:40)
```

## Documentation Format

### Markdown Formatting

- Use appropriate heading levels (# for main title, ## for sections, etc.)
- Use consistent list formatting:
  - Unordered lists with `-` or `*`
  - Ordered lists with numbers
- Code blocks should use triple backticks with language specification:
  ```python
  def example_function():
      return "This is an example"
  ```

### Content Structure

- Each memory bank file has a specific purpose and should focus on that aspect
- Use clear, concise language
- Organize content logically with appropriate sections and subsections
- Include examples where helpful

## File-Specific Guidelines

### activeContext.md

- Document current work in progress
- List recent changes with timestamps
- Outline next steps

### systemPatterns.md

- Document architecture and system patterns
- Explain key technical decisions
- Describe how the system is built

### techContext.md

- List technologies used with version requirements
- Explain development setup
- Document technical constraints

### progress.md

- Track what works and what's left to build
- Maintain progress status percentages
- Document completed features

### productContext.md

- Explain why the project exists
- Document problems it solves
- Describe how it should work
- Document naming conventions

### developmentGuidelines.md

- Document development principles (KISS, YAGNI, etc.)
- Include coding standards
- Document documentation requirements

## Maintenance

These documentation styling guidelines should be reviewed and updated periodically to ensure they remain relevant and effective. Any changes to these guidelines should be documented with a timestamp and rationale.

Last Updated: 2025-03-06 11:40