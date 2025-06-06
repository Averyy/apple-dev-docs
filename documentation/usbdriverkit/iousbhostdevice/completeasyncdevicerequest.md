# CompleteAsyncDeviceRequest

**Framework**: USBDriverKit  
**Kind**: method

The type definition for an asynchronous device request completion routine.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void CompleteAsyncDeviceRequest(OSAction * action, IOReturn status, uint32_t bytesTransferred);
```

#### Discussion

Implement a custom version of this method and use the [`TYPE`](https://developer.apple.com/documentation/DriverKit/TYPE) macro to let the system know that your method conforms to this prototype.

## Parameters

- `action`: A pointer to the   object of the async request.
- `status`: The result of the operation.
- `bytesTransferred`: The byte count of the completed data phase.

## See Also

- [DeviceRequest](iousbhostdevice/devicerequest.md)
  Sends a synchronous request to the device on the default control endpoint.
- [AsyncDeviceRequest](iousbhostdevice/asyncdevicerequest.md)
  Enqueues a request on the default control endpoint of the device.
- [AbortDeviceRequests](iousbhostdevice/abortdevicerequests.md)
  Aborts device requests that you made previously from the current device client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/completeasyncdevicerequest)*