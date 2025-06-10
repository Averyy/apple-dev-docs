# splitTrack

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn splitTrack(
 UInt32address);
```

#### Return_value

Returns the status of the operation.

#### Overview

Issue an MMC RESERVE TRACK command with the ARSV bit.

## Parameters

- `address`: As documented by MMC.

## See Also

- [getSpeed](iobdmedia/1811688-getspeed.md)
- [readDiscInfo](iobdmedia/1811707-readdiscinfo.md)
- [readStructure](iobdmedia/1811722-readstructure.md)
- [readTrackInfo](iobdmedia/1811739-readtrackinfo.md)
- [reportKey](iobdmedia/1811756-reportkey.md)
- [sendKey](iobdmedia/1811776-sendkey.md)
- [setSpeed](iobdmedia/1811802-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811824-splittrack)*