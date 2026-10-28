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
- [copyPhysicalExtent](./api-1810278-copyphysicalextent.md)
- [handleClose](./api-1810310-handleclose.md)
- [handleIsOpen](./api-1810337-handleisopen.md)
- [handleOpen](./api-1810366-handleopen.md)
- [read](./api-1810409-read.md)
- [synchronizeCache](./api-1810446-synchronizecache.md)
- [unlockPhysicalExtents](./api-1810496-unlockphysicalextents.md)
- [unmap](./api-1810548-unmap.md)
- [write](./api-1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810387-lockphysicalextents)*