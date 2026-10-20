# XCTAttachment.Lifetime

**Framework**: XCTest  
**Kind**: enum  
**Role**: Enumeration

The possible lifetime values for a test attachment.

## Declaration

```swift
enum Lifetime
```

```c
enum XCTAttachmentLifetime : NSInteger;
```

## Topics

### Attachment Lifetimes
- [XCTAttachment.Lifetime.deleteOnSuccess](./lifetime-swift.enum/deleteonsuccess.md)
  Indicates that the attachment should be deleted if the test passes.
- [XCTAttachment.Lifetime.keepAlways](./lifetime-swift.enum/keepalways.md)
  Indicates that the attachment should be persisted as part of the test’s results even if the test passes.
### Initializers
- [init?(rawValue: Int)](./lifetime-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting an Attachment’s Lifetime
- [var lifetime: XCTAttachment.Lifetime](./lifetime-swift.property.md)
  Indicates whether the attachment is kept or discarded when its associated test passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/lifetime-swift.enum)*