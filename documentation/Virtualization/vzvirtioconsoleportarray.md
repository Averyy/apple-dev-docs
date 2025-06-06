# VZVirtioConsolePortArray

**Framework**: Virtualization  
**Kind**: class

A class that represents a collection of Virtio console ports.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioConsolePortArray
```

## Topics

### Determining the number of ports
- [var maximumPortCount: UInt32](vzvirtioconsoleportarray/maximumportcount.md)
  An unsigned integer that represents the maximum number of ports allocated by this device.
### Accessing a specific port
- [subscript(Int) -> VZVirtioConsolePort?](vzvirtioconsoleportarray/subscript(_:).md)
  Returns the Virtio console port at the specified index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioConsoleDevice](vzvirtioconsoledevice.md)
  A class that represents a Virtio console device in a virtual machine.
- [class VZVirtioConsolePort](vzvirtioconsoleport.md)
  A class that represents a Virtio console port in a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportarray)*