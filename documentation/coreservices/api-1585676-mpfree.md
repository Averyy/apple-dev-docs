# MPFree

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Frees memory allocated by `MPAllocateAligned`. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
void MPFree(LogicalAddress object);
```

#### Discussion

Also see the function  [`MPAllocateAligned`](./api-1585774-mpallocatealigned.md). 

## Parameters

- `object`: A pointer to the memory you want to release. 

## See Also

### Memory Allocation Functions
- [MPAllocate](./api-1585756-mpallocate.md)
  Allocates a nonrelocatable memory block.
- [MPAllocateAligned](./api-1585774-mpallocatealigned.md)
  Allocates a nonrelocatable memory block.
- [MPBlockClear](./api-1585642-mpblockclear.md)
  Clears a block of memory. 
- [MPBlockCopy](./api-1585707-mpblockcopy.md)
  Copies a block of memory.
- [MPGetAllocatedBlockSize](./api-1585717-mpgetallocatedblocksize.md)
  Returns the size of a memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585676-mpfree)*