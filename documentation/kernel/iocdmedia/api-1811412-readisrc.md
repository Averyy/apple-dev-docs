# readISRC

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readISRC(
 UInt8track,
 CDISRCisrc);
```

#### Return_value

Returns the status of the operation.

#### Overview

Read the International Standard Recording Code for the specified track.

## Parameters

- `track`: Track number from which to read the ISRC.
- `isrc`: Buffer for the ISRC data. Buffer contents will be zero-terminated.

## See Also

- [getSpeed](iocdmedia/1811353-getspeed.md)
- [getTOC](iocdmedia/1811363-gettoc.md)
- [read](iocdmedia/1811376-read.md)
- [readCD()](iocdmedia/1811386-readcd.md)
- [readCD()](iocdmedia/1811393-readcd.md)
- [readDiscInfo](iocdmedia/1811402-readdiscinfo.md)
- [readMCN](iocdmedia/1811424-readmcn.md)
- [readTOC](iocdmedia/1811431-readtoc.md)
- [readTrackInfo](iocdmedia/1811438-readtrackinfo.md)
- [setSpeed](iocdmedia/1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811412-readisrc)*