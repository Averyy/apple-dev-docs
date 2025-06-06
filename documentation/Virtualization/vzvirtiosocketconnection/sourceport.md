# sourcePort

**Framework**: Virtualization  
**Kind**: property

The port number of the system that opened the connection.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var sourcePort: UInt32 { get }
```

#### Discussion

When the guest operating system opens a connection, this property contains the port number that the guest specified. When you open a connection to the guest operating system from your [`VZVirtioSocketDevice`](vzvirtiosocketdevice.md) object, this property contains a randomly generated port number.

## See Also

- [var destinationPort: UInt32](vzvirtiosocketconnection/destinationport.md)
  The destination port number of the connection.
- [var fileDescriptor: Int32](vzvirtiosocketconnection/filedescriptor.md)
  The file descriptor to use when sending data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketconnection/sourceport)*