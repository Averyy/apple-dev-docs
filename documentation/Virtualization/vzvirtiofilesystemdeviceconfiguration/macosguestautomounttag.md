# macOSGuestAutomountTag

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

A value that indicates that the guest needs to automount this file system device in the guest VM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class var macOSGuestAutomountTag: String { get }
```

```objc
@property (class, readonly) NSString * macOSGuestAutomountTag;
```

## Discussion

A device configured with this tag is automatically mounted in a macOS guest.

## See Also

### Getting file system information
- [var share: VZDirectoryShare?](./share.md)
  A value that defines how the host exposes resources to the guest virtual machine.
- [var tag: String](./tag.md)
  A label that identifies this device in the guest VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdeviceconfiguration/macosguestautomounttag)*