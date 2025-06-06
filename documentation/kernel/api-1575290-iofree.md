# IOFree

**Framework**: Kernel  
**Kind**: func

Frees memory allocated with IOMalloc.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void IOFree(void *address, vm_size_t size);
```

#### Discussion

This function frees memory allocated with IOMalloc, it may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `address`: Pointer to the allocated memory. Must be identical to result @of a prior IOMalloc.
- `size`: Size of the memory allocated. Must be identical to size of @the corresponding IOMalloc

## See Also

- [IOFreeAligned](1575330-iofreealigned.md)
  Frees memory allocated with IOMallocAligned.
- [IOFreePageable](1575300-iofreepageable.md)
  Frees memory allocated with IOMallocPageable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575290-iofree)*