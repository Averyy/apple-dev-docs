# listener(_:shouldAcceptNewConnection:from:)

**Framework**: Virtualization  
**Kind**: method

Returns a Boolean value that indicates whether to accept a new connection from the guest operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
optional func listener(_ listener: VZVirtioSocketListener, shouldAcceptNewConnection connection: VZVirtioSocketConnection, from socketDevice: VZVirtioSocketDevice) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to establish the connection, or [`false`](https://developer.apple.com/documentation/Swift/false) to reject it.

#### Discussion

Use your method’s implementation to quickly determine whether to accept or reject connection attempts. A typical implementation verifies that a connection between the specified ports is permissible. Return a result as quickly as possible, and don’t perform any long-running operations in this method.

If you don’t implement this method, the virtual machine refuses all connection requests as if this method returned [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `listener`: The listener object that monitors the associated port.
- `connection`: The object that contains information about the proposed connection. Use this object to fetch port information.
- `socketDevice`: The Virtio socket device that requested the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketlistenerdelegate/listener(_:shouldacceptnewconnection:from:))*