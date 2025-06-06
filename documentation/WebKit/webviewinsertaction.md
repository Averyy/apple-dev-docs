# WebViewInsertAction

**Framework**: Webkit  
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

## See Also

- [enum WebNavigationType](webnavigationtype.md)
  Possible values for the [`WebActionNavigationTypeKey`](webactionnavigationtypekey.md) key that appears in an action dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webviewinsertaction)*