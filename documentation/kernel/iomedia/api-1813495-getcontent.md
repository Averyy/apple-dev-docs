# getContent

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual const char * getContent() const;
```

## Return Value

Description of media's contents.

## Overview

Ask the media object for a description of its contents. The description is the same as the hint at the time of the object's creation, but it is possible that the description has been overridden by a client (which has probed the media and identified the content correctly) of the media object. It is more accurate than the hint for this reason. The string is formed in the likeness of Apple's "Apple_HFS" strings or in the likeness of a UUID.

The content description can be overridden by any client that matches onto this media object with a match category of kIOStorageCategory. The media object checks for a kIOMediaContentMaskKey property in the client, and if it finds one, it copies it into kIOMediaContentKey property.

## See Also

### Miscellaneous
- [copyPhysicalExtent](./api-1813424-copyphysicalextent.md)
- [getAttributes](./api-1813444-getattributes.md)
- [getBase](./api-1813468-getbase.md)
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
- [unlockPhysicalExtents](./api-1813710-unlockphysicalextents.md)
- [unmap](./api-1813719-unmap.md)
- [write](./api-1813725-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia/1813495-getcontent)*