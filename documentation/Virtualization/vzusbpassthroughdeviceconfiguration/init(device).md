# init(device:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(device: AAUSBAccessory)
```

```objc
- (instancetype) initWithDevice:(AAUSBAccessory *) device;
```

## Return Value

An initialized VZUSBPassthroughDeviceConfiguration.

## Discussion

Initialize a passthrough USB device configuration.

Initialize a passthrough USB device configuration from an AccessoryAccess framework device.

## Parameters

- `device`: The AccessoryAccess framework object to be captured by the virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbpassthroughdeviceconfiguration/init(device:))*