# unlockPhysicalExtents

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual void unlockPhysicalExtents(
 IOService *client);
```

#### Overview

Unlock the contents of the storage object for relocation again. This call must balance a successful call to lockPhysicalExtents().

## Parameters

- `client`: Client requesting the operation.

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
- [handleOpen](./api-1813647-handleopen.md)
- [init](./api-1813657-init.md)
- [isEjectable](./api-1813664-isejectable.md)
- [isFormatted](./api-1813670-isformatted.md)
- [isWhole](./api-1813677-iswhole.md)
- [isWritable](./api-1813683-iswritable.md)
- [lockPhysicalExtents](./api-1813689-lockphysicalextents.md)
- [read](./api-1813696-read.md)
- [synchronizeCache](./api-1813702-synchronizecache.md)
- [unmap](./api-1813719-unmap.md)
- [write](./api-1813725-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia/1813710-unlockphysicalextents)*