# fileDescriptor

**Framework**: Virtualization  
**Kind**: property

The file descriptor to use when sending data.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var fileDescriptor: Int32 { get }
```

#### Discussion

To send data to the other side of the connection, write to the file descriptor. To read data from connection, read from the file descriptor. If the socket connection is closed, the value of this property is `-1`.

## See Also

- [var sourcePort: UInt32](vzvirtiosocketconnection/sourceport.md)
  The port number of the system that opened the connection.
- [var destinationPort: UInt32](vzvirtiosocketconnection/destinationport.md)
  The destination port number of the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketconnection/filedescriptor)*