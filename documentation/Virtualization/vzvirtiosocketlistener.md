# VZVirtioSocketListener

**Framework**: Virtualization  
**Kind**: class

An object that listens for port-based connection requests from the guest operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioSocketListener
```

#### Overview

Use a [`VZVirtioSocketListener`](vzvirtiosocketlistener.md) object to route connection requests to your associated delegate object. The socket listener object handles incoming connection requests from the guest operating system and directs them to the methods of its associated [`delegate`](vzvirtiosocketlistener/delegate.md) object. You may use the same listener object to monitor connections on multiple ports.

After creating a [`VZVirtioSocketListener`](vzvirtiosocketlistener.md) object, assign a custom object to its [`delegate`](vzvirtiosocketlistener/delegate.md) property. The delegate must implement the [`VZVirtioSocketListenerDelegate`](vzvirtiosocketlistenerdelegate.md) protocol. To connect the listener to a port, call the [`setSocketListener(_:forPort:)`](vzvirtiosocketdevice/setsocketlistener(_:forport:).md) method of your virtual machine’s [`VZVirtioSocketDevice`](vzvirtiosocketdevice.md) object.

## Topics

### Responding to new connections
- [var delegate: (any VZVirtioSocketListenerDelegate)?](vzvirtiosocketlistener/delegate.md)
  The custom object you use to respond to port-based connection attempts.
- [protocol VZVirtioSocketListenerDelegate](vzvirtiosocketlistenerdelegate.md)
  An interface you use to manage connections between the guest operating system and host computer.

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

## See Also

- [class VZVirtioSocketConnection](vzvirtiosocketconnection.md)
  A port-based connection between the guest operating system and the host computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketlistener)*