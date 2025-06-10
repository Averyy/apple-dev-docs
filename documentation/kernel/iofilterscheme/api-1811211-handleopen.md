# handleOpen

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual bool handleOpen(
 IOService *client, 
 IOOptionBitsoptions, 
 void *access);
```

#### Return_value

Returns true if the open was successful, false otherwise.

#### Overview

The handleOpen method grants or denies permission to access this object to an interested client. The argument is an IOStorageAccess value that specifies the level of access desired -- reader or reader-writer.

This method can be invoked to upgrade or downgrade the access level for an existing client as well. The previous access level will prevail for upgrades that fail, of course. A downgrade should never fail. If the new access level should be the same as the old for a given client, this method will do nothing and return success. In all cases, one, singular close-per-client is expected for all opens-per-client received.

This implementation replaces the IOService definition of handleOpen().

## Parameters

- `client`: Client requesting the open.
- `options`: Options for the open. Set to zero.
- `access`: Access level for the open. Set to kIOStorageAccessReader or kIOStorageAccessReaderWriter.

## See Also

- [copyPhysicalExtent](iofilterscheme/1811149-copyphysicalextent.md)
- [handleClose](iofilterscheme/1811170-handleclose.md)
- [handleIsOpen](iofilterscheme/1811193-handleisopen.md)
- [lockPhysicalExtents](iofilterscheme/1811226-lockphysicalextents.md)
- [read](iofilterscheme/1811238-read.md)
- [synchronizeCache](iofilterscheme/1811248-synchronizecache.md)
- [unlockPhysicalExtents](iofilterscheme/1811258-unlockphysicalextents.md)
- [unmap](iofilterscheme/1811266-unmap.md)
- [write](iofilterscheme/1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811211-handleopen)*