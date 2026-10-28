# synchronizeCache

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn synchronizeCache(
 IOService *client) = 0;
```

## Return Value

Returns the status of the cache synchronization.

## Overview

Flush the cached data in the storage object, if any, synchronously.

## Parameters

- `client`: Client requesting the cache synchronization.

## See Also

### Miscellaneous
- [complete](./api-1810767-complete.md)
- [copyPhysicalExtent](./api-1810820-copyphysicalextent.md)
- [handleClose](./api-1810866-handleclose.md)
- [handleIsOpen](./api-1810905-handleisopen.md)
- [handleOpen](./api-1810948-handleopen.md)
- [lockPhysicalExtents](./api-1810985-lockphysicalextents.md)
- [open](./api-1811013-open.md)
- [read()](./api-1811038-read.md)
- [read()](./api-1811068-read.md)
- [unlockPhysicalExtents](./api-1811117-unlockphysicalextents.md)
- [unmap](./api-1811145-unmap.md)
- [write()](./api-1811168-write.md)
- [write()](./api-1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1811091-synchronizecache)*