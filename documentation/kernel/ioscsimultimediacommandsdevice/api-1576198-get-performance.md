# GET_PERFORMANCE

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool GET_PERFORMANCE(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField2Bit TOLERANCE, SCSICmdField1Bit WRITE, SCSICmdField2Bit EXCEPT, SCSICmdField4Byte STARTING_LBA, SCSICmdField2Byte MAXIMUM_NUMBER_OF_DESCRIPTORS, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576198-get_performance)*