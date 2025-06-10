# readRZoneInfo

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readRZoneInfo(
 IOMemoryDescriptor *buffer, 
 UInt32address, 
 DVDRZoneInfoAddressTypeaddressType, 
 UInt16 *actualByteCount );
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC READ RZONE INFORMATION (READ TRACK INFORMATION) command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `address`: As documented by MMC.
- `addressType`: As documented by MMC.
- `actualByteCount`: Returns the actual number of bytes transferred in the data transfer.

## See Also

- [getSpeed](iodvdmedia/1811144-getspeed.md)
- [readDiscInfo](iodvdmedia/1811197-readdiscinfo.md)
- [readStructure](iodvdmedia/1811277-readstructure.md)
- [reportKey](iodvdmedia/1811294-reportkey.md)
- [sendKey](iodvdmedia/1811314-sendkey.md)
- [setSpeed](iodvdmedia/1811329-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811250-readrzoneinfo)*