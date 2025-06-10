# WRITE_BUFFER

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool WRITE_BUFFER(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField4Bit MODE, SCSICmdField1Byte BUFFER_ID, SCSICmdField3Byte BUFFER_OFFSET, SCSICmdField3Byte PARAMETER_LIST_LENGTH);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsireducedblockcommandsdevice/1473428-write_buffer)*