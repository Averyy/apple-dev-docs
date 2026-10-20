# share

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A value that defines how the host exposes resources to the guest virtual machine.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var share: VZDirectoryShare? { get set }
```

```objc
@property (strong, nullable) VZDirectoryShare * share;
```

## See Also

### Getting file system information
- [var tag: String](./tag.md)
  A label that identifies this device in the guest VM.
- [class var macOSGuestAutomountTag: String](./macosguestautomounttag.md)
  A value that indicates that the guest needs to automount this file system device in the guest VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdeviceconfiguration/share)*