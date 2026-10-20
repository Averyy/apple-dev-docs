# ChangePowerState

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Changes the device's power state to the specified level.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual kern_return_t ChangePowerState(uint32_t powerFlags);
```

*macOS*

```cpp
kern_return_t ChangePowerState(uint32_t powerFlags, OSDispatchMethod supermethod);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md). 

#### Discussion

If the new state is different than the device's current state, this method places an asynchronous request to change the state to the new value. If the change is successful, the system subsequently calls the [`SetPowerState`](./api-3180704-setpowerstate.md) method of your service. 

## Parameters

- `powerFlags`: The new power state for the device. Typically, you specify only [`kIOServicePowerCapabilityLow`](../../DriverKit/kioservicepowercapabilitylow.md) for this parameter. For a list of all possible values, see [Service Power Capabilities](../../DriverKit/api-3325571-service_power_capabilities.md).

## See Also

### Responding to Power-Level Changes
- [- SetPowerState](./api-3180704-setpowerstate.md)
  Updates the service in response to power-related changes for a provider.
- [Service Power Capabilities](../../DriverKit/api-3325571-service_power_capabilities.md)
  Constants that indicate the power state of a device. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180692-changepowerstate)*