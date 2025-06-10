# ReferenceMicroframe

**Framework**: USBDriverKit  
**Kind**: method

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t ReferenceMicroframe(uint64_t * microframeNumber, uint64_t * theTime);
```

#### Return Value

KERN_SUCCESS is successful see IOReturn.h for error codes.

#### Discussion

This method will return a recent microframe number of the USB controller with a timestamp captured near the microframe boundary. This is most useful for scheduling future isochronous requests.

## Parameters

- `microframeNumber`: uint64_t pointer to be updated with the current frame number
- `theTime`: If not NULL, this will be updated with the system time assosiated with the returned microframe


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/referencemicroframe)*