# webView(_:didReceiveTitle:for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when the page title of a frame loads or changes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, didReceiveTitle title: String!, for frame: WebFrame!)
```

```objc
- (void) webView:(WebView *) sender didReceiveTitle:(NSString *) title forFrame:(WebFrame *) frame;
```

## Discussion

This method may be invoked multiple times before all resources for `frame` are completely loaded. Delegates can implement this message to display the page title to the user.

## Parameters

- `sender`: The web view containing the frame.
- `title`: The newly loaded title.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didreceivetitle:for:))*