# AddControl

**Framework**: VideoDriverKit  
**Kind**: method

Adds a video control to the video clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t AddControl(IOUserVideoControl *in_control);
```

#### Return Value

`kIOReturnSuccess` if control was successfully added.

#### Discussion

The control’s reference count will be incremented if it was successfully added to the clock device.

## Parameters

- `in_control`: IOUserVideoControl to add to the clock device.

## See Also

- [RemoveControl](iouservideoclockdevice/removecontrol.md)
  Removes a user video control from the video clock device.
- [IOUserVideoControl](iouservideocontrol.md)
  A base class for control objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/addcontrol)*