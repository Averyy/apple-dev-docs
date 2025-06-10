# setSpeed

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn setSpeed(
 UInt16kilobytesPerSecond);
```

#### Return_value

Returns the status of the operation.

#### Overview

Set the speed to be used for data transfers.

## Parameters

- `kilobytesPerSecond`: kDVDSpeedMin specifies the minimum speed for all DVD media (1X). kDVDSpeedMax specifies the maximum speed supported in hardware.

## See Also

- [getSpeed](iodvdmedia/1811144-getspeed.md)
- [readDiscInfo](iodvdmedia/1811197-readdiscinfo.md)
- [readRZoneInfo](iodvdmedia/1811250-readrzoneinfo.md)
- [readStructure](iodvdmedia/1811277-readstructure.md)
- [reportKey](iodvdmedia/1811294-reportkey.md)
- [sendKey](iodvdmedia/1811314-sendkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811329-setspeed)*