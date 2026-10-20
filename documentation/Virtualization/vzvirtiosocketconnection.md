# VZVirtioSocketConnection

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A port-based connection between the guest operating system and the host computer.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioSocketConnection
```

```objc
@interface VZVirtioSocketConnection : NSObject
```

#### Overview

A [`VZVirtioSocketConnection`](./vzvirtiosocketconnection.md) object contains the port information for the guest operating system and host computer. You don’t create connection objects directly. When the guest operating system initiates a connection, the virtual machine creates the connection object and passes it to the appropriate [`VZVirtioSocketListener`](./vzvirtiosocketlistener.md) object, which forwards the object to its delegate. When the virtual machine opens a connection to a guest port, the [`connect(toPort:)`](./vzvirtiosocketdevice/connect%28toport%29.md) method (Objective-C) or [`connect(toPort:completionHandler:)`](./vzvirtiosocketdevice/connect%28toport,completionhandler%29.md) method (Swift) pass the connection object to your completion handler.

## Topics

### Getting the connection details
- [var sourcePort: UInt32](./vzvirtiosocketconnection/sourceport.md)
  The port number of the system that opened the connection.
- [var destinationPort: UInt32](./vzvirtiosocketconnection/destinationport.md)
  The destination port number of the connection.
- [var fileDescriptor: Int32](./vzvirtiosocketconnection/filedescriptor.md)
  The file descriptor to use when sending data.
### Closing the connection
- [func close()](./vzvirtiosocketconnection/close%28%29.md)
  Close the file descriptor associated with the socket.

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
- [class VZVirtioSocketListener](./vzvirtiosocketlistener.md)
  An object that listens for port-based connection requests from the guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketconnection)*