# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual bool handleIsOpen(
 const IOService *client) const;
```

#### Return Value

Returns true if the client was (or clients were) open, false otherwise.

#### Overview

The handleIsOpen method determines whether the specified client, or any client if none is specified, presently has an open on this object.

This implementation replaces the IOService definition of handleIsOpen().

## Parameters

- `client`: Client to check the open state of. Set to zero to check the open state of all clients.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1810278-copyphysicalextent.md)
- [handleClose](./api-1810310-handleclose.md)
- [handleOpen](./api-1810366-handleopen.md)
- [lockPhysicalExtents](./api-1810387-lockphysicalextents.md)
- [read](./api-1810409-read.md)
- [synchronizeCache](./api-1810446-synchronizecache.md)
- [unlockPhysicalExtents](./api-1810496-unlockphysicalextents.md)
- [unmap](./api-1810548-unmap.md)
- [write](./api-1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810337-handleisopen)*