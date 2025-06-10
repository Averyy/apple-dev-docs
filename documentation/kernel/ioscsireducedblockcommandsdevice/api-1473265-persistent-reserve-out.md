# PERSISTENT_RESERVE_OUT

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool PERSISTENT_RESERVE_OUT(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField5Bit SERVICE_ACTION, SCSICmdField4Bit SCOPE, SCSICmdField4Bit TYPE);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsireducedblockcommandsdevice/1473265-persistent_reserve_out)*