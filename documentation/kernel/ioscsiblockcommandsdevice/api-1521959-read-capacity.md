# READ_CAPACITY

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool READ_CAPACITY(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit RELADR, SCSICmdField4Byte LOGICAL_BLOCK_ADDRESS, SCSICmdField1Bit PMI, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/1521959-read_capacity)*