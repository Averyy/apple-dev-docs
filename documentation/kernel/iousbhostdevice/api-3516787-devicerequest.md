# deviceRequest

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.15.2+ - Deprecated in 10.15.4

## Declaration

```cpp
virtual IOReturn deviceRequest(IOService *forClient, StandardUSB::DeviceRequest & request, void *dataBuffer, uint32_t & bytesTransferred, uint32_t completionTimeoutMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostdevice/3516787-devicerequest)*