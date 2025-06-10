# SEND_KEY_V2

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
bool SEND_KEY_V2(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Byte KEY_CLASS, SCSICmdField2Byte PARAMETER_LIST_LENGTH, SCSICmdField2Bit AGID, SCSICmdField6Bit KEY_FORMAT, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576216-send_key_v2)*