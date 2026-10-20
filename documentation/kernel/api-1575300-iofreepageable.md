# IOFreePageable

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Frees memory allocated with IOMallocPageable.

**Availability**:
- macOS 10.0+

## Declaration

```c
void IOFreePageable(void *address, vm_size_t size);
```

#### Discussion

This function frees memory allocated with IOMallocPageable, it may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `address`: Virtual address of the allocated memory.
- `size`: Size of the memory allocated.

## See Also

### Deallocation
- [IOFree](./api-1575290-iofree.md)
  Frees memory allocated with IOMalloc.
- [IOFreeAligned](./api-1575330-iofreealigned.md)
  Frees memory allocated with IOMallocAligned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575300-iofreepageable)*