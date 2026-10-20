# WRITE_SAME_10

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.12+

## Declaration

```c
bool WRITE_SAME_10(SCSITaskIdentifier request, IOMemoryDescriptor *buffer, UInt32 requestBlockSize, SCSICmdField3Bit WRPROTECT, SCSICmdField1Bit ANCHOR, SCSICmdField1Bit UNMAP, SCSICmdField4Byte startBlock, SCSICmdField6Bit GROUP_NUMBER, SCSICmdField2Byte blockCount, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/1792140-write_same_10)*