# lockPhysicalExtents

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual bool lockPhysicalExtents(
 IOService *client);
```

## Return Value

Returns true if the lock was successful, false otherwise.

## Overview

Lock the contents of the storage object against relocation temporarily, for the purpose of getting physical extents.

## Parameters

- `client`: Client requesting the operation.

## See Also

### Miscellaneous
- [complete](./api-1810767-complete.md)
- [copyPhysicalExtent](./api-1810820-copyphysicalextent.md)
- [handleClose](./api-1810866-handleclose.md)
- [handleIsOpen](./api-1810905-handleisopen.md)
- [handleOpen](./api-1810948-handleopen.md)
- [open](./api-1811013-open.md)
- [read()](./api-1811038-read.md)
- [read()](./api-1811068-read.md)
- [synchronizeCache](./api-1811091-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811117-unlockphysicalextents.md)
- [unmap](./api-1811145-unmap.md)
- [write()](./api-1811168-write.md)
- [write()](./api-1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810985-lockphysicalextents)*