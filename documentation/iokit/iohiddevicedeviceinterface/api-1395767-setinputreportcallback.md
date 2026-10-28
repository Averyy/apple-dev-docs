# setInputReportCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the input report callback to be used when data is received from the Input pipe.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*setInputReportCallback)(void *self, uint8_t *report, CFIndex reportLength, IOHIDReportCallback callback, void *context, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

In order to function properly, the event source obtained using getAsyncEventSource must be added to a run loop.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `report`: Pointer to a pre-allocated buffer to be filled and passed back via the callback.
- `reportLength`: Length of the report buffer.
- `callback`: Callback of type IOHIDReportCallback to be used when report data has been receieved by the IOHIDDevice.
- `context`: Pointer to data to be passed to the callback.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395767-setinputreportcallback)*