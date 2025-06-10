# deviceRequest

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+ - Deprecated in 10.15.4

## Declaration

```swift
virtual IOReturn deviceRequest(IOService *forClient, StandardUSB::DeviceRequest & request, IOMemoryDescriptor *dataBuffer, uint32_t & bytesTransferred, uint32_t completionTimeoutMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostdevice/3516785-devicerequest)*