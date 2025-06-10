# init(archivableObject:)

**Framework**: XCTest  
**Kind**: init

Creates an attachment from an object that conforms to `NSSecureCoding`.

## Declaration

```swift
convenience init(archivableObject object: any NSSecureCoding)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"``public.data"`.

## Parameters

- `object`: An encodable object that conforms to  .

## See Also

- [convenience init(plistObject: Any)](xctattachment/init(plistobject:).md)
  Creates an attachment from an object that can be represented in an XML property list.
- [convenience init(archivableObject: any NSSecureCoding, uniformTypeIdentifier: String)](xctattachment/init(archivableobject:uniformtypeidentifier:).md)
  Creates an attachment from an object that conforms to `NSSecureCoding`, with a custom UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(archivableobject:))*