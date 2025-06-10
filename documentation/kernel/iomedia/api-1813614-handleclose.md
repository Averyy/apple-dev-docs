# handleClose

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual void handleClose(
 IOService *client,
 IOOptionBitsoptions);
```

#### Overview

The handleClose method closes the client's access to this object.

This implementation replaces the IOService definition of handleClose().

## Parameters

- `client`: Client requesting the close.
- `options`: Options for the close. Set to zero.

## See Also

- [copyPhysicalExtent](iomedia/1813424-copyphysicalextent.md)
- [getAttributes](iomedia/1813444-getattributes.md)
- [getBase](iomedia/1813468-getbase.md)
- [getContent](iomedia/1813495-getcontent.md)
- [getContentHint](iomedia/1813522-getcontenthint.md)
- [getPreferredBlockSize](iomedia/1813553-getpreferredblocksize.md)
- [getSize](iomedia/1813585-getsize.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia/1813614-handleclose)*