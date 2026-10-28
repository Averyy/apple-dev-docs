# MPBlockCopy

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Copies a block of memory.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
void MPBlockCopy(LogicalAddress source, LogicalAddress destination, ByteCount size);
```

## Discussion

This function simply calls through to the Driver Services Library function `BlockMoveData`. Note that you should not make any assumptions about the state of the destination memory while this function is executing. In the intermediate state, values may be present that are neither the original nor the final ones. For example, this function may use the `'dcbz'` instruction. If the underlying memory is not cacheable, if the memory is write-through instead of copy-back, or if the cache block is flushed for some reason, the `'dcbz'` instruction will write zeros to the destination. You can avoid the use of the `'dcbz'` instruction by calling `BlockMoveDataUncached`, but even that function makes no other guarantees about the memory block's intermediate state.

As with all shared memory, your application must synchronize access to the memory blocks to avoid data corruption. `MPBlockCopy` ensures the copying stays within the bounds of the area specified by `size`, but the calling task can be preempted during the copying process. 

Note that you can call this function from an interrupt handler. 

## Parameters

- `source`: The starting address of the memory block you want to copy. 
- `destination`: The location to which you want to copy the memory block.
- `size`: The number of bytes to copy. 

## See Also

### Memory Allocation Functions
- [MPAllocate](./api-1585756-mpallocate.md)
  Allocates a nonrelocatable memory block.
- [MPAllocateAligned](./api-1585774-mpallocatealigned.md)
  Allocates a nonrelocatable memory block.
- [MPBlockClear](./api-1585642-mpblockclear.md)
  Clears a block of memory. 
- [MPFree](./api-1585676-mpfree.md)
  Frees memory allocated by `MPAllocateAligned`. 
- [MPGetAllocatedBlockSize](./api-1585717-mpgetallocatedblocksize.md)
  Returns the size of a memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585707-mpblockcopy)*