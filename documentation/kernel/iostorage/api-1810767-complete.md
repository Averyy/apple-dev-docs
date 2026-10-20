# complete

**Framework**: Kernel  
**Kind**: instm

## Declaration

```c
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

### Miscellaneous
- [copyPhysicalExtent](./api-1810820-copyphysicalextent.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1810767-complete)*