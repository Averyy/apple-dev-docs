# setSocketListener(_:forPort:)

**Framework**: Virtualization  
**Kind**: method

Configures an object to monitor the specified port for new connections.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func setSocketListener(_ listener: VZVirtioSocketListener, forPort port: UInt32)
```

#### Discussion

You can register the same listener object on multiple ports. When the guest operating system opens a connection to the port, the listener object notifies its associated delegate.

## Parameters

- `listener`: The   object to monitor the port. This object replaces the previous listener object, if any.
- `port`: The port number to monitor.

## See Also

- [func removeSocketListener(forPort: UInt32)](vzvirtiosocketdevice/removesocketlistener(forport:).md)
  Removes the listener object from the specfied port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdevice/setsocketlistener(_:forport:))*