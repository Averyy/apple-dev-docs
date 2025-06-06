# attachment

**Framework**: Virtualization  
**Kind**: property

The object that defines how the virtual network device communicates with the host system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var attachment: VZNetworkDeviceAttachment? { get set }
```

#### Discussion

The default value of this property is `nil`. Assign an appropriate value to specify the type of network interface you want to make available to the guest operating system. For example, assign a [`VZBridgedNetworkDeviceAttachment`](vzbridgednetworkdeviceattachment.md) object to grant access to one of the host computer’s physical network interfaces.

> ❗ **Important**:  If you assign a [`VZBridgedNetworkDeviceAttachment`](vzbridgednetworkdeviceattachment.md) object to this property, your app must have the [`com.apple.vm.networking`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.vm.networking) entitlement. Without that entitlement, validation of your [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object fails.

 If you assign a [`VZBridgedNetworkDeviceAttachment`](vzbridgednetworkdeviceattachment.md) object to this property, your app must have the [`com.apple.vm.networking`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.vm.networking) entitlement. Without that entitlement, validation of your [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object fails.

## See Also

- [var macAddress: VZMACAddress](vznetworkdeviceconfiguration/macaddress.md)
  The media access control (MAC) address to assign to the network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkdeviceconfiguration/attachment)*