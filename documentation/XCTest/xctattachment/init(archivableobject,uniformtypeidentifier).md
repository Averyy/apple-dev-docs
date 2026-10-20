# init(archivableObject:uniformTypeIdentifier:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment from an object that conforms to `NSSecureCoding`, with a custom UTI.

## Declaration

```swift
convenience init(archivableObject object: any NSSecureCoding, uniformTypeIdentifier identifier: String)
```

```objc
+ (instancetype) attachmentWithArchivableObject:(id<NSSecureCoding>) object uniformTypeIdentifier:(NSString *) identifier;
```

## Parameters

- `object`: An encodable object that conforms to [`NSSecureCoding`](../../Foundation/nssecurecoding.md).
- `identifier`: A custom UTI to represent the encoded data’s type.

## See Also

### Creating Attachments from Objects
- [convenience init(plistObject: Any)](./init%28plistobject%29.md)
  Creates an attachment from an object that can be represented in an XML property list.
- [convenience init(archivableObject: any NSSecureCoding)](./init%28archivableobject%29.md)
  Creates an attachment from an object that conforms to `NSSecureCoding`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(archivableobject:uniformtypeidentifier:))*