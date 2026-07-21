# SetAcquisitionFailure

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetAcquisitionFailure(kern_return_t in_failure_code);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the error for the box’s acquisition failure.

A notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## See Also

- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
- [SetIsAcquired](iouservideobox/setisacquired.md)
- [IsAcquired](iouservideobox/isacquired.md)
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
- [IsAcquirable](iouservideobox/isacquirable.md)
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setacquisitionfailure)*