# deviceRequest

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+ - Deprecated in 10.15.4

## Declaration

```cpp
virtual IOReturn deviceRequest(StandardUSB::DeviceRequest & request, void *dataBuffer, IOUSBHostCompletion *completion, uint32_t completionTimeoutMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostinterface/1522092-devicerequest)*