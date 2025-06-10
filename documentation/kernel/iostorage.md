# IOStorage

**Framework**: Kernel  
**Kind**: cl

The common base class for mass storage objects.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOStorage : IOService
```

#### Overview

The IOStorage class is the common base class for mass storage objects. It is an abstract class that defines the open/close/read/write APIs that need to be implemented in a given subclass. Synchronous versions of the read/write APIs are provided here -- they are coded in such a way as to wrap the asynchronous versions implemented in the subclass.

## Topics

### Miscellaneous
- [complete](iostorage/1810767-complete.md)
- [copyPhysicalExtent](iostorage/1810820-copyphysicalextent.md)
- [handleClose](iostorage/1810866-handleclose.md)
- [handleIsOpen](iostorage/1810905-handleisopen.md)
- [handleOpen](iostorage/1810948-handleopen.md)
- [lockPhysicalExtents](iostorage/1810985-lockphysicalextents.md)
- [open](iostorage/1811013-open.md)
- [read()](iostorage/1811038-read.md)
- [read()](iostorage/1811068-read.md)
- [synchronizeCache](iostorage/1811091-synchronizecache.md)
- [unlockPhysicalExtents](iostorage/1811117-unlockphysicalextents.md)
- [unmap](iostorage/1811145-unmap.md)
- [write()](iostorage/1811168-write.md)
- [write()](iostorage/1811185-write.md)
### Instance Methods
- [- attach](iostorage/1574956-attach.md)
- [- copyPhysicalExtent](iostorage/1574993-copyphysicalextent.md)
- [- discard](iostorage/1574961-discard.md)
- [- getMetaClass](iostorage/1574982-getmetaclass.md)
- [- getProvisionStatus](iostorage/1644751-getprovisionstatus.md)
- [- handleClose](iostorage/1574998-handleclose.md)
- [- handleIsOpen](iostorage/1574986-handleisopen.md)
- [- handleOpen](iostorage/1574957-handleopen.md)
- [- lockPhysicalExtents](iostorage/1575002-lockphysicalextents.md)
- [- open](iostorage/1574976-open.md)
- [- read](iostorage/1574962-read.md)
- [- read](iostorage/3516780-read.md)
- [- setPriority](iostorage/1574967-setpriority.md)
- [- synchronize](iostorage/1574954-synchronize.md)
- [- synchronizeCache](iostorage/1574981-synchronizecache.md)
- [- unlockPhysicalExtents](iostorage/1574979-unlockphysicalextents.md)
- [- unmap](iostorage/1575001-unmap.md)
- [- write](iostorage/1574965-write.md)
- [- write](iostorage/3516781-write.md)
### Type Methods
- [+ complete](iostorage/1575005-complete.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOBDBlockStorageDriver](iobdblockstoragedriver.md)
- [IODVDBlockStorageDriver](iodvdblockstoragedriver.md)
- [IOCDBlockStorageDriver](iocdblockstoragedriver.md)
- [IOBlockStorageDriver](ioblockstoragedriver.md)
  The common base class for generic block storage drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage)*