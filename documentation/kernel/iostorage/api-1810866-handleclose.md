# handleClose

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual void handleClose(
 IOService *client,
 IOOptionBitsoptions) = 0;
```

#### Overview

The handleClose method closes the client's access to this object.

## Parameters

- `client`: Client requesting the close.
- `options`: Options for the close. Set to zero.

## See Also

- [complete](iostorage/1810767-complete.md)
- [copyPhysicalExtent](iostorage/1810820-copyphysicalextent.md)
- [handleIsOpen](iostorage/1810905-handleisopen.md)
- [handleOpen](iostorage/1810948-handleopen.md)
- [lockPhysicalExtents](iostorage/1810985-lockphysicalextents.md)
- [open](iostorage/1811013-open.md)
- [read()](iostorage/1811038-read.md)
- [read()](iostorage/1811068-read.md)
- [synchronizeCache](iostorage/1811091-synchronizecache.md)
- [unlockPhysicalExtents](iostorage/1811117-unlockphysicalextents.md)
- [unmap](iostorage/1811145-unmap.md)
- [write()](iostorage/1811168-write.md)
- [write()](iostorage/1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810866-handleclose)*