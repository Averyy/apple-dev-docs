# GetAcquisitionFailure

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t GetAcquisitionFailure();
```

#### Return Value

Returns kern_return_t.

#### Discussion

Get the acquisition failure of the IOUserVideoBox. Getting the value will be synchronized using the work queue created by the object.

## See Also

- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
- [SetIsAcquired](iouservideobox/setisacquired.md)
- [IsAcquired](iouservideobox/isacquired.md)
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
- [IsAcquirable](iouservideobox/isacquirable.md)
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/getacquisitionfailure)*