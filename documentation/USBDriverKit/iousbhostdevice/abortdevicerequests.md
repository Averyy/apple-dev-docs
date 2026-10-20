# AbortDeviceRequests

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Aborts device requests that you made previously from the current device client.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t AbortDeviceRequests(IOService *forClient, IOOptionBits options, IOReturn withError);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Use this method to abort any requests you made previously with the [`AsyncDeviceRequest`](./asyncdevicerequest.md) method. This method aborts only the requests that the current device object initiated.

## Parameters

- `forClient`: The client that issued the requests.
- `options`: Options to use when aborting requests. Specify `0` for this parameter.
- `withError`: The error value to report for each request. Specify `kIOReturnAborted` for this parameter.

## See Also

### Requesting Information from the Device
- [DeviceRequest](./devicerequest.md)
  Sends a synchronous request to the device on the default control endpoint.
- [AsyncDeviceRequest](./asyncdevicerequest.md)
  Enqueues a request on the default control endpoint of the device.
- [CompleteAsyncDeviceRequest](./completeasyncdevicerequest.md)
  The type definition for an asynchronous device request completion routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/abortdevicerequests)*