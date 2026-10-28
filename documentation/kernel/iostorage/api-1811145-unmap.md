# unmap

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn unmap(
 IOService *client, 
 IOStorageExtent *extents, 
 UInt32extentsCount, 
 UInt32 options = 0);
```

## Return Value

Returns the status of the operation.

## Overview

Delete unused data from the storage object at the specified byte offsets, synchronously.

## Parameters

- `client`: Client requesting the operation.
- `extents`: List of extents. See IOStorageExtent. It is legal for the callee to overwrite the contents of this buffer in order to satisfy the request.
- `extentsCount`: Number of extents.

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
- [synchronizeCache](./api-1811091-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811117-unlockphysicalextents.md)
- [write()](./api-1811168-write.md)
- [write()](./api-1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1811145-unmap)*