# SET_DEVICE_IDENTIFIER

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool SET_DEVICE_IDENTIFIER(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField5Bit SERVICE_ACTION, SCSICmdField4Byte PARAMETER_LIST_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556467-set_device_identifier)*