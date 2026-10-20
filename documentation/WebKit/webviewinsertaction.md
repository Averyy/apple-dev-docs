# WebViewInsertAction

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

The type of user action that initiated a delegate message.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
enum WebViewInsertAction
```

```c
enum WebViewInsertAction : NSInteger;
```

## Topics

### Constants
- [WebViewInsertAction.typed](./webviewinsertaction/typed.md)
  Indicates the user inserted content by typing.
- [WebViewInsertAction.pasted](./webviewinsertaction/pasted.md)
  Indicates the user inserted content by pasting.
- [WebViewInsertAction.dropped](./webviewinsertaction/dropped.md)
  Indicates the user inserted content by dropping.
### Initializers
- [init?(rawValue: Int)](./webviewinsertaction/init%28rawvalue%29.md)

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
- [enum WebNavigationType](./webnavigationtype.md)
  Possible values for the [`WebActionNavigationTypeKey`](./webactionnavigationtypekey.md) key that appears in an action dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webviewinsertaction)*