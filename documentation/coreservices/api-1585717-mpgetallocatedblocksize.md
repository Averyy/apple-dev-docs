# MPGetAllocatedBlockSize

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the size of a memory block.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
ByteCount MPGetAllocatedBlockSize(LogicalAddress object);
```

#### Return Value

The size of the allocated memory block, in bytes. 

## Parameters

- `object`: The address of the memory block whose size you want to determine. 

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
- [MPFree](./api-1585676-mpfree.md)
  Frees memory allocated by `MPAllocateAligned`. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585717-mpgetallocatedblocksize)*