# RESERVE_10

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool RESERVE_10(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit THRDPTY, SCSICmdField1Bit LONGID, SCSICmdField1Byte THIRD_PARTY_DEVICE_ID, SCSICmdField2Byte PARAMETER_LIST_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556489-reserve_10)*