# HandleChangeAcquireBox

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeAcquireBox(bool in_acquire);
```

#### Return Value

Returns kern_return_t inidicating if the change was successful, upon succes the value should be updated.

#### Discussion

Called when host is attempting to the change the box acquisition

Default behavior will call SetIsAcquired() and return kIOReturnSuccess. Custom drivers should override this method and validate the change and return kIOReturnSuccess to confirm the change

## See Also

- [SetIsAcquired](iouservideobox/setisacquired.md)
- [IsAcquired](iouservideobox/isacquired.md)
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
- [IsAcquirable](iouservideobox/isacquirable.md)
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/handlechangeacquirebox)*