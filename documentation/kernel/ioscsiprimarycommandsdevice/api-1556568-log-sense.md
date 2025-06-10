# LOG_SENSE

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool LOG_SENSE(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit PPC, SCSICmdField1Bit SP, SCSICmdField2Bit PC, SCSICmdField6Bit PAGE_CODE, SCSICmdField2Byte PARAMETER_POINTER, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556568-log_sense)*