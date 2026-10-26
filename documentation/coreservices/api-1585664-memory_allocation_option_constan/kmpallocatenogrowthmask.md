# kMPAllocateNoGrowthMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

Do not attempt to grow the pool of available memory. Specifying this option is useful, as attempting to grow memory may cause your task to block until such memory becomes available. 

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
kMPAllocateNoGrowthMask = 0x0010
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585664-memory_allocation_option_constan/kmpallocatenogrowthmask)*