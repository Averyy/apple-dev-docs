# destinationPort

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The destination port number of the connection.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var destinationPort: UInt32 { get }
```

```objc
@property (readonly) uint32_t destinationPort;
```

## See Also

### Getting the connection details
- [var sourcePort: UInt32](./sourceport.md)
  The port number of the system that opened the connection.
- [var fileDescriptor: Int32](./filedescriptor.md)
  The file descriptor to use when sending data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketconnection/destinationport)*