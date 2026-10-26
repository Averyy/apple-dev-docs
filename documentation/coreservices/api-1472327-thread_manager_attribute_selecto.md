# Thread Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Thread Manager.

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
- [gestaltThreadMgrAttr](./api-1472327-thread_manager_attribute_selecto/gestaltthreadmgrattr.md)
- [gestaltThreadMgrPresent](./api-1472327-thread_manager_attribute_selecto/gestaltthreadmgrpresent.md)
  This bit is set if the Thread Manager is present.
- [gestaltSpecificMatchSupport](./api-1472327-thread_manager_attribute_selecto/gestaltspecificmatchsupport.md)
  This bit is set if the Thread Manager supports the allocation of threads based on an exact match with the requested stack size. If this bit is not set, the Thread Manager allocates threads based on the closest match to the requested stack size.
- [gestaltThreadsLibraryPresent](./api-1472327-thread_manager_attribute_selecto/gestaltthreadslibrarypresent.md)
  This bit is set if the native version of the threads library has been loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472327-thread_manager_attribute_selecto)*