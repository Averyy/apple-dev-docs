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

#### Return Value

Returns the status of the operation.

#### Overview

Delete unused data from the storage object at the specified byte offsets, synchronously.

## Parameters

- `client`: Client requesting the operation.
- `extents`: List of extents. See IOStorageExtent. It is legal for the callee to overwrite the contents of this buffer in order to satisfy the request.
- `extentsCount`: Number of extents.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1811149-copyphysicalextent.md)
- [handleClose](./api-1811170-handleclose.md)
- [handleIsOpen](./api-1811193-handleisopen.md)
- [handleOpen](./api-1811211-handleopen.md)
- [lockPhysicalExtents](./api-1811226-lockphysicalextents.md)
- [read](./api-1811238-read.md)
- [synchronizeCache](./api-1811248-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811258-unlockphysicalextents.md)
- [write](./api-1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811266-unmap)*