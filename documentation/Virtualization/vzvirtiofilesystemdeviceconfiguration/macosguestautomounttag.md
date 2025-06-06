# macOSGuestAutomountTag

**Framework**: Virtualization  
**Kind**: property

A value that indicates that the guest needs to automount this file system device in the guest VM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class var macOSGuestAutomountTag: String { get }
```

#### Discussion

A device configured with this tag is automatically mounted in a macOS guest.

## See Also

- [var share: VZDirectoryShare?](vzvirtiofilesystemdeviceconfiguration/share.md)
  A value that defines how the host exposes resources to the guest virtual machine.
- [var tag: String](vzvirtiofilesystemdeviceconfiguration/tag.md)
  A label that identifies this device in the guest VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdeviceconfiguration/macosguestautomounttag)*