# INQUIRY

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool INQUIRY(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit CMDDT, SCSICmdField1Bit EVPD, SCSICmdField1Byte PAGE_OR_OPERATION_CODE, SCSICmdField1Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556549-inquiry)*