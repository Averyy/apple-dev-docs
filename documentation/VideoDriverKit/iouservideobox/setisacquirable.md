# SetIsAcquirable

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the value for the box’s acquirability.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetIsAcquirable(bool in_is_acquirable);
```

#### Discussion

The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## Parameters

- `in_is_acquirable`: The box’s acquirability state.

## See Also

### Managing acquirability
- [HandleChangeAcquireBox](./handlechangeacquirebox.md)
  Called when host is attempting to the change the box acquisition
- [SetIsAcquired](./setisacquired.md)
  Sets the value indicating the box’s acquisition state.
- [IsAcquired](./isacquired.md)
  A Boolean value indicating if box is acquired.
- [IsAcquirable](./isacquirable.md)
  A Boolean value indicating if box can be acquired.
- [SetAcquisitionFailure](./setacquisitionfailure.md)
  Sets the error for the box’s acquisition failure.
- [GetAcquisitionFailure](./getacquisitionfailure.md)
  Gets the acquisition failure of the video box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setisacquirable)*