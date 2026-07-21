# AddControl

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddControl(IOUserVideoControl *in_control);
```

#### Return Value

Returns kIOReturnSuccess if control was successfully added.

#### Discussion

Add a IOUserVideoControl to the IOUserVideoClockDevice

The control’s reference count will be incremented if it was successfully added to the clock device.

## Parameters

- `in_control`: IOUserVideoControl to add to the clock device.

## See Also

- [RemoveControl](iouservideoclockdevice/removecontrol.md)
- [IOUserVideoControl](iouservideocontrol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/addcontrol)*