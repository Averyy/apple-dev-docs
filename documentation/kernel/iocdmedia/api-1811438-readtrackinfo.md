# readTrackInfo

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn readTrackInfo(
 IOMemoryDescriptor *buffer, 
 UInt32address, 
 CDTrackInfoAddressTypeaddressType, 
 UInt16 *actualByteCount);
```

## Return Value

Returns the status of the data transfer.

## Overview

Issue an MMC READ TRACK INFORMATION command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `address`: As documented by MMC.
- `addressType`: As documented by MMC.
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
- [readTOC](./api-1811431-readtoc.md)
- [setSpeed](./api-1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811438-readtrackinfo)*