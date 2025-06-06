# UIWebViewDelegate

**Framework**: UIKit  
**Kind**: protocol

The `UIWebViewDelegate` protocol defines methods that a delegate of a [`UIWebView`](uiwebview.md) object can optionally implement to intervene when web content is loaded.

**Availability**:
- iOS ?+
- iPadOS ?+

## Declaration

```swift
@MainActor
protocol UIWebViewDelegate : NSObjectProtocol
```

#### Overview

> ❗ **Important**:  Before releasing an instance of `UIWebView` for which you have set a delegate, you must first set the `UIWebView` delegate property to `nil` before disposing of the `UIWebView` instance. This can be done, for example, in the dealloc method where you dispose of the `UIWebView`.

 Before releasing an instance of `UIWebView` for which you have set a delegate, you must first set the `UIWebView` delegate property to `nil` before disposing of the `UIWebView` instance. This can be done, for example, in the dealloc method where you dispose of the `UIWebView`.

## Topics

### Loading Content
- [func webView(UIWebView, shouldStartLoadWith: URLRequest, navigationType: UIWebView.NavigationType) -> Bool](uiwebviewdelegate/webview(_:shouldstartloadwith:navigationtype:).md)
  Sent before a web view begins loading a frame.
- [func webViewDidStartLoad(UIWebView)](uiwebviewdelegate/webviewdidstartload(_:).md)
  Sent after a web view starts loading a frame.
- [func webViewDidFinishLoad(UIWebView)](uiwebviewdelegate/webviewdidfinishload(_:).md)
  Sent after a web view finishes loading a frame.
- [func webView(UIWebView, didFailLoadWithError: any Error)](uiwebviewdelegate/webview(_:didfailloadwitherror:).md)
  Sent if a web view failed to load a frame.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UIWebViewDelegate)?](uiwebview/delegate.md)
  The receiver’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate)*