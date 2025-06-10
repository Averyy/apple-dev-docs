# lockPhysicalExtents

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual bool lockPhysicalExtents(
 IOService *client);
```

#### Return_value

Returns true if the lock was successful, false otherwise.

#### Overview

Lock the contents of the storage object against relocation temporarily, for the purpose of getting physical extents.

## Parameters

- `client`: Client requesting the operation.

## See Also

- [copyPhysicalExtent](iopartitionscheme/1810278-copyphysicalextent.md)
- [handleClose](iopartitionscheme/1810310-handleclose.md)
- [handleIsOpen](iopartitionscheme/1810337-handleisopen.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [read](iopartitionscheme/1810409-read.md)
- [synchronizeCache](iopartitionscheme/1810446-synchronizecache.md)
- [unlockPhysicalExtents](iopartitionscheme/1810496-unlockphysicalextents.md)
- [unmap](iopartitionscheme/1810548-unmap.md)
- [write](iopartitionscheme/1810601-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme/1810387-lockphysicalextents)*