# unlockPhysicalExtents

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual void unlockPhysicalExtents(
 IOService *client);
```

#### Overview

Unlock the contents of the storage object for relocation again. This call must balance a successful call to lockPhysicalExtents().

## Parameters

- `client`: Client requesting the operation.

## See Also

- [copyPhysicalExtent](iopartitionscheme/1810278-copyphysicalextent.md)
- [handleClose](iopartitionscheme/1810310-handleclose.md)
- [handleIsOpen](iopartitionscheme/1810337-handleisopen.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [lockPhysicalExtents](iopartitionscheme/1810387-lockphysicalextents.md)
- [read](iopartitionscheme/1810409-read.md)
- [synchronizeCache](iopartitionscheme/1810446-synchronizecache.md)
- [unmap](iopartitionscheme/1810548-unmap.md)
- [write](iopartitionscheme/1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810496-unlockphysicalextents)*