# WRITE_SAME_16

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.12+

## Declaration

```swift
bool WRITE_SAME_16(SCSITaskIdentifier request, IOMemoryDescriptor *buffer, UInt32 requestBlockSize, SCSICmdField3Bit WRPROTECT, SCSICmdField1Bit ANCHOR, SCSICmdField1Bit UNMAP, SCSICmdField1Bit NDOB, SCSICmdField8Byte startBlock, SCSICmdField4Byte blockCount, SCSICmdField6Bit GROUP_NUMBER, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/1792139-write_same_16)*