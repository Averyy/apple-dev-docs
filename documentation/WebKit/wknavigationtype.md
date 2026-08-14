# WKNavigationType

**Framework**: WebKit  
**Kind**: enum

The type of action that triggered the navigation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
enum WKNavigationType
```

## Topics

### Getting the Navigation Types
- [WKNavigationType.linkActivated](wknavigationtype/linkactivated.md)
  A link activation.
- [WKNavigationType.formSubmitted](wknavigationtype/formsubmitted.md)
  A request to submit a form.
- [WKNavigationType.backForward](wknavigationtype/backforward.md)
  A request for the frame’s next or previous item.
- [WKNavigationType.reload](wknavigationtype/reload.md)
  A request to reload the webpage.
- [WKNavigationType.formResubmitted](wknavigationtype/formresubmitted.md)
  A request to resubmit a form.
- [WKNavigationType.other](wknavigationtype/other.md)
  A navigation request that originates for some other reason.
### Initializers
- [init?(rawValue: Int)](wknavigationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var navigationType: WKNavigationType](wknavigationaction/navigationtype.md)
  The type of action that triggered the navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationtype)*