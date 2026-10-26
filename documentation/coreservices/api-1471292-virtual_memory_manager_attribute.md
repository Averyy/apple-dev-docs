# Virtual Memory Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Virtual Memory Manager.

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
- [gestaltVMAttr](./api-1471292-virtual_memory_manager_attribute/gestaltvmattr.md)
  The `Gestalt` selector you pass to determine the virtual memory attributes that are present.
- [gestaltVMPresent](./api-1471292-virtual_memory_manager_attribute/gestaltvmpresent.md)
  If `true`, virtual memory is present.
- [gestaltVMHasLockMemoryForOutput](./api-1471292-virtual_memory_manager_attribute/gestaltvmhaslockmemoryforoutput.md)
- [gestaltVMFilemappingOn](./api-1471292-virtual_memory_manager_attribute/gestaltvmfilemappingon.md)
- [gestaltVMHasPagingControl](./api-1471292-virtual_memory_manager_attribute/gestaltvmhaspagingcontrol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471292-virtual_memory_manager_attribute)*