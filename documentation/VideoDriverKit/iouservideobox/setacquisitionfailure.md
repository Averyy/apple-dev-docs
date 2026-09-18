# SetAcquisitionFailure

**Framework**: VideoDriverKit  
**Kind**: method

Sets the error for the box’s acquisition failure.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetAcquisitionFailure(kern_return_t in_failure_code);
```

#### Discussion

The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

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
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)
  Gets the acquisition failure of the video box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setacquisitionfailure)*