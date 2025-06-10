# READ_DISC_STRUCTURE

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
bool READ_DISC_STRUCTURE(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField4Bit MEDIA_TYPE, SCSICmdField4Byte ADDRESS, SCSICmdField1Byte LAYER_NUMBER, SCSICmdField1Byte FORMAT, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField2Bit AGID, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576170-read_disc_structure)*