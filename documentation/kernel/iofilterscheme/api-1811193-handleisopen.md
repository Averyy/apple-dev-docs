# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual bool handleIsOpen(
 const IOService *client) const;
```

## Return Value

Returns true if the client was (or clients were) open, false otherwise.

## Overview

The handleIsOpen method determines whether the specified client, or any client if none is specified, presently has an open on this object.

This implementation replaces the IOService definition of handleIsOpen().

## Parameters

- `client`: Client to check the open state of. Set to zero to check the open state of all clients.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1811149-copyphysicalextent.md)
- [handleClose](./api-1811170-handleclose.md)
- [handleOpen](./api-1811211-handleopen.md)
- [lockPhysicalExtents](./api-1811226-lockphysicalextents.md)
- [read](./api-1811238-read.md)
- [synchronizeCache](./api-1811248-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811258-unlockphysicalextents.md)
- [unmap](./api-1811266-unmap.md)
- [write](./api-1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811193-handleisopen)*