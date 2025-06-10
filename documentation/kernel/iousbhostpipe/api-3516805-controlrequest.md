# controlRequest

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+ - Deprecated in 10.15.4

## Declaration

```swift
virtual IOReturn controlRequest(IOService *forClient, StandardUSB::DeviceRequest & request, IOMemoryDescriptor *dataBuffer, uint32_t & bytesTransferred, uint32_t completionTimeoutMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostpipe/3516805-controlrequest)*