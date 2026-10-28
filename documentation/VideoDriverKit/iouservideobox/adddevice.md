# AddDevice

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds a video device to the video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t AddDevice(IOUserVideoDevice *in_device);
```

## Return Value

`kIOReturnSuccess` if device was successfully added.

## Discussion

The box doesn’t own the device. The device’s reference count will be incremented if it was successfully added.

## Parameters

- `in_device`: IOUserVideoDevice associated with the box.

## See Also

### Managing box contents
- [RemoveDevice](./removedevice.md)
  Removes a video device from the video box.
- [IOUserVideoDevice](../iouservideodevice.md)
  A video device.
- [AddClockDevice](./addclockdevice.md)
  Adds a clock device video box.
- [RemoveClockDevice](./removeclockdevice.md)
  Removes aa clock device from the video box.
- [IOUserVideoClockDevice](../iouservideoclockdevice.md)
  A clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/adddevice)*