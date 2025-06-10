# complete

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
static void complete(
 IOStorageCompletion *completion, 
 IOReturn status, 
 UInt64 actualByteCount = 0);
```

#### Overview

Invokes the specified completion action of the read/write request. If the completion action is unspecified, no action is taken. This method serves simply as a convenience to storage subclass developers.

## Parameters

- `completion`: Completion information for the data transfer.
- `status`: Status of the data transfer.
- `actualByteCount`: Actual number of bytes transferred in the data transfer.

## See Also

- [copyPhysicalExtent](iostorage/1810820-copyphysicalextent.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810767-complete)*