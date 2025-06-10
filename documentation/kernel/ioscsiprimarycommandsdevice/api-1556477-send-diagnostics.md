# SEND_DIAGNOSTICS

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool SEND_DIAGNOSTICS(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField3Bit SELF_TEST_CODE, SCSICmdField1Bit PF, SCSICmdField1Bit SELF_TEST, SCSICmdField1Bit DEVOFFL, SCSICmdField1Bit UNITOFFL, SCSICmdField2Byte PARAMETER_LIST_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556477-send_diagnostics)*