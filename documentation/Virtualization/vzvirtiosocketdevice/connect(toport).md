# connect(toPort:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Initiates a connection to the specified port of the guest operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func connect(toPort port: UInt32) async throws -> VZVirtioSocketConnection
```

```objc
- (void) connectToPort:(uint32_t) port completionHandler:(void (^)(VZVirtioSocketConnection *connection, NSError *error)) completionHandler;
```

#### Discussion

This method initiates the connection asynchronously, and executes the completion handler when the results are available. If the guest operating system doesn’t listen for connections to the specifed port, this method does nothing.

For a successful connection, this method sets the [`sourcePort`](../vzvirtiosocketconnection/sourceport.md) property of the resulting [`VZVirtioSocketConnection`](../vzvirtiosocketconnection.md) object to a random port number.

## Parameters

- `port`: The destination port number in the guest operating system.

## See Also

### Connecting to Guest System Ports
- [func connect(toPort: UInt32, completionHandler: (Result<VZVirtioSocketConnection, any Error>) -> Void)](./connect%28toport,completionhandler%29.md)
  Initiates a connection to the specified port of the guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdevice/connect(toport:))*