# MODE_SENSE_6

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool MODE_SENSE_6(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit DBD, SCSICmdField2Bit PC, SCSICmdField6Bit PAGE_CODE, SCSICmdField1Byte ALLOCATION_LENGTH);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsireducedblockcommandsdevice/1473235-mode_sense_6)*