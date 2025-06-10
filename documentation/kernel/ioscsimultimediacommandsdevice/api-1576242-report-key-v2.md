# REPORT_KEY_V2

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+ - Deprecated in 10.12

## Declaration

```swift
bool REPORT_KEY_V2(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField4Byte LOGICAL_BLOCK_ADDRESS, SCSICmdField1Byte KEY_CLASS, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField2Bit AGID, SCSICmdField6Bit KEY_FORMAT, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576242-report_key_v2)*