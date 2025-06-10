# getSpeed

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn getSpeed(
 UInt16 *kilobytesPerSecond);
```

#### Return_value

Returns the status of the operation.

#### Overview

Get the current speed used for data transfers.

## Parameters

- `kilobytesPerSecond`: kBDSpeedMin specifies the minimum speed for all BD media (1X). kBDSpeedMax specifies the maximum speed supported in hardware.

## See Also

- [readDiscInfo](iobdmedia/1811707-readdiscinfo.md)
- [readStructure](iobdmedia/1811722-readstructure.md)
- [readTrackInfo](iobdmedia/1811739-readtrackinfo.md)
- [reportKey](iobdmedia/1811756-reportkey.md)
- [sendKey](iobdmedia/1811776-sendkey.md)
- [setSpeed](iobdmedia/1811802-setspeed.md)
- [splitTrack](iobdmedia/1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811688-getspeed)*