# DeviceRequest

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Sends a synchronous request to the device on the default control endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t DeviceRequest(IOService *forClient, uint8_t bmRequestType, uint8_t bRequest, uint16_t wValue, uint16_t wIndex, uint16_t wLength, IOMemoryDescriptor *dataBuffer, uint16_t *bytesTransferred, uint32_t completionTimeoutMs);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

This method acquires the service’s workloop lock and performs a USB device request (USB 2.0, section 9.3). The method waits for the request to complete, and may call [`commandSleep`](../../kernel/iocommandgate/api-1573818-commandsleep.md) during that time.

## Parameters

- `bmRequestType`: The characteristics of the device request. See the [`USBmakebmRequestType`](../../iokit/usbmakebmrequesttype.md) macro for information about how to construct this request.
- `bRequest`: The request you want to make.
- `wValue`: Request-specific data.
- `wIndex`: Request-specific data.
- `wLength`: The number of bytes to transfer, if there’s a data stage.
- `dataBuffer`: The memory descriptor to use for the request’s data phase, if any.
- `bytesTransferred`: A pointer to a variable. On return, this variable contains the number of bytes that the method actually transferred during the data phase.
- `completionTimeoutMs`: The timeout duration in milliseconds. If you specify `0`, the request never times out.

## See Also

### Requesting Information from the Device
- [AsyncDeviceRequest](./asyncdevicerequest.md)
  Enqueues a request on the default control endpoint of the device.
- [CompleteAsyncDeviceRequest](./completeasyncdevicerequest.md)
  The type definition for an asynchronous device request completion routine.
- [AbortDeviceRequests](./abortdevicerequests.md)
  Aborts device requests that you made previously from the current device client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/devicerequest)*