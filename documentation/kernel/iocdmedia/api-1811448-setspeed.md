# setSpeed

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn setSpeed(
 UInt16kilobytesPerSecond);
```

## Return Value

Returns the status of the operation.

## Overview

Set the speed to be used for data transfers.

## Parameters

- `kilobytesPerSecond`: Speed to be used for data transfers, in kB/s.

  kCDSpeedMin specifies the minimum speed for all CD media (1X). kCDSpeedMax specifies the maximum speed supported in hardware.

## See Also

### Miscellaneous
- [getSpeed](./api-1811353-getspeed.md)
- [getTOC](./api-1811363-gettoc.md)
- [read](./api-1811376-read.md)
- [readCD()](./api-1811386-readcd.md)
- [readCD()](./api-1811393-readcd.md)
- [readDiscInfo](./api-1811402-readdiscinfo.md)
- [readISRC](./api-1811412-readisrc.md)
- [readMCN](./api-1811424-readmcn.md)
- [readTOC](./api-1811431-readtoc.md)
- [readTrackInfo](./api-1811438-readtrackinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811448-setspeed)*