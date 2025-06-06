# userInfo

**Framework**: Xctest  
**Kind**: property

User-provided metadata associated with the attachment.

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

#### Discussion

Assign a custom dictionary to this property to store attachment-specific metadata along with the attachment.

> **Note**:  The contents of the [`userInfo`](xctattachment/userinfo.md) dictionary are not represented in Xcode test reports.

## See Also

- [var name: String?](xctattachment/name.md)
  The attachment’s name, or `nil` if the attachment is unnamed.
- [var uniformTypeIdentifier: String](xctattachment/uniformtypeidentifier.md)
  The Uniform Type Identifier (UTI) of the data represented by the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/userinfo)*