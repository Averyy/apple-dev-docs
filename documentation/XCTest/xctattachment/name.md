# name

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The attachment’s name, or `nil` if the attachment is unnamed.

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (copy, nullable) NSString * name;
```

## Discussion

Set an attachment’s [`name`](./name.md) property to a custom string to provide a descriptive name for the attachment within Xcode’s test reports.

## See Also

### Attachment Metadata
- [var uniformTypeIdentifier: String](./uniformtypeidentifier.md)
  The Uniform Type Identifier (UTI) of the data represented by the attachment.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  User-provided metadata associated with the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/name)*