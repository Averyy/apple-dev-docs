# VZVirtioSocketDevice

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A device that manages port-based connections between the guest system and the host computer.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioSocketDevice
```

```objc
@interface VZVirtioSocketDevice : VZSocketDevice
```

## Overview

Use a [`VZVirtioSocketDevice`](./vzvirtiosocketdevice.md) object to configure services and other communication end points in your virtual machine. Host computers make services available using ports, which identify the type of service and the protocol to use when transmitting data. Use this object to specify the ports available to your guest operating system, and to register handlers to manage the communication on those ports.

Don’t create a [`VZVirtioSocketDevice`](./vzvirtiosocketdevice.md) object directly. Instead, when you request a socket device in your configuration, the virtual machine creates it and stores it in the [`socketDevices`](./vzvirtualmachine/socketdevices.md) property. For each port you want to make available in your virtual machine, call the [`setSocketListener(_:forPort:)`](./vzvirtiosocketdevice/setsocketlistener%28_,forport%29.md) method and provide an object to manage the port connections.

## Topics

### Configuring Port Listeners
- [func setSocketListener(VZVirtioSocketListener, forPort: UInt32)](./vzvirtiosocketdevice/setsocketlistener%28_,forport%29.md)
  Configures an object to monitor the specified port for new connections.
- [func removeSocketListener(forPort: UInt32)](./vzvirtiosocketdevice/removesocketlistener%28forport%29.md)
  Removes the listener object from the specfied port.
### Connecting to Guest System Ports
- [func connect(toPort: UInt32, completionHandler: (Result<VZVirtioSocketConnection, any Error>) -> Void)](./vzvirtiosocketdevice/connect%28toport,completionhandler%29.md)
  Initiates a connection to the specified port of the guest operating system.
- [func connect(toPort: UInt32) async throws -> VZVirtioSocketConnection](./vzvirtiosocketdevice/connect%28toport%29.md)
  Initiates a connection to the specified port of the guest operating system.

## Relationships

### Inherits From
- [VZSocketDevice](./vzsocketdevice.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Devices
- [class VZSocketDevice](./vzsocketdevice.md)
  The common behavior of socket devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdevice)*