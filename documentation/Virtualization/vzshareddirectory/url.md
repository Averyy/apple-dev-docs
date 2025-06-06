# url

**Framework**: Virtualization  
**Kind**: property

A file URL to a directory on the host system to expose to the guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var url: URL { get }
```

#### Discussion

The URL must point to an existing directory path in the host file system.

## See Also

- [var isReadOnly: Bool](vzshareddirectory/isreadonly.md)
  A Boolean value that indicates whether the directory is read-only to the guest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzshareddirectory/url)*