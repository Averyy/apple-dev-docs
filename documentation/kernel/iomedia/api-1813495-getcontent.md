# getContent

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual const char * getContent() const;
```

#### Return_value

Description of media's contents.

#### Overview

Ask the media object for a description of its contents. The description is the same as the hint at the time of the object's creation, but it is possible that the description has been overridden by a client (which has probed the media and identified the content correctly) of the media object. It is more accurate than the hint for this reason. The string is formed in the likeness of Apple's "Apple_HFS" strings or in the likeness of a UUID.

The content description can be overridden by any client that matches onto this media object with a match category of kIOStorageCategory. The media object checks for a kIOMediaContentMaskKey property in the client, and if it finds one, it copies it into kIOMediaContentKey property.

## See Also

- [copyPhysicalExtent](iomedia/1813424-copyphysicalextent.md)
- [getAttributes](iomedia/1813444-getattributes.md)
- [getBase](iomedia/1813468-getbase.md)
- [getContentHint](iomedia/1813522-getcontenthint.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia/1813495-getcontent)*