# READ_TRACK_INFORMATION

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool READ_TRACK_INFORMATION(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField2Bit ADDRESS_NUMBER_TYPE, SCSICmdField4Byte LOGICAL_BLOCK_ADDRESS_TRACK_SESSION_NUMBER, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576331-read_track_information)*