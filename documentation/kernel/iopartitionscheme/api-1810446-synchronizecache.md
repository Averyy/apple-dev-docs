# synchronizeCache

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn synchronizeCache(
 IOService *client);
```

#### Return_value

Returns the status of the cache synchronization.

#### Overview

Flush the cached data in the storage object, if any, synchronously.

## Parameters

- `client`: Client requesting the cache synchronization.

## See Also

- [copyPhysicalExtent](iopartitionscheme/1810278-copyphysicalextent.md)
- [handleClose](iopartitionscheme/1810310-handleclose.md)
- [handleIsOpen](iopartitionscheme/1810337-handleisopen.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [lockPhysicalExtents](iopartitionscheme/1810387-lockphysicalextents.md)
- [read](iopartitionscheme/1810409-read.md)
- [unlockPhysicalExtents](iopartitionscheme/1810496-unlockphysicalextents.md)
- [unmap](iopartitionscheme/1810548-unmap.md)
- [write](iopartitionscheme/1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810446-synchronizecache)*