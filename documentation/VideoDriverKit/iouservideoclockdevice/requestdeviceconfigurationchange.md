# RequestDeviceConfigurationChange

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RequestDeviceConfigurationChange(uint64_t in_change_action, OSObject *in_change_info);
```

#### Return Value

Returns kern_return_t indicating success or failure.

#### Discussion

Drivers invoke this routine to tell the host to initiate a configuration change operation.

When a video device object needs to change its structure or change any state related to IO for any reason, it must begin this operation by invoking this Host method. The device object may not perform the state change until the Host gives the device clearance to do so by invoking the PerformDeviceConfigurationChange() routine. Note that the call to PerformDeviceConfigurationChange() may be deferred to another thread at the discretion of the host.

The sorts of changes that must go through this mechanism are anything that affects either the structure of the device or IO. This includes, but is not limited to, changing stream layout, adding/removing controls, changing the nominal sample rate of the device, changing any sample formats on any stream on the device, changing the size of the ring buffer, changing presentation latency, and changing the safety offset.

## Parameters

- `in_change_action`: A uint64_t indicating the action the device object wants to take. It will be passed back to the device in the invocation of PerformDeviceConfigurationChange(). Note that this value is purely for driver’s usage. The Host does not look at this value.
- `in_change_info`: A pointer to an OSObject about the configuration change, can be nullptr. Note that this value is purely for the driver’s usage. The Host does not look at this value.  Object reference should be retained/released as necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/requestdeviceconfigurationchange)*