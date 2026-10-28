# copyPhysicalExtent

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOStorage * copyPhysicalExtent(
 IOService *client, 
 UInt64 *byteStart, 
 UInt64 *byteCount);
```

## Return Value

A reference to the physical storage object, which should be released by the caller, or a null on error.

## Overview

Convert the specified byte offset into a physical byte offset, relative to a physical storage object. This call should only be made within the context of lockPhysicalExtents().

## Parameters

- `client`: Client requesting the operation.
- `byteStart`: Starting byte offset for the operation. Returns a physical byte offset, relative to the physical storage object, on success.
- `byteCount`: Size of the operation. Returns the actual number of bytes which can be transferred, relative to the physical storage object, on success.

## See Also

### Miscellaneous
- [complete](./api-1810767-complete.md)
- [handleClose](./api-1810866-handleclose.md)
- [handleIsOpen](./api-1810905-handleisopen.md)
- [handleOpen](./api-1810948-handleopen.md)
- [lockPhysicalExtents](./api-1810985-lockphysicalextents.md)
- [open](./api-1811013-open.md)
- [read()](./api-1811038-read.md)
- [read()](./api-1811068-read.md)
- [synchronizeCache](./api-1811091-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811117-unlockphysicalextents.md)
- [unmap](./api-1811145-unmap.md)
- [write()](./api-1811168-write.md)
- [write()](./api-1811185-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810820-copyphysicalextent)*