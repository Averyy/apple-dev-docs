# readStructure

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn readStructure(
 IOMemoryDescriptor *buffer, 
 UInt8format, 
 UInt32address, 
 UInt8layer, 
 UInt8grantID );
```

#### Return Value

Returns the status of the data transfer.

#### Overview

Issue an MMC READ DISC STRUCTURE command.

## Parameters

- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `format`: As documented by MMC.
- `address`: As documented by MMC.
- `layer`: As documented by MMC.
- `grantID`: As documented by MMC.

## See Also

### Miscellaneous
- [getSpeed](./api-1811688-getspeed.md)
- [readDiscInfo](./api-1811707-readdiscinfo.md)
- [readTrackInfo](./api-1811739-readtrackinfo.md)
- [reportKey](./api-1811756-reportkey.md)
- [sendKey](./api-1811776-sendkey.md)
- [setSpeed](./api-1811802-setspeed.md)
- [splitTrack](./api-1811824-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdmedia/1811722-readstructure)*