# RemoveDevice

**Framework**: VideoDriverKit  
**Kind**: method

Removes a video device from the video box.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveDevice(IOUserVideoDevice *in_device);
```

#### Return Value

`kIOReturnSuccess` if device was successfully removed.

#### Discussion

The device’s reference count will be decremented if it was successfully removed.

## Parameters

- `in_device`: IOUserVideoDevice associated with the box.

## See Also

- [AddDevice](iouservideobox/adddevice.md)
  Adds a video device to the video box.
- [IOUserVideoDevice](iouservideodevice.md)
  A video device.
- [AddClockDevice](iouservideobox/addclockdevice.md)
  Adds a clock device video box.
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
  Removes aa clock device from the video box.
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
  A clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/removedevice)*