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

  kBDSpeedMin specifies the minimum speed for all BD media (1X). kBDSpeedMax specifies the maximum speed supported in hardware.

## See Also

### Miscellaneous
- [readDiscInfo](./api-1811707-readdiscinfo.md)
- [readStructure](./api-1811722-readstructure.md)
- [readTrackInfo](./api-1811739-readtrackinfo.md)
- [reportKey](./api-1811756-reportkey.md)
- [sendKey](./api-1811776-sendkey.md)
- [setSpeed](./api-1811802-setspeed.md)
- [splitTrack](./api-1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811688-getspeed)*