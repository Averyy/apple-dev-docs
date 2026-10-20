# SET_READ_AHEAD

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual bool SET_READ_AHEAD(SCSITaskIdentifier request, SCSICmdField4Byte TRIGGER_LOGICAL_BLOCK_ADDRESS, SCSICmdField4Byte READ_AHEAD_LOGICAL_BLOCK_ADDRESS, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576187-set_read_ahead)*