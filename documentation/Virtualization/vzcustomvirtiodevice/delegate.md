# delegate

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The device’s delegate.

**Availability**:
- macOS 27.0+

## Declaration

```swift
weak var delegate: (any VZCustomVirtioDeviceDelegate)? { get set }
```

```objc
@property (weak, nullable) id<VZCustomVirtioDeviceDelegate> delegate;
```

#### Discussion

To be able to respond to events from a [`VZCustomVirtioDevice`](../vzcustomvirtiodevice.md), implement a class that conforms to the [`VZCustomVirtioDeviceDelegate`](../vzcustomvirtiodevicedelegate.md) protocol and assign it to this property. You can call the delegate as soon as [`customVirtioConfiguration(_:didCreateDevice:)`](../vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration%28_,didcreatedevice%29.md) returns, to avoid missing any calls, set this delegate when the framework calls [`customVirtioConfiguration(_:didCreateDevice:)`](../vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration%28_,didcreatedevice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/delegate)*