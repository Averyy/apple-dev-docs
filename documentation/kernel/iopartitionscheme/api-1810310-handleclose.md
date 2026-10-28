# handleClose

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual void handleClose(
 IOService *client,
 IOOptionBitsoptions);
```

## Overview

The handleClose method closes the client's access to this object.

This implementation replaces the IOService definition of handleClose().

## Parameters

- `client`: Client requesting the close.
- `options`: Options for the close. Set to zero.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1810278-copyphysicalextent.md)
- [handleIsOpen](./api-1810337-handleisopen.md)
- [handleOpen](./api-1810366-handleopen.md)
- [lockPhysicalExtents](./api-1810387-lockphysicalextents.md)
- [read](./api-1810409-read.md)
- [synchronizeCache](./api-1810446-synchronizecache.md)
- [unlockPhysicalExtents](./api-1810496-unlockphysicalextents.md)
- [unmap](./api-1810548-unmap.md)
- [write](./api-1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810310-handleclose)*