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

  kBDSpeedMin specifies the minimum speed for all BD media (1X). kBDSpeedMax specifies the maximum speed supported in hardware.

## See Also

### Miscellaneous
- [getSpeed](./api-1811688-getspeed.md)
- [readDiscInfo](./api-1811707-readdiscinfo.md)
- [readStructure](./api-1811722-readstructure.md)
- [readTrackInfo](./api-1811739-readtrackinfo.md)
- [reportKey](./api-1811756-reportkey.md)
- [sendKey](./api-1811776-sendkey.md)
- [splitTrack](./api-1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811802-setspeed)*