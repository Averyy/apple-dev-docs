# WebNavigationType

**Framework**: WebKit  
**Kind**: enum

Possible values for the [`WebActionNavigationTypeKey`](webactionnavigationtypekey.md) key that appears in an action dictionary.

**Availability**:
- macOS 10.3+

## Declaration

```swift
enum WebNavigationType
```

## Topics

### Constants
- [WebNavigationType.linkClicked](webnavigationtype/linkclicked.md)
  A link (an `href`) was clicked.
- [WebNavigationType.formSubmitted](webnavigationtype/formsubmitted.md)
  A form was submitted.
- [WebNavigationType.backForward](webnavigationtype/backforward.md)
  The user clicked back or forward button.
- [WebNavigationType.reload](webnavigationtype/reload.md)
  The user hit the reload button.
- [WebNavigationType.formResubmitted](webnavigationtype/formresubmitted.md)
  A form was resubmitted (through a back, forward or reload action).
- [WebNavigationType.other](webnavigationtype/other.md)
  Navigation is taking place for some other reason.
### Initializers
- [init?(rawValue: Int)](webnavigationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class WebView](webview-swift.class.md)
  `WebView` is the core view class in the WebKit framework that manages interactions between the `WebFrame` and `WebFrameView` classes. To embed web content in your application, you just create a `WebView` object, attach it to a window, and send a [`load(_:)`](webframe/load(_:)-47p2s.md) message to its main frame.
- [enum WebViewInsertAction](webviewinsertaction.md)
  The type of user action that initiated a delegate message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webnavigationtype)*