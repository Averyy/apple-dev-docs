# init(name:webFrameView:webView:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Initializes the receiver with a frame name, web frame view, and controlling web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
init!(name: String!, webFrameView view: WebFrameView!, webView: WebView!)
```

```objc
- (instancetype) initWithName:(NSString *) name webFrameView:(WebFrameView *) view webView:(WebView *) webView;
```

#### Return Value

An initialized web frame.

#### Discussion

Normally, you do not invoke this method directly. `WebView` objects automatically create the main frame and subsequent children when new content is loaded. Send a [`load(_:)`](./load%28_%29-47p2s.md) message to the main frame of a `WebView` to load web content.

This method is the designated initializer for the `WebFrame` class.

## Parameters

- `name`: The frame name. Typically a custom name or `nil` (if none is specified). It would be inappropriate to use one of the predefined frame names described in [`findNamed(_:)`](./findnamed%28_%29.md) as they have special meanings.
- `view`: The view that displays this web frame—the view associated with the receiver.
- `webView`: The parent view that manages the main frame and its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/init(name:webframeview:webview:))*