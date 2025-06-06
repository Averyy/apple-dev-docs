# connect(toPort:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Initiates a connection to the specified port of the guest operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func connect(toPort port: UInt32, completionHandler: @escaping (Result<VZVirtioSocketConnection, any Error>) -> Void)
```

#### Discussion

This method initiates the connection asynchronously, and executes the completion handler when the results are available. If the guest operating system doesn’t listen for connections to the specifed port, this method does nothing.

For a successful connection, this method sets the [`sourcePort`](vzvirtiosocketconnection/sourceport.md) property of the resulting [`VZVirtioSocketConnection`](vzvirtiosocketconnection.md) object to a random port number.

## Parameters

- `port`: The destination port number in the guest operating system.
- `completionHandler`: The block to execute with the results of the connection attempt. This block has no return value and takes the following parameter:

## See Also

- [func connect(toPort: UInt32) async throws -> VZVirtioSocketConnection](vzvirtiosocketdevice/connect(toport:).md)
  Initiates a connection to the specified port of the guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdevice/connect(toport:completionhandler:))*