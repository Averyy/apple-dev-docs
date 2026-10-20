# GetDeviceIsAlive

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets a Boolean value indicating if the device is alive.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
bool GetDeviceIsAlive();
```

#### Discussion

The object’s work queue synchronizes access to the value. The default value is true when the device is created.

## See Also

### Working with clock device state
- [GetDeviceIsRunning](./getdeviceisrunning.md)
  Gets bool value indicating if device is running.
- [SetDeviceIsAlive](./setdeviceisalive.md)
  Sets a Boolean value to indicate the device is alive.
- [SetIsHidden](./setishidden.md)
  Sets a Boolean value indicating if the device is hidden.
- [GetIsHidden](./getishidden.md)
  Gets a Boolean value indicating if the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getdeviceisalive)*