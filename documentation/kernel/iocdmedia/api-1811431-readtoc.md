# readTOC

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readTOC(
 IOMemoryDescriptor *buffer, 
 CDTOCFormatformat, 
 UInt8formatAsTime, 
 UInt8trackOrSessionNumber, 
 UInt16 *actualByteCount);
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC READ TOC/PMA/ATIP command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `format`: As documented by MMC.
- `formatAsTime`: As documented by MMC.
- `trackOrSessionNumber`: As documented by MMC.
- `actualByteCount`: Returns the actual number of bytes transferred in the data transfer.

## See Also

- [getSpeed](iocdmedia/1811353-getspeed.md)
- [getTOC](iocdmedia/1811363-gettoc.md)
- [read](iocdmedia/1811376-read.md)
- [readCD()](iocdmedia/1811386-readcd.md)
- [readCD()](iocdmedia/1811393-readcd.md)
- [readDiscInfo](iocdmedia/1811402-readdiscinfo.md)
- [readISRC](iocdmedia/1811412-readisrc.md)
- [readMCN](iocdmedia/1811424-readmcn.md)
- [readTrackInfo](iocdmedia/1811438-readtrackinfo.md)
- [setSpeed](iocdmedia/1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811431-readtoc)*