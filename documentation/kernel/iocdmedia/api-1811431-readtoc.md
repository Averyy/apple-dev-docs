# readTOC

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn readTOC(
 IOMemoryDescriptor *buffer, 
 CDTOCFormatformat, 
 UInt8formatAsTime, 
 UInt8trackOrSessionNumber, 
 UInt16 *actualByteCount);
```

#### Return Value

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

### Miscellaneous
- [getSpeed](./api-1811353-getspeed.md)
- [getTOC](./api-1811363-gettoc.md)
- [read](./api-1811376-read.md)
- [readCD()](./api-1811386-readcd.md)
- [readCD()](./api-1811393-readcd.md)
- [readDiscInfo](./api-1811402-readdiscinfo.md)
- [readISRC](./api-1811412-readisrc.md)
- [readMCN](./api-1811424-readmcn.md)
- [readTrackInfo](./api-1811438-readtrackinfo.md)
- [setSpeed](./api-1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811431-readtoc)*