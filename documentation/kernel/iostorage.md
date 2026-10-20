# IOStorage

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The common base class for mass storage objects.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOStorage : IOService
```

#### Overview

The IOStorage class is the common base class for mass storage objects. It is an abstract class that defines the open/close/read/write APIs that need to be implemented in a given subclass. Synchronous versions of the read/write APIs are provided here -- they are coded in such a way as to wrap the asynchronous versions implemented in the subclass.

## Topics

### Miscellaneous
- [complete](./iostorage/api-1810767-complete.md)
- [copyPhysicalExtent](./iostorage/api-1810820-copyphysicalextent.md)
- [handleClose](./iostorage/api-1810866-handleclose.md)
- [handleIsOpen](./iostorage/api-1810905-handleisopen.md)
- [handleOpen](./iostorage/api-1810948-handleopen.md)
- [lockPhysicalExtents](./iostorage/api-1810985-lockphysicalextents.md)
- [open](./iostorage/api-1811013-open.md)
- [read()](./iostorage/api-1811038-read.md)
- [read()](./iostorage/api-1811068-read.md)
- [synchronizeCache](./iostorage/api-1811091-synchronizecache.md)
- [unlockPhysicalExtents](./iostorage/api-1811117-unlockphysicalextents.md)
- [unmap](./iostorage/api-1811145-unmap.md)
- [write()](./iostorage/api-1811168-write.md)
- [write()](./iostorage/api-1811185-write.md)
### Instance Methods
- [- attach](./iostorage/api-1574956-attach.md)
- [- copyPhysicalExtent](./iostorage/api-1574993-copyphysicalextent.md)
- [- discard](./iostorage/api-1574961-discard.md)
- [- getMetaClass](./iostorage/api-1574982-getmetaclass.md)
- [- getProvisionStatus](./iostorage/api-1644751-getprovisionstatus.md)
- [- handleClose](./iostorage/api-1574998-handleclose.md)
- [- handleIsOpen](./iostorage/api-1574986-handleisopen.md)
- [- handleOpen](./iostorage/api-1574957-handleopen.md)
- [- lockPhysicalExtents](./iostorage/api-1575002-lockphysicalextents.md)
- [- open](./iostorage/api-1574976-open.md)
- [- read](./iostorage/api-1574962-read.md)
- [- read](./iostorage/api-3516780-read.md)
- [- setPriority](./iostorage/api-1574967-setpriority.md)
- [- synchronize](./iostorage/api-1574954-synchronize.md)
- [- synchronizeCache](./iostorage/api-1574981-synchronizecache.md)
- [- unlockPhysicalExtents](./iostorage/api-1574979-unlockphysicalextents.md)
- [- unmap](./iostorage/api-1575001-unmap.md)
- [- write](./iostorage/api-1574965-write.md)
- [- write](./iostorage/api-3516781-write.md)
### Type Methods
- [+ complete](./iostorage/api-1575005-complete.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Drivers
- [IOBDBlockStorageDriver](./iobdblockstoragedriver.md)
- [IODVDBlockStorageDriver](./iodvdblockstoragedriver.md)
- [IOCDBlockStorageDriver](./iocdblockstoragedriver.md)
- [IOBlockStorageDriver](./ioblockstoragedriver.md)
  The common base class for generic block storage drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage)*