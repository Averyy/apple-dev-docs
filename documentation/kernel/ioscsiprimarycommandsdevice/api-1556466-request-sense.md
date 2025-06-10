# REQUEST_SENSE

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool REQUEST_SENSE(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice/1556466-request_sense)*