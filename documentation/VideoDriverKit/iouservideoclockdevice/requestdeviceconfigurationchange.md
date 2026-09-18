# RequestDeviceConfigurationChange

**Framework**: VideoDriverKit  
**Kind**: method

Tells the host to initiate a configuration change operation.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RequestDeviceConfigurationChange(uint64_t in_change_action, OSObject *in_change_info);
```

#### Return Value

A kern_return_t value indicating success or failure.

#### Discussion

When a video device object needs to change its structure or change any state related to IO for any reason, it must begin this operation by invoking this Host method. The device object may not perform the state change until the Host gives the device clearance to do so by invoking the PerformDeviceConfigurationChange() routine. Note that the host may defer the call to PerformDeviceConfigurationChange() to another thread.

The sorts of changes that must go through this mechanism are anything that affects either the structure of the device or IO. This includes, but is not limited to, changing stream layout, adding/removing controls, changing the nominal sample rate of the device, changing any sample formats on any stream on the device, changing the size of the ring buffer, changing presentation latency, and changing the safety offset.

## Parameters

- `in_change_action`: A uint64_t indicating the action the device object wants to take. The host passes it back to the device when it invokes PerformDeviceConfigurationChange(). Note that this value is purely for the driver’s usage. The Host does not look at this value.
- `in_change_info`: A pointer to an OSObject about the configuration change, can be nullptr. Note that this value is purely for the driver’s usage. The Host does not look at this value. Retain or release the object reference as necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/requestdeviceconfigurationchange)*