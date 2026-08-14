# XCTAttachment.Lifetime

**Framework**: XCTest  
**Kind**: enum

The possible lifetime values for a test attachment.

## Declaration

```swift
enum Lifetime
```

## Topics

### Attachment Lifetimes
- [XCTAttachment.Lifetime.deleteOnSuccess](xctattachment/lifetime-swift.enum/deleteonsuccess.md)
  Indicates that the attachment should be deleted if the test passes.
- [XCTAttachment.Lifetime.keepAlways](xctattachment/lifetime-swift.enum/keepalways.md)
  Indicates that the attachment should be persisted as part of the test’s results even if the test passes.
### Initializers
- [init?(rawValue: Int)](xctattachment/lifetime-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var lifetime: XCTAttachment.Lifetime](xctattachment/lifetime-swift.property.md)
  Indicates whether the attachment is kept or discarded when its associated test passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/lifetime-swift.enum)*