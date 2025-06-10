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

- `kilobytesPerSecond`: kCDSpeedMin specifies the minimum speed for all CD media (1X). kCDSpeedMax specifies the maximum speed supported in hardware.

## See Also

- [getSpeed](iocdmedia/1811353-getspeed.md)
- [getTOC](iocdmedia/1811363-gettoc.md)
- [read](iocdmedia/1811376-read.md)
- [readCD()](iocdmedia/1811386-readcd.md)
- [readCD()](iocdmedia/1811393-readcd.md)
- [readDiscInfo](iocdmedia/1811402-readdiscinfo.md)
- [readISRC](iocdmedia/1811412-readisrc.md)
- [readMCN](iocdmedia/1811424-readmcn.md)
- [readTOC](iocdmedia/1811431-readtoc.md)
- [readTrackInfo](iocdmedia/1811438-readtrackinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811448-setspeed)*