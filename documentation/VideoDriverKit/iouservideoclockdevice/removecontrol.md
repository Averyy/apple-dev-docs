# RemoveControl

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveControl(IOUserVideoControl *in_control);
```

#### Return Value

Returns kIOReturnSuccess if control was successfully removed.

#### Discussion

Remove a IOUserVideoControl from the IOUserVideoClockDevice.

The control’s reference count will be decremented if it was successfully removed from the clock device.

## Parameters

- `in_control`: IOUserVideoControl to remove from the clock device.

## See Also

- [AddControl](iouservideoclockdevice/addcontrol.md)
- [IOUserVideoControl](iouservideocontrol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/removecontrol)*