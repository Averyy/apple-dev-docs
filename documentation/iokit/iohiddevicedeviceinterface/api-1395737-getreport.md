# getReport

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains a report of type kIOHIDReportTypeInput or kIOHIDReportTypeFeature from the IOHIDDevice.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*getReport)(void *self, IOHIDReportType reportType, uint32_t reportID, uint8_t *report, CFIndex *pReportLength, uint32_t timeout, IOHIDReportCallback callback, void *context, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

#### Discussion

This method is useful if specific knowledge of the unparsed report is known to the caller. Otherwise, using an IOHIDDeviceTransactionInterface with the kIOHIDTransactionDirectionTypeInput direction is recommended.

**Note:** In order to make use of asynchronous behavior, the event source obtained using getAsyncEventSource must be added to a run loop.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `reportType`: The report type.
- `reportID`: The report id.
- `report`: Pointer to a pre-allocated buffer to be filled.
- `reportLength`: Length of the report buffer. When finished, this will contain the actual length of the report.
- `timeout`: Timeout in milliseconds for issuing the getReport.
- `callback`: Callback of type IOHIDReportCallback to be used when report data has been received from the device. If null, this method will behave synchronously.
- `context`: Pointer to data to be passed to the callback.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395737-getreport)*