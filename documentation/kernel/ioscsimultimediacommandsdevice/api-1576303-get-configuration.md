# GET_CONFIGURATION

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool GET_CONFIGURATION(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField2Bit RT, SCSICmdField2Byte STARTING_FEATURE_NUMBER, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576303-get_configuration)*