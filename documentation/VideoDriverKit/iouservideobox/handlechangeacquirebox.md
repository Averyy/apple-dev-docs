# HandleChangeAcquireBox

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Called when host is attempting to the change the box acquisition

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeAcquireBox(bool in_acquire);
```

## Return Value

Kern_return_t inidicating if the change was successful, upon succes the value should be updated.

## Discussion

Default behavior will call SetIsAcquired() and return `kIOReturnSuccess`. Custom drivers should override this method and validate the change and return `kIOReturnSuccess` to confirm the change

## See Also

### Managing acquirability
- [SetIsAcquired](./setisacquired.md)
  Sets the value indicating the box’s acquisition state.
- [IsAcquired](./isacquired.md)
  A Boolean value indicating if box is acquired.
- [SetIsAcquirable](./setisacquirable.md)
  Sets the value for the box’s acquirability.
- [IsAcquirable](./isacquirable.md)
  A Boolean value indicating if box can be acquired.
- [SetAcquisitionFailure](./setacquisitionfailure.md)
  Sets the error for the box’s acquisition failure.
- [GetAcquisitionFailure](./getacquisitionfailure.md)
  Gets the acquisition failure of the video box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/handlechangeacquirebox)*