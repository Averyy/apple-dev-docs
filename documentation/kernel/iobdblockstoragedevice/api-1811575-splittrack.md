# splitTrack

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn splitTrack(
 UInt32address) = 0;
```

#### Return_value

Returns the status of the operation.

#### Overview

Issue an MMC RESERVE TRACK command with the ARSV bit.

## Parameters

- `address`: As documented by MMC.

## See Also

- [init](iobdblockstoragedevice/1811554-init.md)
- [readDiscStructure](iobdblockstoragedevice/1811564-readdiscstructure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdblockstoragedevice/1811575-splittrack)*