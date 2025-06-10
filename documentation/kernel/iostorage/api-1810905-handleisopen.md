# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual bool handleIsOpen(
 const IOService *client) const = 0;
```

#### Return_value

Returns true if the client was (or clients were) open, false otherwise.

#### Overview

The handleIsOpen method determines whether the specified client, or any client if none is specified, presently has an open on this object.

## Parameters

- `client`: Client to check the open state of. Set to zero to check the open state of all clients.

## See Also

- [complete](iostorage/1810767-complete.md)
- [copyPhysicalExtent](iostorage/1810820-copyphysicalextent.md)
- [handleClose](iostorage/1810866-handleclose.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810905-handleisopen)*