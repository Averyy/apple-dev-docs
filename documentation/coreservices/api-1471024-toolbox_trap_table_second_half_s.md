# Toolbox Trap Table (Second Half) Selector

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies address information for the second half of the Toolbox trap table.

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
- [gestaltExtToolboxTable](./api-1471024-toolbox_trap_table_second_half_s/gestaltexttoolboxtable.md)
  The base address of the second half of the Toolbox trap table if the table is discontiguous. If the table is contiguous, this selector returns 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471024-toolbox_trap_table_second_half_s)*