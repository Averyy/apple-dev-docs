# sendKey

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn sendKey(
 IOMemoryDescriptor *buffer, 
 const DVDKeyClasskeyClass, 
 const UInt8grantID, 
 const DVDKeyFormatformat );
```

#### Return_value

Returns the status of the data transfer.

#### Overview

Issue an MMC SEND KEY command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer. Pass null for the kDVDKeyFormatAGID_Invalidate format case.
- `keyClass`: As documented by MMC.
- `grantID`: As documented by MMC.
- `format`: As documented by MMC.

## See Also

- [getSpeed](iodvdmedia/1811144-getspeed.md)
- [readDiscInfo](iodvdmedia/1811197-readdiscinfo.md)
- [readRZoneInfo](iodvdmedia/1811250-readrzoneinfo.md)
- [readStructure](iodvdmedia/1811277-readstructure.md)
- [reportKey](iodvdmedia/1811294-reportkey.md)
- [setSpeed](iodvdmedia/1811329-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodvdmedia/1811314-sendkey)*