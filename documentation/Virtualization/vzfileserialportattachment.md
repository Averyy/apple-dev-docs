# VZFileSerialPortAttachment

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An attachment point that writes data from the guest system to a file.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZFileSerialPortAttachment
```

```objc
@interface VZFileSerialPortAttachment : VZSerialPortAttachment
```

## Overview

Use a [`VZFileSerialPortAttachment`](./vzfileserialportattachment.md) object to configure a one-way serial port from the guest operating system to the virtual machine. When the guest sends data to the serial port, the virtual machine writes that data to the specified file. You can’t use this serial port to send data back to the guest.

Create a [`VZSerialPortAttachment`](./vzserialportattachment.md) object and assign it to an appropriate subclass of [`VZSerialPortConfiguration`](./vzserialportconfiguration.md) object, such as [`VZVirtioConsoleDeviceConfiguration`](./vzvirtioconsoledeviceconfiguration.md). The file you use to create this object must be writable.

## Topics

### Creating the attachment point
- [init(url: URL, append: Bool) throws](./vzfileserialportattachment/init%28url,append%29-37g72.md)
  Creates a file-based serial port attachment object.
### Getting the file details
- [var url: URL](./vzfileserialportattachment/url.md)
  The URL of a file on the local file system.
- [var append: Bool](./vzfileserialportattachment/append.md)
  A Boolean that indicates whether the virtual machine appends data to the file.
### Initializers
- [init(URL: URL, append: Bool) throws](./vzfileserialportattachment/init%28url,append%29-7xoxy.md)

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

## See Also

### Attachment points
- [class VZFileHandleSerialPortAttachment](./vzfilehandleserialportattachment.md)
  An attachment point that allows bidirectional communication using file handles.
- [class VZSerialPortAttachment](./vzserialportattachment.md)
  The common behaviors for the serial attachment points of your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfileserialportattachment)*