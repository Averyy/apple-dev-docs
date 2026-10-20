# VZVirtioConsolePortArray

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A class that represents a collection of Virtio console ports.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioConsolePortArray
```

```objc
@interface VZVirtioConsolePortArray : NSObject
```

## Topics

### Determining the number of ports
- [var maximumPortCount: UInt32](./vzvirtioconsoleportarray/maximumportcount.md)
  An unsigned integer that represents the maximum number of ports allocated by this device.
### Accessing a specific port
- [subscript(Int) -> VZVirtioConsolePort?](./vzvirtioconsoleportarray/subscript%28_%29.md)
  Returns the Virtio console port at the specified index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZVirtioConsoleDevice](./vzvirtioconsoledevice.md)
  A class that represents a Virtio console device in a virtual machine.
### Console ports
- [class VZVirtioConsolePort](./vzvirtioconsoleport.md)
  A class that represents a Virtio console port in a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportarray)*