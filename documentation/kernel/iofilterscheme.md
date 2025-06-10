# IOFilterScheme

**Framework**: Kernel  
**Kind**: cl

The common base class for all filter scheme objects.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOFilterScheme : IOStorage
```

#### Overview

The IOFilterScheme class is the common base class for all filter scheme objects. It extends the IOStorage class by implementing the appropriate open and close semantics for filter objects (standard semantics are act as a relay for incoming opens, producing one outgoing open for each incoming open). It also implements the default read and write semantics, which pass all reads and writes through to the provider media unprocessed. For simple schemes, the default behavior is sufficient. More complex filter schemes such as RAID will want to do extra processing for reads and writes.

## Topics

### Miscellaneous
- [copyPhysicalExtent](iofilterscheme/1811149-copyphysicalextent.md)
- [handleClose](iofilterscheme/1811170-handleclose.md)
- [handleIsOpen](iofilterscheme/1811193-handleisopen.md)
- [handleOpen](iofilterscheme/1811211-handleopen.md)
- [lockPhysicalExtents](iofilterscheme/1811226-lockphysicalextents.md)
- [read](iofilterscheme/1811238-read.md)
- [synchronizeCache](iofilterscheme/1811248-synchronizecache.md)
- [unlockPhysicalExtents](iofilterscheme/1811258-unlockphysicalextents.md)
- [unmap](iofilterscheme/1811266-unmap.md)
- [write](iofilterscheme/1811274-write.md)
### Instance Methods
- [- copyPhysicalExtent](iofilterscheme/1564815-copyphysicalextent.md)
- [- getMetaClass](iofilterscheme/1564802-getmetaclass.md)
- [- getProvider](iofilterscheme/1564810-getprovider.md)
- [- getProvisionStatus](iofilterscheme/1642770-getprovisionstatus.md)
- [- handleClose](iofilterscheme/1564803-handleclose.md)
- [- handleIsOpen](iofilterscheme/1564804-handleisopen.md)
- [- handleOpen](iofilterscheme/1564806-handleopen.md)
- [- lockPhysicalExtents](iofilterscheme/1564801-lockphysicalextents.md)
- [- read](iofilterscheme/1564808-read.md)
- [- setPriority](iofilterscheme/1564814-setpriority.md)
- [- synchronize](iofilterscheme/1564809-synchronize.md)
- [- unlockPhysicalExtents](iofilterscheme/1564811-unlockphysicalextents.md)
- [- unmap](iofilterscheme/1564812-unmap.md)
- [- write](iofilterscheme/1564807-write.md)

## Relationships

### Inherits From
- [IOStorage](iostorage.md)

## See Also

- [IOAppleLabelScheme](ioapplelabelscheme.md)
- [IOApplePartitionScheme](ioapplepartitionscheme.md)
- [IOFDiskPartitionScheme](iofdiskpartitionscheme.md)
- [IOGUIDPartitionScheme](ioguidpartitionscheme.md)
- [IOPartitionScheme](iopartitionscheme.md)
  The common base class for all partition scheme objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme)*