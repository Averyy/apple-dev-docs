# splitTrack

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn splitTrack(
 UInt32address);
```

## Return Value

Returns the status of the operation.

## Overview

Issue an MMC RESERVE TRACK command with the ARSV bit.

## Parameters

- `address`: As documented by MMC.

## See Also

### Miscellaneous
- [getSpeed](./api-1811688-getspeed.md)
- [readDiscInfo](./api-1811707-readdiscinfo.md)
- [readStructure](./api-1811722-readstructure.md)
- [readTrackInfo](./api-1811739-readtrackinfo.md)
- [reportKey](./api-1811756-reportkey.md)
- [sendKey](./api-1811776-sendkey.md)
- [setSpeed](./api-1811802-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811824-splittrack)*