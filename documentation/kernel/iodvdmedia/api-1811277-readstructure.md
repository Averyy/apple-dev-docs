# readStructure

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn readStructure(
 IOMemoryDescriptor *buffer, 
 const DVDStructureFormatformat, 
 const UInt32address, 
 const UInt8layer, 
 const UInt8grantID );
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC READ DVD STRUCTURE command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `format`: As documented by MMC.
- `address`: As documented by MMC.
- `layer`: As documented by MMC.
- `grantID`: As documented by MMC.

## See Also

- [getSpeed](iodvdmedia/1811144-getspeed.md)
- [readDiscInfo](iodvdmedia/1811197-readdiscinfo.md)
- [readRZoneInfo](iodvdmedia/1811250-readrzoneinfo.md)
- [reportKey](iodvdmedia/1811294-reportkey.md)
- [sendKey](iodvdmedia/1811314-sendkey.md)
- [setSpeed](iodvdmedia/1811329-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811277-readstructure)*