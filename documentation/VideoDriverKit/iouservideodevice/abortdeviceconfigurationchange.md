# AbortDeviceConfigurationChange

**Framework**: VideoDriverKit  
**Kind**: method

The host calls this method to tell the driver not to perform a configuration change it requested by calling RequestDeviceConfigurationChange(). Subclass and override this method to handle any aborted custom configuration change requests. Then call the superclass implementation to update state.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t AbortDeviceConfigurationChange(uint64_t in_change_action, OSObject *in_change_info);
```

#### Return Value

A kern_return_t value indicating success or failure.

## Parameters

- `in_change_action`: A uint64_t indicating the action the device object wants to take. This is the same value passed to RequestDeviceConfigurationChange(). Note that this value is purely for the driver’s usage. The host does not look at this value.
- `in_change_info`: A pointer to an OSObject about the configuration change. This is the same value passed to RequestDeviceConfigurationChange(). Note that this value is purely for the driver’s usage. The host does not look at this value. Retain or release the object reference as necessary.

## See Also

- [PerformDeviceConfigurationChange](iouservideodevice/performdeviceconfigurationchange.md)
  The host calls this method to allow the device to perform a configuration change it previously requested by calling RequestDeviceConfigurationChange(), or a change to an IO state that requires a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/abortdeviceconfigurationchange)*