# GetAcquisitionFailure

**Framework**: VideoDriverKit  
**Kind**: method

Gets the acquisition failure of the video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t GetAcquisitionFailure();
```

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
  Called when host is attempting to the change the box acquisition
- [SetIsAcquired](iouservideobox/setisacquired.md)
  Sets the value indicating the box’s acquisition state.
- [IsAcquired](iouservideobox/isacquired.md)
  A Boolean value indicating if box is acquired.
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
  Sets the value for the box’s acquirability.
- [IsAcquirable](iouservideobox/isacquirable.md)
  A Boolean value indicating if box can be acquired.
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
  Sets the error for the box’s acquisition failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/getacquisitionfailure)*