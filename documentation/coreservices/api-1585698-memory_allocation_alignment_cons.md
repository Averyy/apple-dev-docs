# Memory Allocation Alignment Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify the alignment of the desired memory block when calling the `MPAllocateAligned` function.

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
- [kMPAllocateDefaultAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocatedefaultaligned.md)
  Use the default alignment.
- [kMPAllocate8ByteAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocate8bytealigned.md)
  Use 8-byte alignment.
- [kMPAllocate16ByteAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocate16bytealigned.md)
  Use 16-byte alignment.
- [kMPAllocate32ByteAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocate32bytealigned.md)
  Use 32-byte alignment. 
- [kMPAllocate1024ByteAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocate1024bytealigned.md)
  Use 1024-byte alignment.
- [kMPAllocate4096ByteAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocate4096bytealigned.md)
  Use 4096-byte alignment.
- [kMPAllocateMaxAlignment](./api-1585698-memory_allocation_alignment_cons/kmpallocatemaxalignment.md)
  Use the maximum alignment (65536 byte).
- [kMPAllocateAltiVecAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocatealtivecaligned.md)
  Use AltiVec alignment.
- [kMPAllocateVMXAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocatevmxaligned.md)
  Use VMX (now called AltiVec) alignment.
- [kMPAllocateVMPageAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocatevmpagealigned.md)
  Use virtual memory page alignment. This alignment is set at runtime. 
- [kMPAllocateInterlockAligned](./api-1585698-memory_allocation_alignment_cons/kmpallocateinterlockaligned.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585698-memory_allocation_alignment_cons)*