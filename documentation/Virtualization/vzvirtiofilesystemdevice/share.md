# share

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A value that defines the directory share the host exposes to the guest VM.

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

### Related Documentation
- [class VZSingleDirectoryShare](../vzsingledirectoryshare.md)
  An object that defines the directory share for a single directory.
- [class VZMultipleDirectoryShare](../vzmultipledirectoryshare.md)
  An object that describes a directory share for multiple directories.
### Accessing directory properties
- [var tag: String](./tag.md)
  A string that identifies the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdevice/share)*