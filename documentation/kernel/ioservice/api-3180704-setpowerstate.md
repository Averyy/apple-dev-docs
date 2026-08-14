# SetPowerState

**Framework**: Kernel  
**Kind**: instm

Updates the service in response to power-related changes for a provider.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
kern_return_t SetPowerState(uint32_t powerFlags, OSDispatchMethod supermethod);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

#### Discussion

DriverKit calls this method to notify your service when the power state of its provider changes. Implement this method in your service object and use it to put your driver in a safe state for the new power setting. Call `super` as the last step in your implementation. 

## Parameters

- `powerFlags`: The new power state for the service's provider object. Configure your driver appropriately for the new state. For a list of possible values, see [`Service Power Capabilities`](https://developer.apple.com/documentation/driverkit/3325571-service_power_capabilities).

## See Also

- [- ChangePowerState](ioservice/3180692-changepowerstate.md)
  Changes the device's power state to the specified level.
- [Service Power Capabilities](../driverkit/3325571-service_power_capabilities.md)
  Constants that indicate the power state of a device. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180704-setpowerstate)*