# delegate

**Framework**: Virtualization  
**Kind**: property

The device’s delegate.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
weak var delegate: (any VZCustomVirtioDeviceDelegate)? { get set }
```

#### Discussion

To be able to respond to events from a [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md), implement a class that conforms to the [`VZCustomVirtioDeviceDelegate`](vzcustomvirtiodevicedelegate.md) protocol and assign it to this property. You can call the delegate as soon as [`customVirtioConfiguration(_:didCreateDevice:)`](vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration(_:didcreatedevice:).md) returns, to avoid missing any calls, set this delegate when the framework calls [`customVirtioConfiguration(_:didCreateDevice:)`](vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration(_:didcreatedevice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/delegate)*