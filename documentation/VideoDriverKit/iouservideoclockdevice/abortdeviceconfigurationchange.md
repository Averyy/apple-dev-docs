# AbortDeviceConfigurationChange

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t AbortDeviceConfigurationChange(uint64_t change_action, OSObject *in_change_info);
```

#### Return Value

Returns kern_return_t

#### Discussion

This is called by the Host to tell the driver not to perform a configuration change that had been requested via a call to the Host method, RequestDeviceConfigurationChange(). Subclass and override this method to handle any aborted custom configuration change requests, then call super class to update state.

## Parameters

- `in_change_info`: A pointer to an OSObject  about the configuration change. This is the same value that was passed to RequestDeviceConfigurationChange(). Note that this value is purely for the driver’s usage. The Host does not look at this value.  Object reference should be retained/released as necessary.

## See Also

- [PerformDeviceConfigurationChange](iouservideoclockdevice/performdeviceconfigurationchange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/abortdeviceconfigurationchange)*