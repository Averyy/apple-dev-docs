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
- [copyPhysicalExtent](./api-1810278-copyphysicalextent.md)
- [handleClose](./api-1810310-handleclose.md)
- [handleIsOpen](./api-1810337-handleisopen.md)
- [handleOpen](./api-1810366-handleopen.md)
- [lockPhysicalExtents](./api-1810387-lockphysicalextents.md)
- [read](./api-1810409-read.md)
- [unlockPhysicalExtents](./api-1810496-unlockphysicalextents.md)
- [unmap](./api-1810548-unmap.md)
- [write](./api-1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810446-synchronizecache)*