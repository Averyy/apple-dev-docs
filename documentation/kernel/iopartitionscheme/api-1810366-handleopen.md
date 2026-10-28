# handleOpen

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual bool handleOpen(
 IOService *client, 
 IOOptionBitsoptions, 
 void *access);
```

## Return Value

Returns true if the open was successful, false otherwise.

## Overview

The handleOpen method grants or denies permission to access this object to an interested client. The argument is an IOStorageAccess value that specifies the level of access desired -- reader or reader-writer.

This method can be invoked to upgrade or downgrade the access level for an existing client as well. The previous access level will prevail for upgrades that fail, of course. A downgrade should never fail. If the new access level should be the same as the old for a given client, this method will do nothing and return success. In all cases, one, singular close-per-client is expected for all opens-per-client received.

This implementation replaces the IOService definition of handleOpen().

## Parameters

- `client`: Client requesting the open.
- `options`: Options for the open. Set to zero.
- `access`: Access level for the open. Set to kIOStorageAccessReader or kIOStorageAccessReaderWriter.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1810278-copyphysicalextent.md)
- [handleClose](./api-1810310-handleclose.md)
- [handleIsOpen](./api-1810337-handleisopen.md)
- [lockPhysicalExtents](./api-1810387-lockphysicalextents.md)
- [read](./api-1810409-read.md)
- [synchronizeCache](./api-1810446-synchronizecache.md)
- [unlockPhysicalExtents](./api-1810496-unlockphysicalextents.md)
- [unmap](./api-1810548-unmap.md)
- [write](./api-1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810366-handleopen)*