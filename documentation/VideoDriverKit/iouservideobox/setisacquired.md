# SetIsAcquired

**Framework**: VideoDriverKit  
**Kind**: method

Sets the value indicating the box’s acquisition state.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetIsAcquired(bool in_is_acquired);
```

#### Discussion

The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## Parameters

- `in_is_acquired`: The box’s acquisition state.

## See Also

- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
  Called when host is attempting to the change the box acquisition
- [IsAcquired](iouservideobox/isacquired.md)
  A Boolean value indicating if box is acquired.
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
  Sets the value for the box’s acquirability.
- [IsAcquirable](iouservideobox/isacquirable.md)
  A Boolean value indicating if box can be acquired.
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
  Sets the error for the box’s acquisition failure.
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)
  Gets the acquisition failure of the video box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setisacquired)*