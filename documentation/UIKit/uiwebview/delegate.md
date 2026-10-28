# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s delegate.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
unowned(unsafe) var delegate: (any UIWebViewDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<UIWebViewDelegate> delegate;
```

## Discussion

The delegate is sent messages when content is loading. See [`UIWebViewDelegate`](../uiwebviewdelegate.md) for the optional methods this delegate may implement.

> ❗ **Important**:  Before releasing an instance of `UIWebView` for which you have set a delegate, you must first set its delegate property to `nil`. This can be done, for example, in your dealloc method.

## See Also

### Responding to web view changes
- [protocol UIWebViewDelegate](../uiwebviewdelegate.md)
  The `UIWebViewDelegate` protocol defines methods that a delegate of a [`UIWebView`](../uiwebview.md) object can optionally implement to intervene when web content is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/delegate)*