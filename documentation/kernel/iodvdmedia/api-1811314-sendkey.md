# sendKey

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn sendKey(
 IOMemoryDescriptor *buffer, 
 const DVDKeyClasskeyClass, 
 const UInt8grantID, 
 const DVDKeyFormatformat );
```

## Return Value

Returns the status of the data transfer.

## Overview

Issue an MMC SEND KEY command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer. Pass null for the kDVDKeyFormatAGID_Invalidate format case.
- `keyClass`: As documented by MMC.
- `grantID`: As documented by MMC.
- `format`: As documented by MMC.

## See Also

### Miscellaneous
- [getSpeed](./api-1811144-getspeed.md)
- [readDiscInfo](./api-1811197-readdiscinfo.md)
- [readRZoneInfo](./api-1811250-readrzoneinfo.md)
- [readStructure](./api-1811277-readstructure.md)
- [reportKey](./api-1811294-reportkey.md)
- [setSpeed](./api-1811329-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811314-sendkey)*