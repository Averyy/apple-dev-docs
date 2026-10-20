# handleClose

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
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

### Miscellaneous
- [copyPhysicalExtent](./api-1811149-copyphysicalextent.md)
- [handleIsOpen](./api-1811193-handleisopen.md)
- [handleOpen](./api-1811211-handleopen.md)
- [lockPhysicalExtents](./api-1811226-lockphysicalextents.md)
- [read](./api-1811238-read.md)
- [synchronizeCache](./api-1811248-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811258-unlockphysicalextents.md)
- [unmap](./api-1811266-unmap.md)
- [write](./api-1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811170-handleclose)*