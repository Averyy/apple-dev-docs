# AddClockDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddClockDevice(IOUserVideoClockDevice *in_clock_device);
```

#### Return Value

Returns kIOReturnSuccess if device was successfully added.

#### Discussion

Add a IOUserVideoClockDevice to the IOUserVideoBox

The box does not own the clock device. The clock device’s reference count will be incremented if it was successfully added.

## Parameters

- `in_clock_device`: IOUserVideoClockDevice associated with the box.

## See Also

- [AddDevice](iouservideobox/adddevice.md)
- [RemoveDevice](iouservideobox/removedevice.md)
- [IOUserVideoDevice](iouservideodevice.md)
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
- [IOUserVideoClockDevice](iouservideoclockdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/addclockdevice)*