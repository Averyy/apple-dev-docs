# init(archivableObject:uniformTypeIdentifier:)

**Framework**: XCTest  
**Kind**: init

Creates an attachment from an object that conforms to `NSSecureCoding`, with a custom UTI.

## Declaration

```swift
convenience init(archivableObject object: any NSSecureCoding, uniformTypeIdentifier identifier: String)
```

## Parameters

- `object`: An encodable object that conforms to [`NSSecureCoding`](https://developer.apple.com/documentation/foundation/nssecurecoding).
- `identifier`: A custom UTI to represent the encoded data’s type.

## See Also

- [convenience init(plistObject: Any)](xctattachment/init(plistobject:).md)
  Creates an attachment from an object that can be represented in an XML property list.
- [convenience init(archivableObject: any NSSecureCoding)](xctattachment/init(archivableobject:).md)
  Creates an attachment from an object that conforms to `NSSecureCoding`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(archivableobject:uniformtypeidentifier:))*