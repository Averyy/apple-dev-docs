# init(plistObject:)

**Framework**: Xctest  
**Kind**: init

Creates an attachment from an object that can be represented in an XML property list.

## Declaration

```swift
convenience init(plistObject object: Any)
```

#### Discussion

The content of the attachment is an XML property list representation of the provided object with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) value of `"com.apple.xml-property-list"`.

> **Note**:  Creating an attachment with a non-property-list-compatible object will trigger an exception at the point that the attachment is added to an [`XCTActivity`](xctactivity.md).

 Creating an attachment with a non-property-list-compatible object will trigger an exception at the point that the attachment is added to an [`XCTActivity`](xctactivity.md).

## Parameters

- `object`: An object that can be serialized to an XML property list format, such as an array, dictionary, string, or date.

## See Also

- [convenience init(archivableObject: any NSSecureCoding)](xctattachment/init(archivableobject:).md)
  Creates an attachment from an object that conforms to `NSSecureCoding`.
- [convenience init(archivableObject: any NSSecureCoding, uniformTypeIdentifier: String)](xctattachment/init(archivableobject:uniformtypeidentifier:).md)
  Creates an attachment from an object that conforms to `NSSecureCoding`, with a custom UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(plistobject:))*