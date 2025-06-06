# attachment

**Framework**: Virtualization  
**Kind**: property

The object that defines how the configuration of the virtual machine’s serial port interfaces.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var attachment: VZSerialPortAttachment? { get set }
```

#### Discussion

Assign an appropriate attachment object to this property, such as a [`VZFileHandleSerialPortAttachment`](vzfilehandleserialportattachment.md) or [`VZFileSerialPortAttachment`](vzfileserialportattachment.md) object. When configuring the serial ports, the virtual machine uses the attachment to set up the serial port communications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzserialportconfiguration/attachment)*