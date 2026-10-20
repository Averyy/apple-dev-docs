# UIWebViewDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The `UIWebViewDelegate` protocol defines methods that a delegate of a [`UIWebView`](./uiwebview.md) object can optionally implement to intervene when web content is loaded.

**Availability**:
- iOS
- iPadOS

## Declaration

```swift
@MainActor
protocol UIWebViewDelegate : NSObjectProtocol
```

```objc
@protocol UIWebViewDelegate <NSObject>
```

#### Overview

> ❗ **Important**:  Before releasing an instance of `UIWebView` for which you have set a delegate, you must first set the `UIWebView` delegate property to `nil` before disposing of the `UIWebView` instance. This can be done, for example, in the dealloc method where you dispose of the `UIWebView`.

## Topics

### Deprecated
- [func webView(UIWebView, shouldStartLoadWith: URLRequest, navigationType: UIWebView.NavigationType) -> Bool](./uiwebviewdelegate/webview%28_,shouldstartloadwith,navigationtype%29.md)
  Sent before a web view begins loading a frame.
- [func webViewDidStartLoad(UIWebView)](./uiwebviewdelegate/webviewdidstartload%28_%29.md)
  Sent after a web view starts loading a frame.
- [func webViewDidFinishLoad(UIWebView)](./uiwebviewdelegate/webviewdidfinishload%28_%29.md)
  Sent after a web view finishes loading a frame.
- [func webView(UIWebView, didFailLoadWithError: any Error)](./uiwebviewdelegate/webview%28_,didfailloadwitherror%29.md)
  Sent if a web view failed to load a frame.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to web view changes
- [var delegate: (any UIWebViewDelegate)?](./uiwebview/delegate.md)
  The receiver’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate)*