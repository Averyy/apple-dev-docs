# GET_LBA_STATUS

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.12+

## Declaration

```swift
bool GET_LBA_STATUS(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS, SCSICmdField4Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/1792145-get_lba_status)*