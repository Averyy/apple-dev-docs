# GET_EVENT_STATUS_NOTIFICATION

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool GET_EVENT_STATUS_NOTIFICATION(SCSITaskIdentifier request, IOMemoryDescriptor *dataBuffer, SCSICmdField1Bit IMMED, SCSICmdField1Byte NOTIFICATION_CLASS_REQUEST, SCSICmdField2Byte ALLOCATION_LENGTH, SCSICmdField1Byte CONTROL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576286-get_event_status_notification)*