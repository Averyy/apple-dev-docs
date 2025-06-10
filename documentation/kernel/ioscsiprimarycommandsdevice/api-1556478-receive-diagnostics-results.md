# RECEIVE_DIAGNOSTICS_RESULTS

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool RECEIVE_DIAGNOSTICS_RESULTS(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit PCV, SCSICmdField1Byte PAGE_CODE, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556478-receive_diagnostics_results)*