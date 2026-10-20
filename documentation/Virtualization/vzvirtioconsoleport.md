# VZVirtioConsolePort

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A class that represents a Virtio console port in a VM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioConsolePort
```

```objc
@interface VZVirtioConsolePort : NSObject
```

#### Overview

Don’t instantiate a `VZVirtioConsolePort` directly. You retrieve this object from the [`VZVirtioConsoleDevice`](./vzvirtioconsoledevice.md) [`ports`](./vzvirtioconsoledevice/ports.md) property.

## Topics

### Configuring the port
- [var name: String?](./vzvirtioconsoleport/name.md)
  The name of the port.
- [var attachment: VZSerialPortAttachment?](./vzvirtioconsoleport/attachment.md)
  An array of serial port attachments.

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

### Console ports
- [class VZVirtioConsolePortArray](./vzvirtioconsoleportarray.md)
  A class that represents a collection of Virtio console ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleport)*