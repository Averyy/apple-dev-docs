# SetIsAcquired

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIsAcquired(bool in_is_acquired);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the value indicating the box’s acquisition state

A notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_is_acquired`: Bool value for the box’s acquisition state

## See Also

- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
- [IsAcquired](iouservideobox/isacquired.md)
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
- [IsAcquirable](iouservideobox/isacquirable.md)
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setisacquired)*