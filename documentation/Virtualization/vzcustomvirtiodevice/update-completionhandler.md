# update(_:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Updates the device’s device-specific configuration.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func update(_ newConfiguration: VZVirtioDeviceSpecificConfiguration) async throws
```

#### Discussion

The size of the underlying data for the new configuration must be the same as the previous configuration. The framework raises an exception if this condition isn’t met.

## Parameters

- `newConfiguration`: The [`VZVirtioDeviceSpecificConfiguration`](vzvirtiodevicespecificconfiguration.md) object that contains the new configuration data.
- `completionHandler`: A block the framework calls after the device’s configuration updates successfully, or on error. The error parameter the framework passes to the block is `nil` if the configuration update was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/update(_:completionhandler:))*