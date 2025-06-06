# IOMalloc

**Framework**: Kernel  
**Kind**: func

Allocates general purpose, wired memory in the kernel map.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void * IOMalloc(vm_size_t size);
```

#### Return_value

Pointer to the allocated memory, or zero on failure.

#### Discussion

This is a general purpose utility to allocate memory in the kernel. There are no alignment guarantees given on the returned memory, and alignment may vary depending on the kernel configuration. This function may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `size`: Size of the memory requested.

## See Also

- [IOMallocAligned](1575291-iomallocaligned.md)
  Allocates wired memory in the kernel map, with an alignment restriction.
- [IOMallocPageable](1575327-iomallocpageable.md)
  Allocates pageable memory in the kernel map.
- [IOMallocZero](3074962-iomalloczero.md)
- [IORangeAllocator](iorangeallocator.md)
  A utility class to manage allocations from a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575326-iomalloc)*