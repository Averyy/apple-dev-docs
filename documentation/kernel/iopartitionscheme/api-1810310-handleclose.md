# handleClose

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual void handleClose(
 IOService *client,
 IOOptionBitsoptions);
```

#### Overview

The handleClose method closes the client's access to this object.

This implementation replaces the IOService definition of handleClose().

## Parameters

- `client`: Client requesting the close.
- `options`: Options for the close. Set to zero.

## See Also

- [copyPhysicalExtent](iopartitionscheme/1810278-copyphysicalextent.md)
- [handleIsOpen](iopartitionscheme/1810337-handleisopen.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [lockPhysicalExtents](iopartitionscheme/1810387-lockphysicalextents.md)
- [read](iopartitionscheme/1810409-read.md)
- [synchronizeCache](iopartitionscheme/1810446-synchronizecache.md)
- [unlockPhysicalExtents](iopartitionscheme/1810496-unlockphysicalextents.md)
- [unmap](iopartitionscheme/1810548-unmap.md)
- [write](iopartitionscheme/1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810310-handleclose)*