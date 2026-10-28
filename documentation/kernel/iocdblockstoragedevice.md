# IOCDBlockStorageDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The IOCDBlockStorageDevice class is a generic CD block storage device abstraction.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOCDBlockStorageDevice : IOBlockStorageDevice
```

## Overview

This class is the protocol for generic CD functionality, independent of the physical connection protocol (e.g. SCSI, ATA, USB).

The APIs are the union of CD (block storage) data APIs and all necessary low-level CD APIs.

A subclass implements relay methods that translate our requests into calls to a protocol- and device-specific provider.

## Topics

### Instance Methods
- [- doAsyncReadCD](./iocdblockstoragedevice/api-1578555-doasyncreadcd.md)
- [- getMediaType](./iocdblockstoragedevice/api-1578556-getmediatype.md)
- [- getMetaClass](./iocdblockstoragedevice/api-1578565-getmetaclass.md)
- [- getSpeed](./iocdblockstoragedevice/api-1578567-getspeed.md)
- [- init](./iocdblockstoragedevice/api-1578562-init.md)
- [- readDiscInfo](./iocdblockstoragedevice/api-1578568-readdiscinfo.md)
- [- readISRC](./iocdblockstoragedevice/api-1578558-readisrc.md)
- [- readMCN](./iocdblockstoragedevice/api-1578557-readmcn.md)
- [- readTOC](./iocdblockstoragedevice/api-1578559-readtoc.md)
- [- readTOC](./iocdblockstoragedevice/api-3516774-readtoc.md)
- [- readTrackInfo](./iocdblockstoragedevice/api-1578560-readtrackinfo.md)
- [- setSpeed](./iocdblockstoragedevice/api-1578564-setspeed.md)

## Relationships

### Inherits From
- [IOBlockStorageDevice](./ioblockstoragedevice.md)

## See Also

### Devices
- [IOBlockStorageServices](./ioblockstorageservices.md)
- [IOBDServices](./iobdservices.md)
- [IOBlockStorageDevice](./ioblockstoragedevice.md)
  A generic block storage device abstraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdblockstoragedevice)*