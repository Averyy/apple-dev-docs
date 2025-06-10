# readMCN

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readMCN(
 CDMCNmcn);
```

#### Return_value

Returns the status of the operation.

#### Overview

Read the Media Catalog Number (also known as the Universal Product Code).

## Parameters

- `mcn`: Buffer for the MCN data. Buffer contents will be zero-terminated.

## See Also

- [getSpeed](iocdmedia/1811353-getspeed.md)
- [getTOC](iocdmedia/1811363-gettoc.md)
- [read](iocdmedia/1811376-read.md)
- [readCD()](iocdmedia/1811386-readcd.md)
- [readCD()](iocdmedia/1811393-readcd.md)
- [readDiscInfo](iocdmedia/1811402-readdiscinfo.md)
- [readISRC](iocdmedia/1811412-readisrc.md)
- [readTOC](iocdmedia/1811431-readtoc.md)
- [readTrackInfo](iocdmedia/1811438-readtrackinfo.md)
- [setSpeed](iocdmedia/1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811424-readmcn)*