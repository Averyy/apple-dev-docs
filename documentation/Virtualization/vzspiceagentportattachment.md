# VZSpiceAgentPortAttachment

**Framework**: Virtualization  
**Kind**: class

An attachment point that enables the Spice clipboard sharing capability.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZSpiceAgentPortAttachment
```

## Topics

### Creating a shared clipboard
- [init()](vzspiceagentportattachment/init.md)
  Creates a new Spice agent port attachment.
### Enabling clipboard sharing between the host and the VM
- [var sharesClipboard: Bool](vzspiceagentportattachment/sharesclipboard.md)
  A Boolean value that indicates whether the framework needs to share the clipboard between the host and the VM.
### Naming the Virtio console port for the Spice guest agent
- [class var spiceAgentPortName: String](vzspiceagentportattachment/spiceagentportname.md)
  The name of the Virtio console port for the Spice guest agent.

## Relationships

### Inherits From
- [VZSerialPortAttachment](vzserialportattachment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzspiceagentportattachment)*