# tag

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A label that identifies this device in the guest VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var tag: String { get set }
```

```objc
@property (copy) NSString * tag;
```

## See Also

### Getting file system information
- [var share: VZDirectoryShare?](./share.md)
  A value that defines how the host exposes resources to the guest virtual machine.
- [class var macOSGuestAutomountTag: String](./macosguestautomounttag.md)
  A value that indicates that the guest needs to automount this file system device in the guest VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdeviceconfiguration/tag)*