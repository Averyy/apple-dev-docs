# RemoveClockDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveClockDevice(IOUserVideoClockDevice *in_clock_device);
```

#### Return Value

Returns kIOReturnSuccess if clock device was successfully removed.

#### Discussion

Remove a IOUserVideoClockDevice from the IOUserVideoBox.

The clock device’s reference count will be decremented if it was successfully removed.

## Parameters

- `in_clock_device`: IOUserVideoClockDevice associated with the box.

## See Also

- [AddDevice](iouservideobox/adddevice.md)
- [RemoveDevice](iouservideobox/removedevice.md)
- [IOUserVideoDevice](iouservideodevice.md)
- [AddClockDevice](iouservideobox/addclockdevice.md)
- [IOUserVideoClockDevice](iouservideoclockdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/removeclockdevice)*