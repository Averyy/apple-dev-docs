# unlockPhysicalExtents

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual void unlockPhysicalExtents(
 IOService *client);
```

#### Overview

Unlock the contents of the storage object for relocation again. This call must balance a successful call to lockPhysicalExtents().

## Parameters

- `client`: Client requesting the operation.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1811149-copyphysicalextent.md)
- [handleClose](./api-1811170-handleclose.md)
- [handleIsOpen](./api-1811193-handleisopen.md)
- [handleOpen](./api-1811211-handleopen.md)
- [lockPhysicalExtents](./api-1811226-lockphysicalextents.md)
- [read](./api-1811238-read.md)
- [synchronizeCache](./api-1811248-synchronizecache.md)
- [unmap](./api-1811266-unmap.md)
- [write](./api-1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811258-unlockphysicalextents)*