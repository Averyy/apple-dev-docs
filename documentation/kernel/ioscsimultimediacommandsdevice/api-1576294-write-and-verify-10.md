# WRITE_AND_VERIFY_10

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool WRITE_AND_VERIFY_10(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, UInt32 blockSize, SCSICmdField1Bit DPO, SCSICmdField1Bit BYT_CHK, SCSICmdField1Bit RELADR, SCSICmdField4Byte LOGICAL_BLOCK_ADDRESS, SCSICmdField4Byte TRANSFER_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576294-write_and_verify_10)*