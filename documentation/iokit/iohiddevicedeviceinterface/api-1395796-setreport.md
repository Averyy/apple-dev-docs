# setReport

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sends a report of type kIOHIDReportTypeOutput or kIOHIDReportTypeFeature to the IOHIDDevice.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*setReport)(void *self, IOHIDReportType reportType, uint32_t reportID, const uint8_t *report, CFIndex reportLength, uint32_t timeout, IOHIDReportCallback callback, void *context, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

This method is useful if specific knowledge of the unparsed report is known to the caller. Otherwise, using an IOHIDDeviceTransactionInterface with the kIOHIDTransactionDirectionTypeOutput direction is recommended.

**Note:** In order to make use of asynchronous behavior, the event source obtained using getAsyncEventSource must be added to a run loop.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `reportType`: The report type.
- `reportID`: The report id.
- `report`: Pointer to a buffer containing the report data to be sent.
- `reportLength`: Length of the report buffer.
- `timeout`: Timeout in milliseconds for issuing the setReport.
- `callback`: Callback of type IOHIDReportCallback to be used after report data has been sent to the device. If null, this method will behave synchronously.
- `context`: Pointer to data to be passed to the callback.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395796-setreport)*