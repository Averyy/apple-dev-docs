# CompleteAsyncIsochIO

**Framework**: USBDriverKit  
**Kind**: method

Handles the completion of an asynchronous request.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
virtual void CompleteAsyncIsochIO(OSAction *action, IOReturn status);
```

#### Discussion

Implement a custom version of this method and use the [`TYPE`](https://developer.apple.com/documentation/driverkit/type) macro to let the system know that your method conforms to this prototype.

## Parameters

- `action`: A pointer to the [`OSAction`](https://developer.apple.com/documentation/driverkit/osaction) object of the request.
- `status`: The result of the operation.

## See Also

- [IsochIO](iousbhostpipe/isochio.md)
  Performs a synchronous or asynchronous request on an isochronous endpoint.
- [IOUSBIsochronousFrame](iousbisochronousframe.md)
  A structure representing a single frame in an isochronous transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/completeasyncisochio)*