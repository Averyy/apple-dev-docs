# setReport

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn (*setReport)(void *self, IOHIDReportType reportType, uint32_t reportID, void *reportBuffer, uint32_t reportBufferSize, uint32_t timeoutMS, IOHIDReportCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface122/1493378-setreport)*