# READ_SUB_CHANNEL

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool READ_SUB_CHANNEL(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit MSF, SCSICmdField1Bit SUBQ, SCSICmdField1Byte SUB_CHANNEL_PARAMETER_LIST, SCSICmdField1Byte TRACK_NUMBER, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576342-read_sub_channel)*