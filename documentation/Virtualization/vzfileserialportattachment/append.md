# append

**Framework**: Virtualization  
**Kind**: property

A Boolean that indicates whether the virtual machine appends data to the file.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var append: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the virtual machine appends new data to the file; otherwise, it replaces the existing contents of the file before writing new data to it.

## See Also

- [var url: URL](vzfileserialportattachment/url.md)
  The URL of a file on the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfileserialportattachment/append)*