# setInterruptReportHandlerCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the report handler callout to be called when the data is received from the Interrupt-In pipe.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn (*setInterruptReportHandlerCallback)(void *self, void *reportBuffer, uint32_t reportBufferSize, IOHIDReportCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

## Return Value

Returns an IOReturn code.

## Discussion

In order for this to work correctly, you must call createAsyncPort and createAsyncEventSource.

## Parameters

- `reportBuffer`: Pointer to a preallocated buffer.
- `reportBufferSize`: Size of the reportBuffer in bytes.
- `callback`: If non-NULL, is a callback to be called when data is received from the device.
- `callbackTarget`: The callback target passed to the callback
- `callbackRefcon`: The callback refcon passed to the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface122/1493280-setinterruptreporthandlercallbac)*