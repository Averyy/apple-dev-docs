# lockPhysicalExtents

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual bool lockPhysicalExtents(
 IOService *client);
```

#### Return_value

Returns true if the lock was successful, false otherwise.

#### Overview

Lock the contents of the storage object against relocation temporarily, for the purpose of getting physical extents.

## Parameters

- `client`: Client requesting the operation.

## See Also

- [complete](iostorage/1810767-complete.md)
- [copyPhysicalExtent](iostorage/1810820-copyphysicalextent.md)
- [handleClose](iostorage/1810866-handleclose.md)
- [handleIsOpen](iostorage/1810905-handleisopen.md)
- [handleOpen](iostorage/1810948-handleopen.md)
- [open](iostorage/1811013-open.md)
- [read()](iostorage/1811038-read.md)
- [read()](iostorage/1811068-read.md)
- [synchronizeCache](iostorage/1811091-synchronizecache.md)
- [unlockPhysicalExtents](iostorage/1811117-unlockphysicalextents.md)
- [unmap](iostorage/1811145-unmap.md)
- [write()](iostorage/1811168-write.md)
- [write()](iostorage/1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810985-lockphysicalextents)*