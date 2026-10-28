# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual bool handleIsOpen(
 const IOService *client) const = 0;
```

## Return Value

Returns true if the client was (or clients were) open, false otherwise.

## Overview

The handleIsOpen method determines whether the specified client, or any client if none is specified, presently has an open on this object.

## Parameters

- `client`: Client to check the open state of. Set to zero to check the open state of all clients.

## See Also

### Miscellaneous
- [complete](./api-1810767-complete.md)
- [copyPhysicalExtent](./api-1810820-copyphysicalextent.md)
- [handleClose](./api-1810866-handleclose.md)
- [handleOpen](./api-1810948-handleopen.md)
- [lockPhysicalExtents](./api-1810985-lockphysicalextents.md)
- [open](./api-1811013-open.md)
- [read()](./api-1811038-read.md)
- [read()](./api-1811068-read.md)
- [synchronizeCache](./api-1811091-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811117-unlockphysicalextents.md)
- [unmap](./api-1811145-unmap.md)
- [write()](./api-1811168-write.md)
- [write()](./api-1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810905-handleisopen)*