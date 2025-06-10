# CurrentMicroframe

**Framework**: USBDriverKit  
**Kind**: method

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t CurrentMicroframe(uint64_t * microframeNumber, uint64_t * theTime);
```

#### Return Value

KERN_SUCCESS is successful see IOReturn.h for error codes.

#### Discussion

This method will return the current microframe number of the USB controller This is most useful for scheduling future isochronous requests.

## Parameters

- `microframeNumber`: uint64_t pointer to be updated with the current microframe number
- `theTime`: If not NULL, this will be updated with the system time assosiated with the returned microframe


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/currentmicroframe)*