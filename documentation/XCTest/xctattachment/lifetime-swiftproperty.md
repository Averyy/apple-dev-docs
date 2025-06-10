# lifetime

**Framework**: XCTest  
**Kind**: property

Indicates whether the attachment is kept or discarded when its associated test passes.

## Declaration

```swift
var lifetime: XCTAttachment.Lifetime { get set }
```

## Mentions

- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)

#### Discussion

Defaults to [`XCTAttachment.Lifetime.deleteOnSuccess`](xctattachment/lifetime-swift.enum/deleteonsuccess.md), indicating that the attachment should be discarded when its test passes successfully, to save on storage space. Set this property to [`XCTAttachment.Lifetime.keepAlways`](xctattachment/lifetime-swift.enum/keepalways.md) to persist an attachment even when its test passes.

## See Also

- [XCTAttachment.Lifetime](xctattachment/lifetime-swift.enum.md)
  The possible lifetime values for a test attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/lifetime-swift.property)*