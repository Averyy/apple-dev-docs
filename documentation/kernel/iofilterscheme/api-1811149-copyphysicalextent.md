# copyPhysicalExtent

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOStorage * copyPhysicalExtent(
 IOService *client, 
 UInt64 *byteStart, 
 UInt64 *byteCount);
```

#### Return_value

A reference to the physical storage object, which should be released by the caller, or a null on error.

#### Overview

Convert the specified byte offset into a physical byte offset, relative to a physical storage object. This call should only be made within the context of lockPhysicalExtents().

## Parameters

- `client`: Client requesting the operation.
- `byteStart`: Starting byte offset for the operation. Returns a physical byte offset, relative to the physical storage object, on success.
- `byteCount`: Size of the operation. Returns the actual number of bytes which can be transferred, relative to the physical storage object, on success.

## See Also

- [handleClose](iofilterscheme/1811170-handleclose.md)
- [handleIsOpen](iofilterscheme/1811193-handleisopen.md)
- [handleOpen](iofilterscheme/1811211-handleopen.md)
- [lockPhysicalExtents](iofilterscheme/1811226-lockphysicalextents.md)
- [read](iofilterscheme/1811238-read.md)
- [synchronizeCache](iofilterscheme/1811248-synchronizecache.md)
- [unlockPhysicalExtents](iofilterscheme/1811258-unlockphysicalextents.md)
- [unmap](iofilterscheme/1811266-unmap.md)
- [write](iofilterscheme/1811274-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1811149-copyphysicalextent)*