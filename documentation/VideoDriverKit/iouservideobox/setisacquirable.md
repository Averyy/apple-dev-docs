# SetIsAcquirable

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIsAcquirable(bool in_is_acquirable);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the value for the box’s acquirability

A notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_is_acquirable`: Bool value for the box’s acquirability state

## See Also

- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
- [SetIsAcquired](iouservideobox/setisacquired.md)
- [IsAcquired](iouservideobox/isacquired.md)
- [IsAcquirable](iouservideobox/isacquirable.md)
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setisacquirable)*