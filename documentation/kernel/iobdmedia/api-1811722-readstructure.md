# readStructure

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readStructure(
 IOMemoryDescriptor *buffer, 
 UInt8format, 
 UInt32address, 
 UInt8layer, 
 UInt8grantID );
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC READ DISC STRUCTURE command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `format`: As documented by MMC.
- `address`: As documented by MMC.
- `layer`: As documented by MMC.
- `grantID`: As documented by MMC.

## See Also

- [getSpeed](iobdmedia/1811688-getspeed.md)
- [readDiscInfo](iobdmedia/1811707-readdiscinfo.md)
- [readTrackInfo](iobdmedia/1811739-readtrackinfo.md)
- [reportKey](iobdmedia/1811756-reportkey.md)
- [sendKey](iobdmedia/1811776-sendkey.md)
- [setSpeed](iobdmedia/1811802-setspeed.md)
- [splitTrack](iobdmedia/1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811722-readstructure)*