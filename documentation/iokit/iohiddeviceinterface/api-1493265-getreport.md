# getReport

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*getReport)(void *self, IOHIDReportType reportType, uint32_t reportID, void *reportBuffer, uint32_t *reportBufferSize, uint32_t timeoutMS, IOHIDReportCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface/1493265-getreport)*