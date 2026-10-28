# MPAllocate

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allocates a nonrelocatable memory block.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use `MPAllocateAligned` instead.

## Declaration

```c
LogicalAddress MPAllocate(ByteCount size);
```

## Return Value

A pointer to the allocated memory. If the function cannot allocate the requested memory or the requested alignment, the returned address is `NULL`.

## Parameters

- `size`: The size, in bytes, of the memory block to allocate.

## See Also

### Memory Allocation Functions
- [MPAllocateAligned](./api-1585774-mpallocatealigned.md)
  Allocates a nonrelocatable memory block.
- [MPBlockClear](./api-1585642-mpblockclear.md)
  Clears a block of memory. 
- [MPBlockCopy](./api-1585707-mpblockcopy.md)
  Copies a block of memory.
- [MPFree](./api-1585676-mpfree.md)
  Frees memory allocated by `MPAllocateAligned`. 
- [MPGetAllocatedBlockSize](./api-1585717-mpgetallocatedblocksize.md)
  Returns the size of a memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585756-mpallocate)*