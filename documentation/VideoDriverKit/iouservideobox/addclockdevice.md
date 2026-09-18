# AddClockDevice

**Framework**: VideoDriverKit  
**Kind**: method

Adds a clock device video box.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddClockDevice(IOUserVideoClockDevice *in_clock_device);
```

#### Return Value

`kIOReturnSuccess` if device was successfully added.

#### Discussion

The box doesn’t own the clock device. The clock device’s reference count will be incremented if it was successfully added.

## Parameters

- `in_clock_device`: IOUserVideoClockDevice associated with the box.

## See Also

- [AddDevice](iouservideobox/adddevice.md)
  Adds a video device to the video box.
- [RemoveDevice](iouservideobox/removedevice.md)
  Removes a video device from the video box.
- [IOUserVideoDevice](iouservideodevice.md)
  A video device.
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
  Removes aa clock device from the video box.
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
  A clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/addclockdevice)*