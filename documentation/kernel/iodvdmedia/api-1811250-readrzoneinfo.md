# readRZoneInfo

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn readRZoneInfo(
 IOMemoryDescriptor *buffer, 
 UInt32address, 
 DVDRZoneInfoAddressTypeaddressType, 
 UInt16 *actualByteCount );
```

## Return Value

Returns the status of the data transfer.

## Overview

Issue an MMC READ RZONE INFORMATION (READ TRACK INFORMATION) command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `address`: As documented by MMC.
- `addressType`: As documented by MMC.
- `actualByteCount`: Returns the actual number of bytes transferred in the data transfer.

## See Also

### Miscellaneous
- [getSpeed](./api-1811144-getspeed.md)
- [readDiscInfo](./api-1811197-readdiscinfo.md)
- [readStructure](./api-1811277-readstructure.md)
- [reportKey](./api-1811294-reportkey.md)
- [sendKey](./api-1811314-sendkey.md)
- [setSpeed](./api-1811329-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811250-readrzoneinfo)*