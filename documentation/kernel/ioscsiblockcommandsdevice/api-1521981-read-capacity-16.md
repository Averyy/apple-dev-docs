# READ_CAPACITY_16

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
bool READ_CAPACITY_16(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS, SCSICmdField4Byte ALLOCATION_LENGTH, SCSICmdField1Bit PMI, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/1521981-read_capacity_16)*