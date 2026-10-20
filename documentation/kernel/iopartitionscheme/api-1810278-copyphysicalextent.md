# copyPhysicalExtent

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOStorage * copyPhysicalExtent(
 IOService *client, 
 UInt64 *byteStart, 
 UInt64 *byteCount);
```

#### Return Value

A reference to the physical storage object, which should be released by the caller, or a null on error.

#### Overview

Convert the specified byte offset into a physical byte offset, relative to a physical storage object. This call should only be made within the context of lockPhysicalExtents().

## Parameters

- `client`: Client requesting the operation.
- `byteStart`: Starting byte offset for the operation. Returns a physical byte offset, relative to the physical storage object, on success.
- `byteCount`: Size of the operation. Returns the actual number of bytes which can be transferred, relative to the physical storage object, on success.

## See Also

### Miscellaneous
- [handleClose](./api-1810310-handleclose.md)
- [handleIsOpen](./api-1810337-handleisopen.md)
- [handleOpen](./api-1810366-handleopen.md)
- [lockPhysicalExtents](./api-1810387-lockphysicalextents.md)
- [read](./api-1810409-read.md)
- [synchronizeCache](./api-1810446-synchronizecache.md)
- [unlockPhysicalExtents](./api-1810496-unlockphysicalextents.md)
- [unmap](./api-1810548-unmap.md)
- [write](./api-1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810278-copyphysicalextent)*