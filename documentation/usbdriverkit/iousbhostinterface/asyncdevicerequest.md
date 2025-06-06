# AsyncDeviceRequest

**Framework**: USBDriverKit  
**Kind**: method

Enqueues a request on the default control endpoint of the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t AsyncDeviceRequest(uint8_t bmRequestType, uint8_t bRequest, uint16_t wValue, uint16_t wIndex, uint16_t wLength, IOMemoryDescriptor * dataBuffer, OSAction * completion, uint32_t completionTimeoutMs);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) if the request was enqueued successfully, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method performs a USB device request (USB 2.0, section 9.3) asynchronously on the default control endpoint. After enqueueing the request, this method returns immediately. If the request was enqueued successfully, the system executes the action in the `completion` parameter after the request finishes.

## Parameters

- `bmRequestType`: The characteristics of the device request. See the   macro for information about how to construct this request.
- `bRequest`: The request you want to make.
- `wValue`: Request-specific data.
- `wIndex`: Request-specific data.
- `wLength`: The number of bytes to transfer, if there’s a data stage.
- `dataBuffer`: The memory descriptor to use for the request’s data phase, if any.
- `completion`: An   object that contains the method to call when the request finishes.
- `completionTimeoutMs`: The timeout duration in milliseconds. If you specify  , the request never times out.

## See Also

- [DeviceRequest](iousbhostinterface/devicerequest.md)
  Sends a synchronous request to the device on the default control endpoint.
- [AbortDeviceRequests](iousbhostinterface/abortdevicerequests.md)
  Aborts device requests that you made previously from the current interface client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/asyncdevicerequest)*