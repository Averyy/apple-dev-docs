# RemoveClockDevice

**Framework**: VideoDriverKit  
**Kind**: method

Removes aa clock device from the video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t RemoveClockDevice(IOUserVideoClockDevice *in_clock_device);
```

#### Return Value

`kIOReturnSuccess` if clock device was successfully removed.

#### Discussion

The clock device’s reference count will be decremented if it was successfully removed.

## Parameters

- `in_clock_device`: IOUserVideoClockDevice associated with the box.

## See Also

- [AddDevice](iouservideobox/adddevice.md)
  Adds a video device to the video box.
- [RemoveDevice](iouservideobox/removedevice.md)
  Removes a video device from the video box.
- [IOUserVideoDevice](iouservideodevice.md)
  A video device.
- [AddClockDevice](iouservideobox/addclockdevice.md)
  Adds a clock device video box.
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
  A clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/removeclockdevice)*