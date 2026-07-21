# PerformDeviceConfigurationChange

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t PerformDeviceConfigurationChange(uint64_t in_change_action, OSObject *in_change_info);
```

#### Return Value

Returns kern_return_t

#### Discussion

This is called by the host to allow the device to perform a configuration change that had been previously requested via a call to the host via RequestDeviceConfigChange or a change to an IO state that requires a configuration change

Subclass and override this method to handle any custom configuration change requests, then call super class to update state. IO will be stopped prior to the performing the configuration change.

## Parameters

- `in_change_action`: A uint64_t indicating the action the device object wants to take. This is the same value that was passed to RequestDeviceConfigurationChange(). Note that this value is purely for the driver’s usage. The host does not look at this value.
- `in_change_info`: A pointer to an OSObject  about the configuration change. This is the same value that was passed to RequestDeviceConfigurationChange(). Note that this value is purely for the driver’s usage. The Host does not look at this value.  Object reference should be retained/released as necessary.

## See Also

- [AbortDeviceConfigurationChange](iouservideodevice/abortdeviceconfigurationchange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/performdeviceconfigurationchange)*