# readDiscStructure

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn readDiscStructure(
 IOMemoryDescriptor *buffer, 
 UInt8format, 
 UInt32address, 
 UInt8layer, 
 UInt8grantID, 
 UInt8type ) = 0;
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
- `type`: As documented by MMC.

## See Also

### Miscellaneous
- [init](./api-1811554-init.md)
- [splitTrack](./api-1811575-splittrack.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdblockstoragedevice/1811564-readdiscstructure)*