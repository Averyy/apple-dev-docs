# Toolbox Trap Table Selector

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies base address information for the Toolbox trap dispatch table.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltToolboxTable](./api-1471440-toolbox_trap_table_selector/gestalttoolboxtable.md)
  The selector you pass to the `Gestalt` function to determine the base address of the Toolbox trap dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471440-toolbox_trap_table_selector)*