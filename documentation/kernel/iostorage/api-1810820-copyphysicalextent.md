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

- [complete](iostorage/1810767-complete.md)
- [handleClose](iostorage/1810866-handleclose.md)
- [handleIsOpen](iostorage/1810905-handleisopen.md)
- [handleOpen](iostorage/1810948-handleopen.md)
- [lockPhysicalExtents](iostorage/1810985-lockphysicalextents.md)
- [open](iostorage/1811013-open.md)
- [read()](iostorage/1811038-read.md)
- [read()](iostorage/1811068-read.md)
- [synchronizeCache](iostorage/1811091-synchronizecache.md)
- [unlockPhysicalExtents](iostorage/1811117-unlockphysicalextents.md)
- [unmap](iostorage/1811145-unmap.md)
- [write()](iostorage/1811168-write.md)
- [write()](iostorage/1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810820-copyphysicalextent)*