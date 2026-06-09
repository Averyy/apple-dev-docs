# customVirtioConfiguration(_:didCreateDevice:)

**Framework**: Virtualization  
**Kind**: method

A method the framework calls when it creates a custom Virtio device from a custom Virtio device configuration.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioConfiguration(_ deviceConfiguration: VZCustomVirtioDeviceConfiguration, didCreateDevice device: VZCustomVirtioDevice)
```

#### Discussion

The Virtualization framework creates a [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md) when you call [`init(configuration:)`](vzvirtualmachine/init(configuration:).md) and calls this method on the serial queue of the guest’s [`VZVirtualMachine`](vzvirtualmachine.md) instance.

## Parameters

- `deviceConfiguration`: The configuration calling the delegate method.
- `device`: The [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md) that the framework created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration(_:didcreatedevice:))*