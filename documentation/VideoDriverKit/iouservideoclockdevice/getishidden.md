# GetIsHidden

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets a Boolean value indicating if the device is hidden.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
bool GetIsHidden();
```

## Discussion

The object’s work queue synchronizes access to the value. The default value is false when the device is created.

## See Also

### Working with clock device state
- [GetDeviceIsRunning](./getdeviceisrunning.md)
  Gets bool value indicating if device is running.
- [SetDeviceIsAlive](./setdeviceisalive.md)
  Sets a Boolean value to indicate the device is alive.
- [GetDeviceIsAlive](./getdeviceisalive.md)
  Gets a Boolean value indicating if the device is alive.
- [SetIsHidden](./setishidden.md)
  Sets a Boolean value indicating if the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getishidden)*