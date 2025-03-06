[//]: # (File: developmentGuidelines.md)
[//]: # (Author: David Diaz (https://github.com/alfdav))
[//]: # (Last Updated: March 6, 2025, 11:38 AM (America/Chicago, UTC-6:00))
[//]: # (Description: Documents the development guidelines and principles for the curlthis project)

# Development Guidelines

- KISS (Keep It Simple, Stupid)

    - Write simple, clear code
    - Avoid unnecessary complexity
    - If it seems complex, you're probably doing it wrong
    - Ask yourself: "Could a junior developer understand this?"
    
-   YAGNI (You Aren't Gonna Need It)

    - Only implement what is needed NOW
    - Don't add features for future use cases
    - If it's not in progress.md, don't build it
    - Remove any speculative code
    
-   SOLID Principles

    - **S**ingle Responsibility: One purpose per class/module
    - **O**pen-Closed: Open for extension, closed for modification
    - **L**iskov Substitution: Derived classes must be substitutable
    - **I**nterface Segregation: Many specific interfaces over one general
    - **D**ependency Inversion: Depend on abstractions
    
-   Law of Demeter

    - Objects only talk to immediate friends
    - No method call chains (a.b().c().d())
    - Keep dependencies minimal
    - Loose coupling between components
    
-   Documentation Standards (2025-03-06 11:34)

    - All source files must include author headers
    - Memory bank updates must include short-format date/time stamps
    - Updates to memory bank files should be appended, not overwritten
    - Documentation should be clear, concise, and comprehensive
    - Follow the detailed guidelines in `styling_standards/documentation_styling_guidelines.md` (2025-03-06 11:40)