# MPAllocateAligned

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allocates a nonrelocatable memory block.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
LogicalAddress MPAllocateAligned(ByteCount size, UInt8 alignment, OptionBits options);
```

#### Return Value

A pointer to the allocated memory. If the function cannot allocate the requested memory or the requested alignment, the returned address is `NULL`. 

#### Discussion

The memory referenced by the returned address is guaranteed to be accessible by the application's cooperative task and any preemptive tasks that it creates, but not by other applications or their preemptive tasks. Any existing non-global heap blocks are freed when the application terminates. As with all shared memory, you must explicitly synchronize access to allocated heap blocks using a notification mechanism.

You can replicate the effect of the older `MPAllocate` function by calling `MPAllocateAligned` with 32-byte alignment and no options. 

Also see the function  [`MPFree`](./api-1585676-mpfree.md). 

##### Special Considerations

macOS does not support allocation of global (cross address space) or resident memory with this function. In addition, passing the `kMPAllocateNoGrowthMask` constant in the `options` parameter has no effect in macOS, since memory allocation is done with sparse heaps.

## Parameters

- `size`: The size, in bytes, of the memory block to allocate. 
- `alignment`: The desired alignment of the allocated memory block. See [Memory Allocation Alignment Constants](./api-1585698-memory_allocation_alignment_cons.md) for a list of possible values to pass. Note that there will be a minimum alignment regardless of the requested alignment. If the requested memory block is 4 bytes or smaller, the block will be at least 4-byte aligned. If the requested block is greater than 4 bytes, the block will be at least 8-byte aligned. 
- `options`: Any optional information to use with this call. See [Memory Allocation Option Constants](./api-1585664-memory_allocation_option_constan.md) for a list of possible values to pass. 

## See Also

### Memory Allocation Functions
- [MPAllocate](./api-1585756-mpallocate.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585774-mpallocatealigned)*