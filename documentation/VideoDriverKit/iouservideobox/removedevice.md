# RemoveDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveDevice(IOUserVideoDevice *in_device);
```

#### Return Value

Returns kIOReturnSuccess if device was successfully removed.

#### Discussion

Remove a IOUserVideoDevice from the IOUserVideoBox.

Remove a IOUserVideoDevice from the IOUserVideoBox. The device’s reference count will be decremented if it was successfully removed.

## Parameters

- `in_device`: IOUserVideoDevice associated with the box.

## See Also

- [AddDevice](iouservideobox/adddevice.md)
- [IOUserVideoDevice](iouservideodevice.md)
- [AddClockDevice](iouservideobox/addclockdevice.md)
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
- [IOUserVideoClockDevice](iouservideoclockdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/removedevice)*