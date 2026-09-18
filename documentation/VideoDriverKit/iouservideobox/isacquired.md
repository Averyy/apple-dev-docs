# IsAcquired

**Framework**: VideoDriverKit  
**Kind**: method

A Boolean value indicating if box is acquired.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
bool IsAcquired();
```

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
  Called when host is attempting to the change the box acquisition
- [SetIsAcquired](iouservideobox/setisacquired.md)
  Sets the value indicating the box’s acquisition state.
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
  Sets the value for the box’s acquirability.
- [IsAcquirable](iouservideobox/isacquirable.md)
  A Boolean value indicating if box can be acquired.
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
  Sets the error for the box’s acquisition failure.
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)
  Gets the acquisition failure of the video box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/isacquired)*