# IOBDBlockStorageDevice

**Framework**: Kernel  
**Kind**: cl

The IOBDBlockStorageDevice class is a generic BD block storage device abstraction.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOBDBlockStorageDevice : IODVDBlockStorageDevice
```

#### Overview

This class is the protocol for generic BD functionality, independent of the physical connection protocol (e.g. SCSI, ATA, USB).

The APIs are the union of CD APIs, DVD APIs, and all necessary new low-level BD APIs.

A subclass implements relay methods that translate our requests into calls to a protocol- and device-specific provider.

## Topics

### Miscellaneous
- [init](iobdblockstoragedevice/1811554-init.md)
- [readDiscStructure](iobdblockstoragedevice/1811564-readdiscstructure.md)
- [splitTrack](iobdblockstoragedevice/1811575-splittrack.md)
### Instance Methods
- [- getMetaClass](iobdblockstoragedevice/1541734-getmetaclass.md)
- [- init](iobdblockstoragedevice/1541739-init.md)
- [- readDiscStructure](iobdblockstoragedevice/1541740-readdiscstructure.md)
- [- splitTrack](iobdblockstoragedevice/1541738-splittrack.md)

## Relationships

### Inherits From
- [IODVDBlockStorageDevice](iodvdblockstoragedevice.md)

## See Also

- [IODVDServices](iodvdservices.md)
- [IODVDBlockStorageDevice](iodvdblockstoragedevice.md)
  The IODVDBlockStorageDevice class is a generic DVD block storage device abstraction.
- [IOCompactDiscServices](iocompactdiscservices.md)
- [IOBDMediaBSDClient](iobdmediabsdclient.md)
- [IOMediaBSDClient](iomediabsdclient.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdblockstoragedevice)*