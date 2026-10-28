# IOMedia

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

A random-access disk device abstraction.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOMedia : IOStorage
```

## Overview

The IOMedia class is a random-access disk device abstraction. It provides a consistent interface for both real and virtual disk devices, for subdivisions of disks such as partitions, for supersets of disks such as RAID volumes, and so on. It extends the IOStorage class by implementing the appropriate open, close, read, write, and matching semantics for media objects. The properties it has reflect the properties of real disk devices, such as ejectability and writability.

The read and write interfaces support byte-level access to the storage space, with the appropriate deblocking handled by the block storage driver, however, a typical client will want to get the natural block size in order to optimize access to the real disk device. A read or write is accepted so long as the client's access is valid, the media is formatted and the transfer is within the bounds of the media. An optional non-zero base (offset) is then applied before the read or write is passed to provider object.

## Topics

### Miscellaneous
- [copyPhysicalExtent](./iomedia/api-1813424-copyphysicalextent.md)
- [getAttributes](./iomedia/api-1813444-getattributes.md)
- [getBase](./iomedia/api-1813468-getbase.md)
- [getContent](./iomedia/api-1813495-getcontent.md)
- [getContentHint](./iomedia/api-1813522-getcontenthint.md)
- [getPreferredBlockSize](./iomedia/api-1813553-getpreferredblocksize.md)
- [getSize](./iomedia/api-1813585-getsize.md)
- [handleClose](./iomedia/api-1813614-handleclose.md)
- [handleIsOpen](./iomedia/api-1813630-handleisopen.md)
- [handleOpen](./iomedia/api-1813647-handleopen.md)
- [init](./iomedia/api-1813657-init.md)
- [isEjectable](./iomedia/api-1813664-isejectable.md)
- [isFormatted](./iomedia/api-1813670-isformatted.md)
- [isWhole](./iomedia/api-1813677-iswhole.md)
- [isWritable](./iomedia/api-1813683-iswritable.md)
- [lockPhysicalExtents](./iomedia/api-1813689-lockphysicalextents.md)
- [read](./iomedia/api-1813696-read.md)
- [synchronizeCache](./iomedia/api-1813702-synchronizecache.md)
- [unlockPhysicalExtents](./iomedia/api-1813710-unlockphysicalextents.md)
- [unmap](./iomedia/api-1813719-unmap.md)
- [write](./iomedia/api-1813725-write.md)
### Instance Methods
- [- attachToChild](./iomedia/api-1420235-attachtochild.md)
- [- copyPhysicalExtent](./iomedia/api-1420300-copyphysicalextent.md)
- [- detachFromChild](./iomedia/api-1420322-detachfromchild.md)
- [- free](./iomedia/api-1420316-free.md)
- [- getAttributes](./iomedia/api-1420270-getattributes.md)
- [- getBase](./iomedia/api-1420251-getbase.md)
- [- getContent](./iomedia/api-1420330-getcontent.md)
- [- getContentHint](./iomedia/api-1420318-getcontenthint.md)
- [- getMetaClass](./iomedia/api-1420314-getmetaclass.md)
- [- getPreferredBlockSize](./iomedia/api-1420311-getpreferredblocksize.md)
- [- getProvider](./iomedia/api-1420258-getprovider.md)
- [- getProvisionStatus](./iomedia/api-1644058-getprovisionstatus.md)
- [- getSize](./iomedia/api-1420239-getsize.md)
- [- handleClose](./iomedia/api-1420298-handleclose.md)
- [- handleIsOpen](./iomedia/api-1420285-handleisopen.md)
- [- handleOpen](./iomedia/api-1420304-handleopen.md)
- [- init](./iomedia/api-1420306-init.md)
- [- isEjectable](./iomedia/api-1420264-isejectable.md)
- [- isFormatted](./iomedia/api-1420283-isformatted.md)
- [- isWhole](./iomedia/api-1420290-iswhole.md)
- [- isWritable](./iomedia/api-1420292-iswritable.md)
- [- lockPhysicalExtents](./iomedia/api-1420248-lockphysicalextents.md)
- [- matchPropertyTable](./iomedia/api-1420288-matchpropertytable.md)
- [- read](./iomedia/api-1420242-read.md)
- [- setPriority](./iomedia/api-1420328-setpriority.md)
- [- synchronize](./iomedia/api-1420266-synchronize.md)
- [- unlockPhysicalExtents](./iomedia/api-1420302-unlockphysicalextents.md)
- [- unmap](./iomedia/api-1420272-unmap.md)
- [- write](./iomedia/api-1420277-write.md)

## Relationships

### Inherits From
- [IOStorage](./iostorage.md)

## See Also

### Data Storage
- [IOCDMedia](./iocdmedia.md)
  The IOCDMedia class is a random-access disk device abstraction for CDs.
- [IOBDMedia](./iobdmedia.md)
  The IOBDMedia class is a random-access disk device abstraction for BDs.
- [IOCDMediaBSDClient](./iocdmediabsdclient.md)
- [IOCDPartitionScheme](./iocdpartitionscheme.md)
- [IODVDMedia](./iodvdmedia.md)
  The IODVDMedia class is a random-access disk device abstraction for DVDs.
- [IODVDMediaBSDClient](./iodvdmediabsdclient.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomedia)*