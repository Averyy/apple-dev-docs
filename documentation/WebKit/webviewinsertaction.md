# WebViewInsertAction

**Framework**: WebKit  
**Kind**: enum

The type of user action that initiated a delegate message.

**Availability**:
- macOS 10.3+

## Declaration

```swift
enum WebViewInsertAction
```

## Topics

### Constants
- [WebViewInsertAction.typed](webviewinsertaction/typed.md)
  Indicates the user inserted content by typing.
- [WebViewInsertAction.pasted](webviewinsertaction/pasted.md)
  Indicates the user inserted content by pasting.
- [WebViewInsertAction.dropped](webviewinsertaction/dropped.md)
  Indicates the user inserted content by dropping.
### Initializers
- [init?(rawValue: Int)](webviewinsertaction/init(rawvalue:).md)

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
- [enum WebNavigationType](webnavigationtype.md)
  Possible values for the [`WebActionNavigationTypeKey`](webactionnavigationtypekey.md) key that appears in an action dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webviewinsertaction)*