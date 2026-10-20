# IOMallocZero

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.15+

## Declaration

```c
void * IOMallocZero(vm_size_t size);
```

## See Also

### Allocation
- [IOMalloc](./api-1575326-iomalloc.md)
  Allocates general purpose, wired memory in the kernel map.
- [IOMallocAligned](./api-1575291-iomallocaligned.md)
  Allocates wired memory in the kernel map, with an alignment restriction.
- [IOMallocPageable](./api-1575327-iomallocpageable.md)
  Allocates pageable memory in the kernel map.
- [IORangeAllocator](./iorangeallocator.md)
  A utility class to manage allocations from a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3074962-iomalloczero)*