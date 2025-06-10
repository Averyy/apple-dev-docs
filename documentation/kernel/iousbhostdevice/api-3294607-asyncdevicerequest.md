# AsyncDeviceRequest

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15+ - Deprecated in 10.15.4

## Declaration

```swift
kern_return_t AsyncDeviceRequest(IOService *forClient, uint8_t bmRequestType, uint8_t bRequest, uint16_t wValue, uint16_t wIndex, uint16_t wLength, IOMemoryDescriptor *dataBuffer, OSAction *completion, uint32_t completionTimeoutMs, OSDispatchMethod supermethod);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostdevice/3294607-asyncdevicerequest)*