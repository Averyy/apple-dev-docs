# VZSpiceAgentPortAttachment

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An attachment point that enables the Spice clipboard sharing capability.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZSpiceAgentPortAttachment
```

```objc
@interface VZSpiceAgentPortAttachment : VZSerialPortAttachment
```

## Topics

### Creating a shared clipboard
- [init()](./vzspiceagentportattachment/init%28%29.md)
  Creates a new Spice agent port attachment.
### Enabling clipboard sharing between the host and the VM
- [var sharesClipboard: Bool](./vzspiceagentportattachment/sharesclipboard.md)
  A Boolean value that indicates whether the framework needs to share the clipboard between the host and the VM.
### Naming the Virtio console port for the Spice guest agent
- [class var spiceAgentPortName: String](./vzspiceagentportattachment/spiceagentportname.md)
  The name of the Virtio console port for the Spice guest agent.

## Relationships

### Inherits From
- [VZSerialPortAttachment](./vzserialportattachment.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzspiceagentportattachment)*