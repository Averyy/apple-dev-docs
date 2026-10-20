# removeSocketListener(forPort:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Removes the listener object from the specfied port.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func removeSocketListener(forPort port: UInt32)
```

```objc
- (void) removeSocketListenerForPort:(uint32_t) port;
```

## Parameters

- `port`: The port number to clear. If the specified port doesn’t have a listener object, this method does nothing.

## See Also

### Configuring Port Listeners
- [func setSocketListener(VZVirtioSocketListener, forPort: UInt32)](./setsocketlistener%28_,forport%29.md)
  Configures an object to monitor the specified port for new connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdevice/removesocketlistener(forport:))*