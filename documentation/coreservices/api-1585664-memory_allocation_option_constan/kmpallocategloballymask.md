# kMPAllocateGloballyMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
kMPAllocateGloballyMask = 0x0002
```

#### Discussion

Allocate memory from in memory space that is visible to all processes. Note that such globally-allocated space is not automatically reclaimed when the allocating process terminates. By default, [`MPAllocateAligned`](../api-1585774-mpallocatealigned.md) allocates memory from process-specific (that is, not global) memory. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585664-memory_allocation_option_constan/kmpallocategloballymask)*