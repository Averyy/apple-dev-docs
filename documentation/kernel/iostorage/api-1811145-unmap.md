# unmap

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn unmap(
 IOService *client, 
 IOStorageExtent *extents, 
 UInt32extentsCount, 
 UInt32 options = 0);
```

#### Return_value

Returns the status of the operation.

#### Overview

Delete unused data from the storage object at the specified byte offsets, synchronously.

## Parameters

- `client`: Client requesting the operation.
- `extents`: List of extents. See IOStorageExtent. It is legal for the callee to overwrite the contents of this buffer in order to satisfy the request.
- `extentsCount`: Number of extents.

## See Also

- [complete](iostorage/1810767-complete.md)
- [copyPhysicalExtent](iostorage/1810820-copyphysicalextent.md)
- [handleClose](iostorage/1810866-handleclose.md)
- [handleIsOpen](iostorage/1810905-handleisopen.md)
- [handleOpen](iostorage/1810948-handleopen.md)
- [lockPhysicalExtents](iostorage/1810985-lockphysicalextents.md)
- [open](iostorage/1811013-open.md)
- [read()](iostorage/1811038-read.md)
- [read()](iostorage/1811068-read.md)
- [synchronizeCache](iostorage/1811091-synchronizecache.md)
- [unlockPhysicalExtents](iostorage/1811117-unlockphysicalextents.md)
- [write()](iostorage/1811168-write.md)
- [write()](iostorage/1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1811145-unmap)*