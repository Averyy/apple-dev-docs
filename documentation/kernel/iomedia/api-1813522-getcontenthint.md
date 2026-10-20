# getContentHint

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual const char * getContentHint() const;
```

#### Return Value

Hint of media's contents.

#### Overview

Ask the media object for a hint of its contents. The hint is set at the time of the object's creation, should the creator have a clue as to what it may contain. The hint string does not change for the lifetime of the object and is also formed in the likeness of Apple's "Apple_HFS" strings or in the likeness of a UUID.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1813424-copyphysicalextent.md)
- [getAttributes](./api-1813444-getattributes.md)
- [getBase](./api-1813468-getbase.md)
- [getContent](./api-1813495-getcontent.md)
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
- [unlockPhysicalExtents](./api-1813710-unlockphysicalextents.md)
- [unmap](./api-1813719-unmap.md)
- [write](./api-1813725-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia/1813522-getcontenthint)*