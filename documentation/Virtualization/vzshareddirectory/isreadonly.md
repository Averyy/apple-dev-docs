# isReadOnly

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the directory is read-only to the guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var isReadOnly: Bool { get }
```

```objc
@property (readonly, getter=isReadOnly) BOOL readOnly;
```

## See Also

### Accessing Directory Properties
- [var url: URL](./url.md)
  A file URL to a directory on the host system to expose to the guest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzshareddirectory/isreadonly)*