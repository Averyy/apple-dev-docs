# WKNavigationType

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum WKNavigationType : NSInteger;
```

## Topics

### Getting the Navigation Types
- [WKNavigationType.linkActivated](./wknavigationtype/linkactivated.md)
  A link activation.
- [WKNavigationType.formSubmitted](./wknavigationtype/formsubmitted.md)
  A request to submit a form.
- [WKNavigationType.backForward](./wknavigationtype/backforward.md)
  A request for the frame’s next or previous item.
- [WKNavigationType.reload](./wknavigationtype/reload.md)
  A request to reload the webpage.
- [WKNavigationType.formResubmitted](./wknavigationtype/formresubmitted.md)
  A request to resubmit a form.
- [WKNavigationType.other](./wknavigationtype/other.md)
  A navigation request that originates for some other reason.
### Initializers
- [init?(rawValue: Int)](./wknavigationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the navigation type
- [var navigationType: WKNavigationType](./wknavigationaction/navigationtype.md)
  The type of action that triggered the navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationtype)*