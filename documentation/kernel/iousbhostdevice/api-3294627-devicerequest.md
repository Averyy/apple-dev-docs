# DeviceRequest

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15+ - Deprecated in 10.15.4

## Declaration

```swift
kern_return_t DeviceRequest(IOService *forClient, uint8_t bmRequestType, uint8_t bRequest, uint16_t wValue, uint16_t wIndex, uint16_t wLength, IOMemoryDescriptor *dataBuffer, uint16_t *bytesTransferred, uint32_t completionTimeoutMs, OSDispatchMethod supermethod);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostdevice/3294627-devicerequest)*