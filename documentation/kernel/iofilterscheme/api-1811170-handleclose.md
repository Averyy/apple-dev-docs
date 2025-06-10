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

- [copyPhysicalExtent](iofilterscheme/1811149-copyphysicalextent.md)
- [handleIsOpen](iofilterscheme/1811193-handleisopen.md)
- [handleOpen](iofilterscheme/1811211-handleopen.md)
- [lockPhysicalExtents](iofilterscheme/1811226-lockphysicalextents.md)
- [read](iofilterscheme/1811238-read.md)
- [synchronizeCache](iofilterscheme/1811248-synchronizecache.md)
- [unlockPhysicalExtents](iofilterscheme/1811258-unlockphysicalextents.md)
- [unmap](iofilterscheme/1811266-unmap.md)
- [write](iofilterscheme/1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811170-handleclose)*