# setSocketListener(_:forPort:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Configures an object to monitor the specified port for new connections.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func setSocketListener(_ listener: VZVirtioSocketListener, forPort port: UInt32)
```

```objc
- (void) setSocketListener:(VZVirtioSocketListener *) listener forPort:(uint32_t) port;
```

#### Discussion

You can register the same listener object on multiple ports. When the guest operating system opens a connection to the port, the listener object notifies its associated delegate.

## Parameters

- `listener`: The [`VZVirtioSocketListener`](../vzvirtiosocketlistener.md) object to monitor the port. This object replaces the previous listener object, if any.
- `port`: The port number to monitor.

## See Also

### Configuring Port Listeners
- [func removeSocketListener(forPort: UInt32)](./removesocketlistener%28forport%29.md)
  Removes the listener object from the specfied port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdevice/setsocketlistener(_:forport:))*