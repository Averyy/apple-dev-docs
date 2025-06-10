# unmap

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn unmap(
 IOService *client, 
 IOStorageExtent *extents, 
 UInt32extentsCount, 
 UInt32 options = 0);
```

#### Return_value

Returns the status of the operation.

#### Overview

Delete unused data from the storage object at the specified byte offsets, synchronously.

## Parameters

- `client`: Client requesting the operation.
- `extents`: List of extents. See IOStorageExtent. It is legal for the callee to overwrite the contents of this buffer in order to satisfy the request.
- `extentsCount`: Number of extents.

## See Also

- [copyPhysicalExtent](iopartitionscheme/1810278-copyphysicalextent.md)
- [handleClose](iopartitionscheme/1810310-handleclose.md)
- [handleIsOpen](iopartitionscheme/1810337-handleisopen.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [lockPhysicalExtents](iopartitionscheme/1810387-lockphysicalextents.md)
- [read](iopartitionscheme/1810409-read.md)
- [synchronizeCache](iopartitionscheme/1810446-synchronizecache.md)
- [unlockPhysicalExtents](iopartitionscheme/1810496-unlockphysicalextents.md)
- [write](iopartitionscheme/1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810548-unmap)*