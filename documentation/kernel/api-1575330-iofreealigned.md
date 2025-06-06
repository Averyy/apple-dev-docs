# IOFreeAligned

**Framework**: Kernel  
**Kind**: func

Frees memory allocated with IOMallocAligned.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void IOFreeAligned(void *address, vm_size_t size);
```

#### Discussion

This function frees memory allocated with IOMallocAligned, it may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `address`: Pointer to the allocated memory.
- `size`: Size of the memory allocated.

## See Also

- [IOFree](1575290-iofree.md)
  Frees memory allocated with IOMalloc.
- [IOFreePageable](1575300-iofreepageable.md)
  Frees memory allocated with IOMallocPageable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575330-iofreealigned)*