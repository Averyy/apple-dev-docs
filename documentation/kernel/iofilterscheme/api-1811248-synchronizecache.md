# synchronizeCache

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn synchronizeCache(
 IOService *client);
```

## Return Value

Returns the status of the cache synchronization.

## Overview

Flush the cached data in the storage object, if any, synchronously.

## Parameters

- `client`: Client requesting the cache synchronization.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1811149-copyphysicalextent.md)
- [handleClose](./api-1811170-handleclose.md)
- [handleIsOpen](./api-1811193-handleisopen.md)
- [handleOpen](./api-1811211-handleopen.md)
- [lockPhysicalExtents](./api-1811226-lockphysicalextents.md)
- [read](./api-1811238-read.md)
- [unlockPhysicalExtents](./api-1811258-unlockphysicalextents.md)
- [unmap](./api-1811266-unmap.md)
- [write](./api-1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811248-synchronizecache)*