# name

**Framework**: Virtualization  
**Kind**: property

The name of the port.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var name: String? { get }
```

#### Discussion

This property can’t change while the VM is running. A null value indicates a name isn’t set.

## See Also

- [var attachment: VZSerialPortAttachment?](vzvirtioconsoleport/attachment.md)
  An array of serial port attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleport/name)*