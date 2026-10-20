# PERSISTENT_RESERVE_IN

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual bool PERSISTENT_RESERVE_IN(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField5Bit SERVICE_ACTION, SCSICmdField2Byte ALLOCATION_LENGTH);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsireducedblockcommandsdevice/1473376-persistent_reserve_in)*