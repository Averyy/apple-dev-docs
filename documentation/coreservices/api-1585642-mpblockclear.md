# MPBlockClear

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Clears a block of memory. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
void MPBlockClear(LogicalAddress address, ByteCount size);
```

#### Discussion

As with all shared memory, your application must synchronize access to the memory blocks to avoid data corruption. `MPBlockClear` ensures the clearing stays within the bounds of the area specified by `size`, but the calling task can be preempted during the copying process. 

Note that you can call this function from an interrupt handler. 

## Parameters

- `address`: The starting address of the memory block you want to clear. 
- `size`: The number of bytes you want to clear. 

## See Also

### Memory Allocation Functions
- [MPAllocate](./api-1585756-mpallocate.md)
  Allocates a nonrelocatable memory block.
- [MPAllocateAligned](./api-1585774-mpallocatealigned.md)
  Allocates a nonrelocatable memory block.
- [MPBlockCopy](./api-1585707-mpblockcopy.md)
  Copies a block of memory.
- [MPFree](./api-1585676-mpfree.md)
  Frees memory allocated by `MPAllocateAligned`. 
- [MPGetAllocatedBlockSize](./api-1585717-mpgetallocatedblocksize.md)
  Returns the size of a memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585642-mpblockclear)*