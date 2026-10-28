# splitTrack

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn splitTrack(
 UInt32address) = 0;
```

## Return Value

Returns the status of the operation.

## Overview

Issue an MMC RESERVE TRACK command with the ARSV bit.

## Parameters

- `address`: As documented by MMC.

## See Also

### Miscellaneous
- [init](./api-1811554-init.md)
- [readDiscStructure](./api-1811564-readdiscstructure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdblockstoragedevice/1811575-splittrack)*