# controlRequest

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+ - Deprecated in 10.15.4

## Declaration

```swift
virtual IOReturn controlRequest(IOService *forClient, StandardUSB::DeviceRequest & request, void *dataBuffer, IOUSBHostCompletion *completion, uint32_t completionTimeoutMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostpipe/1584489-controlrequest)*