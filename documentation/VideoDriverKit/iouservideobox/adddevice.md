# AddDevice

**Framework**: VideoDriverKit  
**Kind**: method

Adds a video device to the video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t AddDevice(IOUserVideoDevice *in_device);
```

#### Return Value

`kIOReturnSuccess` if device was successfully added.

#### Discussion

The box doesn’t own the device. The device’s reference count will be incremented if it was successfully added.

## Parameters

- `in_device`: IOUserVideoDevice associated with the box.

## See Also

- [RemoveDevice](iouservideobox/removedevice.md)
  Removes a video device from the video box.
- [IOUserVideoDevice](iouservideodevice.md)
  A video device.
- [AddClockDevice](iouservideobox/addclockdevice.md)
  Adds a clock device video box.
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
  Removes aa clock device from the video box.
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
  A clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/adddevice)*