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

  kDVDSpeedMin specifies the minimum speed for all DVD media (1X). kDVDSpeedMax specifies the maximum speed supported in hardware.

## See Also

### Miscellaneous
- [getSpeed](./api-1811144-getspeed.md)
- [readDiscInfo](./api-1811197-readdiscinfo.md)
- [readRZoneInfo](./api-1811250-readrzoneinfo.md)
- [readStructure](./api-1811277-readstructure.md)
- [reportKey](./api-1811294-reportkey.md)
- [sendKey](./api-1811314-sendkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811329-setspeed)*