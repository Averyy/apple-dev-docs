# sendKey

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn sendKey(
 IOMemoryDescriptor *buffer, 
 UInt8keyClass, 
 UInt8grantID, 
 UInt8format );
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC SEND KEY command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `keyClass`: As documented by MMC.
- `grantID`: As documented by MMC.
- `format`: As documented by MMC.

## See Also

- [getSpeed](iobdmedia/1811688-getspeed.md)
- [readDiscInfo](iobdmedia/1811707-readdiscinfo.md)
- [readStructure](iobdmedia/1811722-readstructure.md)
- [readTrackInfo](iobdmedia/1811739-readtrackinfo.md)
- [reportKey](iobdmedia/1811756-reportkey.md)
- [setSpeed](iobdmedia/1811802-setspeed.md)
- [splitTrack](iobdmedia/1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811776-sendkey)*