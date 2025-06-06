# SetConfiguration

**Framework**: USBDriverKit  
**Kind**: method

Selects a new configuration for the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t SetConfiguration(uint8_t bConfigurationValue, bool matchInterfaces);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method terminates all previously configured child interfaces and sets the new configuration for the device. This method sends a `SET_CONFIGURATION` control request (USB 2.0, section 9.4.7) to the device. When making the `GET_DESCRIPTOR` control request, this method acquires the service’s workloop lock and may call [`commandSleep`](https://developer.apple.com/documentation/kernel/iocommandgate/1573818-commandsleep).

## Parameters

- `bConfigurationValue`: The configuration to select. You can get this value from the   field of the   structure.
- `matchInterfaces`: A Boolean value indicating whether you want the system to perform matching on the interfaces of the new configuration. Specify   to skip the matching process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/setconfiguration)*