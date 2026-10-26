# gestaltSpecificMatchSupport

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

This bit is set if the Thread Manager supports the allocation of threads based on an exact match with the requested stack size. If this bit is not set, the Thread Manager allocates threads based on the closest match to the requested stack size.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltSpecificMatchSupport = 1
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472327-thread_manager_attribute_selecto/gestaltspecificmatchsupport)*