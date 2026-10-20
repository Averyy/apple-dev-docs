# UNMAP

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.12+

## Declaration

```c
bool UNMAP(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit ANCHOR, SCSICmdField6Bit GROUP_NUMBER, SCSICmdField2Byte PARAMETER_LIST_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/1792152-unmap)*