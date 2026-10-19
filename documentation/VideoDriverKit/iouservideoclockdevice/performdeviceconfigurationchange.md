# PerformDeviceConfigurationChange

**Framework**: VideoDriverKit  
**Kind**: method

The host calls this method to allow the clock device to perform a configuration change.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t PerformDeviceConfigurationChange(uint64_t change_action, OSObject *in_change_info);
```

#### Discussion

The configuration change is one that had been previously requested via a call to the host via `RequestDeviceConfigChange` or a change to an IO state that requires a configuration change.

Subclass and override this method to handle any custom configuration change requests, then call the superclass implementation to update state. IO will be stopped prior to the performing the configuration change.

## Parameters

- `change_action`: The action the device object wants to take. This is the same value that was passed to `RequestDeviceConfigurationChange()`. Note that this value is purely for the driver’s usage. The host doesn’t look at this value.
- `in_change_info`: A pointer to an `OSObject` about the configuration change. This is the same value that was passed to `RequestDeviceConfigurationChange()`. Note that this value is purely for the driver’s usage. The host doesn’t look at this value. Object reference should be retained/released as necessary.

## See Also

- [AbortDeviceConfigurationChange](iouservideoclockdevice/abortdeviceconfigurationchange.md)
  The host calls this method to tell the driver not to perform a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/performdeviceconfigurationchange)*