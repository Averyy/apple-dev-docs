# LOG_SELECT

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool LOG_SELECT(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit PCR, SCSICmdField1Bit SP, SCSICmdField2Bit PC, SCSICmdField2Byte PARAMETER_LIST_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556487-log_select)*