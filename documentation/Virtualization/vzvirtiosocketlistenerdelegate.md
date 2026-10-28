# VZVirtioSocketListenerDelegate

**Framework**: Virtualization  
**Kind**: protocol  
**Role**: Protocol

An interface you use to manage connections between the guest operating system and host computer.

**Availability**:
- macOS 11.0+

## Declaration

```swift
protocol VZVirtioSocketListenerDelegate : NSObjectProtocol
```

```objc
@protocol VZVirtioSocketListenerDelegate <NSObject>
```

## Overview

Adopt the [`VZVirtioSocketListenerDelegate`](./vzvirtiosocketlistenerdelegate.md) protocol in a custom object and use it to accept or reject socket-based connection attempts from the guest operating system to the host computer. You may use the same object to manage connection attempts on multiple ports.

## Topics

### Accepting new connections
- [func listener(VZVirtioSocketListener, shouldAcceptNewConnection: VZVirtioSocketConnection, from: VZVirtioSocketDevice) -> Bool](./vzvirtiosocketlistenerdelegate/listener%28_,shouldacceptnewconnection,from%29.md)
  Returns a Boolean value that indicates whether to accept a new connection from the guest operating system.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to new connections
- [var delegate: (any VZVirtioSocketListenerDelegate)?](./vzvirtiosocketlistener/delegate.md)
  The custom object you use to respond to port-based connection attempts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketlistenerdelegate)*