# tag

**Framework**: Virtualization  
**Kind**: property

A string that identifies the device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var tag: String { get }
```

#### Discussion

The system presents the `tag` as a label in the guest VM that identifies this device that’s available for mounting.

## See Also

- [var share: VZDirectoryShare?](vzvirtiofilesystemdevice/share.md)
  A value that defines the directory share the host exposes to the guest VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdevice/tag)*