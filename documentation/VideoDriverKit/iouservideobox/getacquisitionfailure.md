# GetAcquisitionFailure

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the acquisition failure of the video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t GetAcquisitionFailure();
```

## Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Managing acquirability
- [HandleChangeAcquireBox](./handlechangeacquirebox.md)
  Called when host is attempting to the change the box acquisition
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/getacquisitionfailure)*