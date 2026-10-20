# init(plistObject:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment from an object that can be represented in an XML property list.

## Declaration

```swift
convenience init(plistObject object: Any)
```

```objc
+ (instancetype) attachmentWithPlistObject:(id) object;
```

#### Discussion

The content of the attachment is an XML property list representation of the provided object with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) value of `"com.apple.xml-property-list"`.

> **Note**:  Creating an attachment with a non-property-list-compatible object will trigger an exception at the point that the attachment is added to an [`XCTActivity`](../xctactivity.md).

## Parameters

- `object`: An object that can be serialized to an XML property list format, such as an array, dictionary, string, or date.

## See Also

### Creating Attachments from Objects
- [convenience init(archivableObject: any NSSecureCoding)](./init%28archivableobject%29.md)
  Creates an attachment from an object that conforms to `NSSecureCoding`.
- [convenience init(archivableObject: any NSSecureCoding, uniformTypeIdentifier: String)](./init%28archivableobject,uniformtypeidentifier%29.md)
  Creates an attachment from an object that conforms to `NSSecureCoding`, with a custom UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(plistobject:))*