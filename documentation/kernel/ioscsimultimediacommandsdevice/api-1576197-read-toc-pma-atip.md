# READ_TOC_PMA_ATIP

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool READ_TOC_PMA_ATIP(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit MSF, SCSICmdField4Bit FORMAT, SCSICmdField1Byte TRACK_SESSION_NUMBER, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576197-read_toc_pma_atip)*