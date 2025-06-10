# copyPhysicalExtent

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOStorage * copyPhysicalExtent(
 IOService *client, 
 UInt64 *byteStart, 
 UInt64 *byteCount);
```

#### Return_value

A reference to the physical storage object, which should be released by the caller, or a null on error.

#### Overview

Convert the specified byte offset into a physical byte offset, relative to a physical storage object. This call should only be made within the context of lockPhysicalExtents().

## Parameters

- `client`: Client requesting the operation.
- `byteStart`: Starting byte offset for the operation. Returns a physical byte offset, relative to the physical storage object, on success.
- `byteCount`: Size of the operation. Returns the actual number of bytes which can be transferred, relative to the physical storage object, on success.

## See Also

- [handleClose](iopartitionscheme/1810310-handleclose.md)
- [handleIsOpen](iopartitionscheme/1810337-handleisopen.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [lockPhysicalExtents](iopartitionscheme/1810387-lockphysicalextents.md)
- [read](iopartitionscheme/1810409-read.md)
- [synchronizeCache](iopartitionscheme/1810446-synchronizecache.md)
- [unlockPhysicalExtents](iopartitionscheme/1810496-unlockphysicalextents.md)
- [unmap](iopartitionscheme/1810548-unmap.md)
- [write](iopartitionscheme/1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810278-copyphysicalextent)*