# getReport

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains a report from the device.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn (*getReport)(void *self, IOHIDReportType reportType, uint32_t reportID, void *reportBuffer, uint32_t *reportBufferSize, uint32_t timeoutMS, IOHIDReportCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

## Return Value

Returns an IOReturn code.

## Parameters

- `reportType`: The report type.
- `reportID`: The report ID.
- `reportBuffer`: Pointer to a preallocated buffer.
- `reportBufferSize`: Size of the reportBuffer in bytes. When finished, will contain the actual size of the report.
- `timeoutMS`: 
- `callback`: If null, this method will behave synchronously.
- `callbackTarget`: The callback target passed to the callback.
- `callbackRefcon`: The callback refcon passed to the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface121/1493257-getreport)*