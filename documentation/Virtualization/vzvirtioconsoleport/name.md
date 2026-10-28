# name

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The name of the port.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var name: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * name;
```

## Discussion

This property can’t change while the VM is running. A null value indicates a name isn’t set.

## See Also

### Configuring the port
- [var attachment: VZSerialPortAttachment?](./attachment.md)
  An array of serial port attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleport/name)*