# SYNCHRONIZE_CACHE

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool SYNCHRONIZE_CACHE(SCSITaskIdentifier request, SCSICmdField1Bit IMMED, SCSICmdField1Bit RELADR, SCSICmdField4Byte LOGICAL_BLOCK_ADDRESS, SCSICmdField2Byte NUMBER_OF_BLOCKS, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/1522004-synchronize_cache)*