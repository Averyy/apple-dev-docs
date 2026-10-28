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
- [copyPhysicalExtent](./api-1813424-copyphysicalextent.md)
- [getAttributes](./api-1813444-getattributes.md)
- [getBase](./api-1813468-getbase.md)
- [getContent](./api-1813495-getcontent.md)
- [getContentHint](./api-1813522-getcontenthint.md)
- [getPreferredBlockSize](./api-1813553-getpreferredblocksize.md)
- [getSize](./api-1813585-getsize.md)
- [handleClose](./api-1813614-handleclose.md)
- [handleIsOpen](./api-1813630-handleisopen.md)
- [init](./api-1813657-init.md)
- [isEjectable](./api-1813664-isejectable.md)
- [isFormatted](./api-1813670-isformatted.md)
- [isWhole](./api-1813677-iswhole.md)
- [isWritable](./api-1813683-iswritable.md)
- [lockPhysicalExtents](./api-1813689-lockphysicalextents.md)
- [read](./api-1813696-read.md)
- [synchronizeCache](./api-1813702-synchronizecache.md)
- [unlockPhysicalExtents](./api-1813710-unlockphysicalextents.md)
- [unmap](./api-1813719-unmap.md)
- [write](./api-1813725-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia/1813647-handleopen)*