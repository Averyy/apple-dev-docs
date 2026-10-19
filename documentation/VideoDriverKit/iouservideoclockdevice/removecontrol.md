# RemoveControl

**Framework**: VideoDriverKit  
**Kind**: method

Removes a user video control from the video clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t RemoveControl(IOUserVideoControl *in_control);
```

#### Return Value

`kIOReturnSuccess` if control was successfully removed.

#### Discussion

The control’s reference count will be decremented if it was successfully removed from the clock device.

## Parameters

- `in_control`: IOUserVideoControl to remove from the clock device.

## See Also

- [AddControl](iouservideoclockdevice/addcontrol.md)
  Adds a video control to the video clock device.
- [IOUserVideoControl](iouservideocontrol.md)
  A base class for control objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/removecontrol)*