# SYNCHRONIZE_CACHE

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
bool SYNCHRONIZE_CACHE(SCSITaskIdentifier request, SCSICmdField1Bit IMMED, SCSICmdField1Bit SYNC_NV, SCSICmdField4Byte LOGICAL_BLOCK_ADDRESS, SCSICmdField6Bit GROUP_NUMBER, SCSICmdField2Byte NUMBER_OF_BLOCKS, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/3516749-synchronize_cache)*