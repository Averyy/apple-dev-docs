# setReport

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sends a report to the device.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn (*setReport)(void *self, IOHIDReportType reportType, uint32_t reportID, void *reportBuffer, uint32_t reportBufferSize, uint32_t timeoutMS, IOHIDReportCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

## Return Value

Returns an IOReturn code.

## Parameters

- `reportType`: The report type.
- `reportID`: The report id.
- `reportBuffer`: Pointer to a preallocated buffer.
- `reportBufferSize`: Size of the reportBuffer in bytes.
- `timeoutMS`: 
- `callback`: If null, this method will behave synchronously.
- `callbackTarget`: The callback target passed to the callback.
- `callbackRefcon`: The callback refcon passed to the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface121/1493282-setreport)*