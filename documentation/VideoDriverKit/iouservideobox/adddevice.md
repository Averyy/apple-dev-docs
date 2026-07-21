# AddDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddDevice(IOUserVideoDevice *in_device);
```

#### Return Value

Returns kIOReturnSuccess if device was successfully added.

#### Discussion

Add a IOUserVideoDevice to the IOUserVideoBox

Add a IOUserVideoDevice to the IOUserVideoBox. The box does not own the device. The device’s reference count will be incremented if it was successfully added.

## Parameters

- `in_device`: IOUserVideoDevice associated with the box.

## See Also

- [RemoveDevice](iouservideobox/removedevice.md)
- [IOUserVideoDevice](iouservideodevice.md)
- [AddClockDevice](iouservideobox/addclockdevice.md)
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
- [IOUserVideoClockDevice](iouservideoclockdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/adddevice)*