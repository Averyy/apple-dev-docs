# kMPAllocateInterlockAligned

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
kMPAllocateInterlockAligned = 255
```

## Discussion

Use interlock alignment, which is the alignment needed to allow the use of CPU interlock instructions (that is, `lwarx` and `stwcx`.) on the returned memory address. This alignment is set at runtime. In most cases you would never need to use this alignment. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585698-memory_allocation_alignment_cons/kmpallocateinterlockaligned)*