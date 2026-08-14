# ChangePowerState

**Framework**: Kernel  
**Kind**: instm

Changes the device's power state to the specified level.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
kern_return_t ChangePowerState(uint32_t powerFlags, OSDispatchMethod supermethod);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

#### Discussion

If the new state is different than the device's current state, this method places an asynchronous request to change the state to the new value. If the change is successful, the system subsequently calls the [`SetPowerState`](ioservice/3180704-setpowerstate.md) method of your service. 

## Parameters

- `powerFlags`: The new power state for the device. Typically, you specify only [`kIOServicePowerCapabilityLow`](https://developer.apple.com/documentation/driverkit/kioservicepowercapabilitylow) for this parameter. For a list of all possible values, see [`Service Power Capabilities`](https://developer.apple.com/documentation/driverkit/3325571-service_power_capabilities).

## See Also

- [- SetPowerState](ioservice/3180704-setpowerstate.md)
  Updates the service in response to power-related changes for a provider.
- [Service Power Capabilities](../driverkit/3325571-service_power_capabilities.md)
  Constants that indicate the power state of a device. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180692-changepowerstate)*