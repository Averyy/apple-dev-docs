# VZCustomVirtioDeviceConfigurationDelegate

**Framework**: Virtualization  
**Kind**: protocol

A class that conforms to the custom Virtio device configuration delegate protocol that can provide methods for tracking the state of a custom Virtio device configuration object.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol VZCustomVirtioDeviceConfigurationDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func customVirtioConfiguration(VZCustomVirtioDeviceConfiguration, didCreateDevice: VZCustomVirtioDevice)](vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration(_:didcreatedevice:).md)
  A method the framework calls when it creates a custom Virtio device from a custom Virtio device configuration.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol VZCustomVirtioDeviceDelegate](vzcustomvirtiodevicedelegate.md)
  A delegate protocol that defines the methods you implement to respond to the life cycle events of a custom Virtio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfigurationdelegate)*