# IOFilterScheme

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The common base class for all filter scheme objects.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOFilterScheme : IOStorage
```

#### Overview

The IOFilterScheme class is the common base class for all filter scheme objects. It extends the IOStorage class by implementing the appropriate open and close semantics for filter objects (standard semantics are act as a relay for incoming opens, producing one outgoing open for each incoming open). It also implements the default read and write semantics, which pass all reads and writes through to the provider media unprocessed. For simple schemes, the default behavior is sufficient. More complex filter schemes such as RAID will want to do extra processing for reads and writes.

## Topics

### Miscellaneous
- [copyPhysicalExtent](./iofilterscheme/api-1811149-copyphysicalextent.md)
- [handleClose](./iofilterscheme/api-1811170-handleclose.md)
- [handleIsOpen](./iofilterscheme/api-1811193-handleisopen.md)
- [handleOpen](./iofilterscheme/api-1811211-handleopen.md)
- [lockPhysicalExtents](./iofilterscheme/api-1811226-lockphysicalextents.md)
- [read](./iofilterscheme/api-1811238-read.md)
- [synchronizeCache](./iofilterscheme/api-1811248-synchronizecache.md)
- [unlockPhysicalExtents](./iofilterscheme/api-1811258-unlockphysicalextents.md)
- [unmap](./iofilterscheme/api-1811266-unmap.md)
- [write](./iofilterscheme/api-1811274-write.md)
### Instance Methods
- [- copyPhysicalExtent](./iofilterscheme/api-1564815-copyphysicalextent.md)
- [- getMetaClass](./iofilterscheme/api-1564802-getmetaclass.md)
- [- getProvider](./iofilterscheme/api-1564810-getprovider.md)
- [- getProvisionStatus](./iofilterscheme/api-1642770-getprovisionstatus.md)
- [- handleClose](./iofilterscheme/api-1564803-handleclose.md)
- [- handleIsOpen](./iofilterscheme/api-1564804-handleisopen.md)
- [- handleOpen](./iofilterscheme/api-1564806-handleopen.md)
- [- lockPhysicalExtents](./iofilterscheme/api-1564801-lockphysicalextents.md)
- [- read](./iofilterscheme/api-1564808-read.md)
- [- setPriority](./iofilterscheme/api-1564814-setpriority.md)
- [- synchronize](./iofilterscheme/api-1564809-synchronize.md)
- [- unlockPhysicalExtents](./iofilterscheme/api-1564811-unlockphysicalextents.md)
- [- unmap](./iofilterscheme/api-1564812-unmap.md)
- [- write](./iofilterscheme/api-1564807-write.md)

## Relationships

### Inherits From
- [IOStorage](./iostorage.md)

## See Also

### Schemes
- [IOAppleLabelScheme](./ioapplelabelscheme.md)
- [IOApplePartitionScheme](./ioapplepartitionscheme.md)
- [IOFDiskPartitionScheme](./iofdiskpartitionscheme.md)
- [IOGUIDPartitionScheme](./ioguidpartitionscheme.md)
- [IOPartitionScheme](./iopartitionscheme.md)
  The common base class for all partition scheme objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme)*