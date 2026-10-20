# WebNavigationType

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Possible values for the [`WebActionNavigationTypeKey`](./webactionnavigationtypekey.md) key that appears in an action dictionary.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
enum WebNavigationType
```

```c
enum WebNavigationType : NSInteger;
```

## Topics

### Constants
- [WebNavigationType.linkClicked](./webnavigationtype/linkclicked.md)
  A link (an `href`) was clicked.
- [WebNavigationType.formSubmitted](./webnavigationtype/formsubmitted.md)
  A form was submitted.
- [WebNavigationType.backForward](./webnavigationtype/backforward.md)
  The user clicked back or forward button.
- [WebNavigationType.reload](./webnavigationtype/reload.md)
  The user hit the reload button.
- [WebNavigationType.formResubmitted](./webnavigationtype/formresubmitted.md)
  A form was resubmitted (through a back, forward or reload action).
- [WebNavigationType.other](./webnavigationtype/other.md)
  Navigation is taking place for some other reason.
### Initializers
- [init?(rawValue: Int)](./webnavigationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Content
- [class WebView](./webview-swift.class.md)
  `WebView` is the core view class in the WebKit framework that manages interactions between the `WebFrame` and `WebFrameView` classes. To embed web content in your application, you just create a `WebView` object, attach it to a window, and send a [`load(_:)`](./webframe/load%28_%29-47p2s.md) message to its main frame.
- [enum WebViewInsertAction](./webviewinsertaction.md)
  The type of user action that initiated a delegate message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webnavigationtype)*