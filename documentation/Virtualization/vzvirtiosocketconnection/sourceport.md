# sourcePort

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The port number of the system that opened the connection.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var sourcePort: UInt32 { get }
```

```objc
@property (readonly) uint32_t sourcePort;
```

#### Discussion

When the guest operating system opens a connection, this property contains the port number that the guest specified. When you open a connection to the guest operating system from your [`VZVirtioSocketDevice`](../vzvirtiosocketdevice.md) object, this property contains a randomly generated port number.

## See Also

### Getting the connection details
- [var destinationPort: UInt32](./destinationport.md)
  The destination port number of the connection.
- [var fileDescriptor: Int32](./filedescriptor.md)
  The file descriptor to use when sending data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketconnection/sourceport)*