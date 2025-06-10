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

- [copyPhysicalExtent](iofilterscheme/1811149-copyphysicalextent.md)
- [handleClose](iofilterscheme/1811170-handleclose.md)
- [handleOpen](iofilterscheme/1811211-handleopen.md)
- [lockPhysicalExtents](iofilterscheme/1811226-lockphysicalextents.md)
- [read](iofilterscheme/1811238-read.md)
- [synchronizeCache](iofilterscheme/1811248-synchronizecache.md)
- [unlockPhysicalExtents](iofilterscheme/1811258-unlockphysicalextents.md)
- [unmap](iofilterscheme/1811266-unmap.md)
- [write](iofilterscheme/1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811193-handleisopen)*