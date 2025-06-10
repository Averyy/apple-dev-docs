# MODE_SENSE_10

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool MODE_SENSE_10(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit LLBAA, SCSICmdField1Bit DBD, SCSICmdField2Bit PC, SCSICmdField6Bit PAGE_CODE, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556538-mode_sense_10)*