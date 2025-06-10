# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual bool handleIsOpen(
 const IOService *client) const;
```

#### Return_value

Returns true if the client was (or clients were) open, false otherwise.

#### Overview

The handleIsOpen method determines whether the specified client, or any client if none is specified, presently has an open on this object.

This implementation replaces the IOService definition of handleIsOpen().

## Parameters

- `client`: Client to check the open state of. Set to zero to check the open state of all clients.

## See Also

- [copyPhysicalExtent](iopartitionscheme/1810278-copyphysicalextent.md)
- [handleClose](iopartitionscheme/1810310-handleclose.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [lockPhysicalExtents](iopartitionscheme/1810387-lockphysicalextents.md)
- [read](iopartitionscheme/1810409-read.md)
- [synchronizeCache](iopartitionscheme/1810446-synchronizecache.md)
- [unlockPhysicalExtents](iopartitionscheme/1810496-unlockphysicalextents.md)
- [unmap](iopartitionscheme/1810548-unmap.md)
- [write](iopartitionscheme/1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810337-handleisopen)*