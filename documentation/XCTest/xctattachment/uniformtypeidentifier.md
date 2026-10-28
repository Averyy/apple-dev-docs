# uniformTypeIdentifier

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The Uniform Type Identifier (UTI) of the data represented by the attachment.

## Declaration

```swift
var uniformTypeIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * uniformTypeIdentifier;
```

## Mentions

- [Adding Attachments to Tests, Activities, and Issues](../adding-attachments-to-tests-activities-and-issues.md)

## Discussion

Uniform Type Identifiers (UTIs) are Apple-defined identifiers that uniquely identify a particular type of data, such as a JPEG image or text document. Every [`XCTAttachment`](../xctattachment.md) instance stores a UTI string that indicates the type of data represented by the attachment.

When you create an attachment with an [`XCTAttachment`](../xctattachment.md) convenience initializer such as [`init(contentsOfFileAtURL:)`](./init%28contentsoffileaturl%29.md) or [`init(plistObject:)`](./init%28plistobject%29.md), XCTest determines an appropriate UTI to use for the provided data. See each convenience initializer for more information about the UTIs it uses.

Where possible, you should use the [`XCTAttachment`](../xctattachment.md) convenience initializers to create attachments for known data types. If you need to create an attachment with a manually specified UTI (such as for a custom data format used by your app), use one of the following initializers instead:

- [`init(archivableObject:uniformTypeIdentifier:)`](./init%28archivableobject,uniformtypeidentifier%29.md) for custom data stored in an object that conforms to [`NSSecureCoding`](../../Foundation/nssecurecoding.md)
- [`init(contentsOfFileAtURL:uniformTypeIdentifier:)`](./init%28contentsoffileaturl,uniformtypeidentifier%29.md) for reading the contents of a file with a known custom UTI
- [`init(data:uniformTypeIdentifier:)`](./init%28data,uniformtypeidentifier%29.md) for data stored in memory with a known custom UTI
- [`init(uniformTypeIdentifier:name:payload:userInfo:)`](./init%28uniformtypeidentifier,name,payload,userinfo%29.md) for a data payload with a custom UTI, name, and user info dictionary

For more information about UTIs, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319). For a list of system-declared UTIs, see [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257).

## See Also

### Attachment Metadata
- [var name: String?](./name.md)
  The attachment’s name, or `nil` if the attachment is unnamed.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  User-provided metadata associated with the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/uniformtypeidentifier)*