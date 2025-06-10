# synchronizeCache

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn synchronizeCache(
 IOService *client);
```

#### Return_value

Returns the status of the cache synchronization.

#### Overview

Flush the cached data in the storage object, if any, synchronously.

## Parameters

- `client`: Client requesting the cache synchronization.

## See Also

- [copyPhysicalExtent](iofilterscheme/1811149-copyphysicalextent.md)
- [handleClose](iofilterscheme/1811170-handleclose.md)
- [handleIsOpen](iofilterscheme/1811193-handleisopen.md)
- [handleOpen](iofilterscheme/1811211-handleopen.md)
- [lockPhysicalExtents](iofilterscheme/1811226-lockphysicalextents.md)
- [read](iofilterscheme/1811238-read.md)
- [unlockPhysicalExtents](iofilterscheme/1811258-unlockphysicalextents.md)
- [unmap](iofilterscheme/1811266-unmap.md)
- [write](iofilterscheme/1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811248-synchronizecache)*