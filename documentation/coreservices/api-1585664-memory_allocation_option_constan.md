# Memory Allocation Option Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify optional actions when calling the `MPAllocateAligned` function. 

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kMPAllocateClearMask](./api-1585664-memory_allocation_option_constan/kmpallocateclearmask.md)
  Zero out the allocated memory block.
- [kMPAllocateGloballyMask](./api-1585664-memory_allocation_option_constan/kmpallocategloballymask.md)
- [kMPAllocateResidentMask](./api-1585664-memory_allocation_option_constan/kmpallocateresidentmask.md)
  Allocate memory from resident memory only (that is, the allocated memory is not pageable).
- [kMPAllocateNoGrowthMask](./api-1585664-memory_allocation_option_constan/kmpallocatenogrowthmask.md)
  Do not attempt to grow the pool of available memory. Specifying this option is useful, as attempting to grow memory may cause your task to block until such memory becomes available. 
- [kMPAllocateNoCreateMask](./api-1585664-memory_allocation_option_constan/kmpallocatenocreatemask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585664-memory_allocation_option_constan)*