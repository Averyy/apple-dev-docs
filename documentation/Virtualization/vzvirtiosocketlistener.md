# VZVirtioSocketListener

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that listens for port-based connection requests from the guest operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioSocketListener
```

```objc
@interface VZVirtioSocketListener : NSObject
```

## Overview

Use a [`VZVirtioSocketListener`](./vzvirtiosocketlistener.md) object to route connection requests to your associated delegate object. The socket listener object handles incoming connection requests from the guest operating system and directs them to the methods of its associated [`delegate`](./vzvirtiosocketlistener/delegate.md) object. You may use the same listener object to monitor connections on multiple ports.

After creating a [`VZVirtioSocketListener`](./vzvirtiosocketlistener.md) object, assign a custom object to its [`delegate`](./vzvirtiosocketlistener/delegate.md) property. The delegate must implement the [`VZVirtioSocketListenerDelegate`](./vzvirtiosocketlistenerdelegate.md) protocol. To connect the listener to a port, call the [`setSocketListener(_:forPort:)`](./vzvirtiosocketdevice/setsocketlistener%28_,forport%29.md) method of your virtual machine’s [`VZVirtioSocketDevice`](./vzvirtiosocketdevice.md) object.

## Topics

### Responding to new connections
- [var delegate: (any VZVirtioSocketListenerDelegate)?](./vzvirtiosocketlistener/delegate.md)
  The custom object you use to respond to port-based connection attempts.
- [protocol VZVirtioSocketListenerDelegate](./vzvirtiosocketlistenerdelegate.md)
  An interface you use to manage connections between the guest operating system and host computer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Connection management
- [class VZVirtioSocketConnection](./vzvirtiosocketconnection.md)
  A port-based connection between the guest operating system and the host computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketlistener)*