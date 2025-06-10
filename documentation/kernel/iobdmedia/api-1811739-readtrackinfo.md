# readTrackInfo

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readTrackInfo(
 IOMemoryDescriptor *buffer, 
 UInt32address, 
 UInt8addressType, 
 UInt8open, 
 UInt16 *actualByteCount );
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC READ TRACK INFORMATION command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `address`: As documented by MMC.
- `addressType`: As documented by MMC.
- `open`: Reserved for future use. Set to zero.
- `actualByteCount`: Returns the actual number of bytes transferred in the data transfer.

## See Also

- [getSpeed](iobdmedia/1811688-getspeed.md)
- [readDiscInfo](iobdmedia/1811707-readdiscinfo.md)
- [readStructure](iobdmedia/1811722-readstructure.md)
- [reportKey](iobdmedia/1811756-reportkey.md)
- [sendKey](iobdmedia/1811776-sendkey.md)
- [setSpeed](iobdmedia/1811802-setspeed.md)
- [splitTrack](iobdmedia/1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811739-readtrackinfo)*