# internalDeviceRequest

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+ - Deprecated in 10.15.4

## Declaration

```swift
virtual IOReturn internalDeviceRequest(IOService *forClient, StandardUSB::DeviceRequest & request, void *rawBuffer, IOMemoryDescriptor *descriptorBuffer, uint32_t & bytesTransferred, IOUSBHostCompletion *completion, uint32_t completionTimeoutMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostdevice/1543490-internaldevicerequest)*