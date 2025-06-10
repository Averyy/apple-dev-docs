# readDiscInfo

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readDiscInfo(
 IOMemoryDescriptor *buffer, 
 UInt8type, 
 UInt16 *actualByteCount );
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC READ DISC INFORMATION command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `type`: Reserved for future use. Set to zero.
- `actualByteCount`: Returns the actual number of bytes transferred in the data transfer.

## See Also

- [getSpeed](iobdmedia/1811688-getspeed.md)
- [readStructure](iobdmedia/1811722-readstructure.md)
- [readTrackInfo](iobdmedia/1811739-readtrackinfo.md)
- [reportKey](iobdmedia/1811756-reportkey.md)
- [sendKey](iobdmedia/1811776-sendkey.md)
- [setSpeed](iobdmedia/1811802-setspeed.md)
- [splitTrack](iobdmedia/1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811707-readdiscinfo)*