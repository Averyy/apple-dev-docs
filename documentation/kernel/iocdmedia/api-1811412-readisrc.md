# readISRC

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn readISRC(
 UInt8track,
 CDISRCisrc);
```

#### Return Value

Returns the status of the operation.

#### Overview

Read the International Standard Recording Code for the specified track.

## Parameters

- `track`: Track number from which to read the ISRC.
- `isrc`: Buffer for the ISRC data. Buffer contents will be zero-terminated.

## See Also

### Miscellaneous
- [getSpeed](./api-1811353-getspeed.md)
- [getTOC](./api-1811363-gettoc.md)
- [read](./api-1811376-read.md)
- [readCD()](./api-1811386-readcd.md)
- [readCD()](./api-1811393-readcd.md)
- [readDiscInfo](./api-1811402-readdiscinfo.md)
- [readMCN](./api-1811424-readmcn.md)
- [readTOC](./api-1811431-readtoc.md)
- [readTrackInfo](./api-1811438-readtrackinfo.md)
- [setSpeed](./api-1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811412-readisrc)*