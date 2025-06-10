# getContentHint

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual const char * getContentHint() const;
```

#### Return_value

Hint of media's contents.

#### Overview

Ask the media object for a hint of its contents. The hint is set at the time of the object's creation, should the creator have a clue as to what it may contain. The hint string does not change for the lifetime of the object and is also formed in the likeness of Apple's "Apple_HFS" strings or in the likeness of a UUID.

## See Also

- [copyPhysicalExtent](iomedia/1813424-copyphysicalextent.md)
- [getAttributes](iomedia/1813444-getattributes.md)
- [getBase](iomedia/1813468-getbase.md)
- [getContent](iomedia/1813495-getcontent.md)
- [getPreferredBlockSize](iomedia/1813553-getpreferredblocksize.md)
- [getSize](iomedia/1813585-getsize.md)
- [handleClose](iomedia/1813614-handleclose.md)
- [handleIsOpen](iomedia/1813630-handleisopen.md)
- [handleOpen](iomedia/1813647-handleopen.md)
- [init](iomedia/1813657-init.md)
- [isEjectable](iomedia/1813664-isejectable.md)
- [isFormatted](iomedia/1813670-isformatted.md)
- [isWhole](iomedia/1813677-iswhole.md)
- [isWritable](iomedia/1813683-iswritable.md)
- [lockPhysicalExtents](iomedia/1813689-lockphysicalextents.md)
- [read](iomedia/1813696-read.md)
- [synchronizeCache](iomedia/1813702-synchronizecache.md)
- [unlockPhysicalExtents](iomedia/1813710-unlockphysicalextents.md)
- [unmap](iomedia/1813719-unmap.md)
- [write](iomedia/1813725-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia/1813522-getcontenthint)*