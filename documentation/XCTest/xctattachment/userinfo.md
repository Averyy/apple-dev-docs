# userInfo

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

User-provided metadata associated with the attachment.

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

```objc
@property (copy, nullable) NSDictionary * userInfo;
```

## Discussion

Assign a custom dictionary to this property to store attachment-specific metadata along with the attachment.

> **Note**:  The contents of the [`userInfo`](./userinfo.md) dictionary are not represented in Xcode test reports.

## See Also

### Attachment Metadata
- [var name: String?](./name.md)
  The attachment’s name, or `nil` if the attachment is unnamed.
- [var uniformTypeIdentifier: String](./uniformtypeidentifier.md)
  The Uniform Type Identifier (UTI) of the data represented by the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/userinfo)*