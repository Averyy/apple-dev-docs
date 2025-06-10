# IOPartitionScheme

**Framework**: Kernel  
**Kind**: cl

The common base class for all partition scheme objects.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOPartitionScheme : IOStorage
```

#### Overview

The IOPartitionScheme class is the common base class for all partition scheme objects. It extends the IOStorage class by implementing the appropriate open and close semantics for partition objects (standard semantics are to act as a multiplexor for incoming opens, producing one outgoing open with the correct access). It also implements the default read and write semantics, which pass all reads and writes through to the provider media unprocessed. For simple schemes, the default behavior is sufficient. More complex partition schemes such as RAID will want to do extra processing for reads and writes.

## Topics

### Miscellaneous
- [copyPhysicalExtent](iopartitionscheme/1810278-copyphysicalextent.md)
- [handleClose](iopartitionscheme/1810310-handleclose.md)
- [handleIsOpen](iopartitionscheme/1810337-handleisopen.md)
- [handleOpen](iopartitionscheme/1810366-handleopen.md)
- [lockPhysicalExtents](iopartitionscheme/1810387-lockphysicalextents.md)
- [read](iopartitionscheme/1810409-read.md)
- [synchronizeCache](iopartitionscheme/1810446-synchronizecache.md)
- [unlockPhysicalExtents](iopartitionscheme/1810496-unlockphysicalextents.md)
- [unmap](iopartitionscheme/1810548-unmap.md)
- [write](iopartitionscheme/1810601-write.md)
### Instance Methods
- [- attachMediaObjectToDeviceTree](iopartitionscheme/1590598-attachmediaobjecttodevicetree.md)
- [- copyPhysicalExtent](iopartitionscheme/1590601-copyphysicalextent.md)
- [- detachMediaObjectFromDeviceTree](iopartitionscheme/1590587-detachmediaobjectfromdevicetree.md)
- [- free](iopartitionscheme/1590595-free.md)
- [- getMetaClass](iopartitionscheme/1590597-getmetaclass.md)
- [- getProvider](iopartitionscheme/1590584-getprovider.md)
- [- getProvisionStatus](iopartitionscheme/1638730-getprovisionstatus.md)
- [- handleClose](iopartitionscheme/1590600-handleclose.md)
- [- handleIsOpen](iopartitionscheme/1590588-handleisopen.md)
- [- handleOpen](iopartitionscheme/1590590-handleopen.md)
- [- init](iopartitionscheme/1590579-init.md)
- [- juxtaposeMediaObjects](iopartitionscheme/1590594-juxtaposemediaobjects.md)
- [- lockPhysicalExtents](iopartitionscheme/1590593-lockphysicalextents.md)
- [- read](iopartitionscheme/1590581-read.md)
- [- setPriority](iopartitionscheme/1590591-setpriority.md)
- [- synchronize](iopartitionscheme/1590585-synchronize.md)
- [- unlockPhysicalExtents](iopartitionscheme/1590596-unlockphysicalextents.md)
- [- unmap](iopartitionscheme/1590589-unmap.md)
- [- write](iopartitionscheme/1590583-write.md)

## Relationships

### Inherits From
- [IOStorage](iostorage.md)

## See Also

- [IOAppleLabelScheme](ioapplelabelscheme.md)
- [IOApplePartitionScheme](ioapplepartitionscheme.md)
- [IOFDiskPartitionScheme](iofdiskpartitionscheme.md)
- [IOGUIDPartitionScheme](ioguidpartitionscheme.md)
- [IOFilterScheme](iofilterscheme.md)
  The common base class for all filter scheme objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopartitionscheme)*