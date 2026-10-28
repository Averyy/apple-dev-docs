# init(archivableObject:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment from an object that conforms to `NSSecureCoding`.

## Declaration

```swift
convenience init(archivableObject object: any NSSecureCoding)
```

```objc
+ (instancetype) attachmentWithArchivableObject:(id<NSSecureCoding>) object;
```

## Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"``public.data"`.

## Parameters

- `object`: An encodable object that conforms to [`NSSecureCoding`](../../Foundation/nssecurecoding.md).

## See Also

### Creating Attachments from Objects
- [convenience init(plistObject: Any)](./init%28plistobject%29.md)
  Creates an attachment from an object that can be represented in an XML property list.
- [convenience init(archivableObject: any NSSecureCoding, uniformTypeIdentifier: String)](./init%28archivableobject,uniformtypeidentifier%29.md)
  Creates an attachment from an object that conforms to `NSSecureCoding`, with a custom UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(archivableobject:))*