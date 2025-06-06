# VZBridgedNetworkInterface

**Framework**: Virtualization  
**Kind**: class

An object that identifies the supported network interfaces of the host computer.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZBridgedNetworkInterface
```

#### Overview

Use a [`VZBridgedNetworkInterface`](vzbridgednetworkinterface.md) object to retrieve the physical interfaces on the host computer. Use a bridged network interface to create a [`VZBridgedNetworkDeviceAttachment`](vzbridgednetworkdeviceattachment.md) object, which maps that interface to one of your virtual machine’s network devices. The host computer and your virtual machine share access to the physical network interface, but communicate over it using distinct network layers.

You don’t create [`VZBridgedNetworkInterface`](vzbridgednetworkinterface.md) objects directly. Instead, the system creates one object for each physical interface of the host computer and stores those objects in the [`networkInterfaces`](vzbridgednetworkinterface/networkinterfaces.md) property. Iterate over the objects in that property to retrieve the network interfaces you need.

## Topics

### Getting the available interfaces
- [class var networkInterfaces: [VZBridgedNetworkInterface]](vzbridgednetworkinterface/networkinterfaces.md)
  The bridged network interfaces that you may use in your virtual machine.
### Getting the interface description
- [var identifier: String](vzbridgednetworkinterface/identifier.md)
  The unique BSD name of this network interface.
- [var localizedDisplayName: String?](vzbridgednetworkinterface/localizeddisplayname.md)
  A user-visible name for the network interface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzbridgednetworkinterface)*