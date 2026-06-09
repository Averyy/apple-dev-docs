# validateTag(_:)

**Framework**: Virtualization  
**Kind**: method

Checks to see whether a Virtio tag is valid.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func validateTag(_ tag: String) throws
```

## Mentions

- [Running Intel Binaries in Linux VMs](running-intel-binaries-in-linux-vms.md)

#### Discussion

The tag can’t be empty and must be fewer than 36 bytes when encoded in UTF-8.

## Parameters

- `tag`: The tag to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdeviceconfiguration/validatetag(_:))*