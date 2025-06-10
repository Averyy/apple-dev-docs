# XCTAttachment.Lifetime.deleteOnSuccess

**Framework**: XCTest  
**Kind**: case

Indicates that the attachment should be deleted if the test passes.

## Declaration

```swift
case deleteOnSuccess
```

## Mentions

- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)

#### Discussion

[`XCTAttachment.Lifetime.deleteOnSuccess`](xctattachment/lifetime-swift.enum/deleteonsuccess.md) is the default lifetime for all new attachments. This lifetime indicates that an attachment should be discarded if its test passes successfully, to save on storage space.

To persist an attachment even when its test passes, set the attachment’s [`lifetime`](xctattachment/lifetime-swift.property.md) property to [`XCTAttachment.Lifetime.keepAlways`](xctattachment/lifetime-swift.enum/keepalways.md) after attachment initialization.

## See Also

- [XCTAttachment.Lifetime.keepAlways](xctattachment/lifetime-swift.enum/keepalways.md)
  Indicates that the attachment should be persisted as part of the test’s results even if the test passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/lifetime-swift.enum/deleteonsuccess)*