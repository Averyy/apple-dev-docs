# Logical Page Size Selector

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies logical page size information.

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
- [gestaltLogicalPageSize](./api-1471519-logical_page_size_selector/gestaltlogicalpagesize.md)
  The logical page size. This value is defined only on machines with the MC68010, MC68020, MC68030, or MC68040 microprocessors. On a machine with the MC68000, the `Gestalt` function returns an error when called with this selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471519-logical_page_size_selector)*