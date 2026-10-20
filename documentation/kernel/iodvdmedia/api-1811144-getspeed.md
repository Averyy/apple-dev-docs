# getSpeed

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn getSpeed(
 UInt16 *kilobytesPerSecond);
```

#### Return Value

Returns the status of the operation.

#### Overview

Get the current speed used for data transfers.

## Parameters

- `kilobytesPerSecond`: Returns the current speed used for data transfers, in kB/s.

  kDVDSpeedMin specifies the minimum speed for all DVD media (1X). kDVDSpeedMax specifies the maximum speed supported in hardware.

## See Also

### Miscellaneous
- [readDiscInfo](./api-1811197-readdiscinfo.md)
- [readRZoneInfo](./api-1811250-readrzoneinfo.md)
- [readStructure](./api-1811277-readstructure.md)
- [reportKey](./api-1811294-reportkey.md)
- [sendKey](./api-1811314-sendkey.md)
- [setSpeed](./api-1811329-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811144-getspeed)*