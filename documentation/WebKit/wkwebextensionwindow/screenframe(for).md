# screenFrame(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when the screen frame containing the window is needed.

**Availability**:
- macOS 15.4+

## Declaration

```swift
optional func screenFrame(for context: WKWebExtensionContext) -> CGRect
```

```objc
- (CGRect) screenFrameForWebExtensionContext:(WKWebExtensionContext *) context;
```

## Discussion

Defaults to [`CGRectNull`](../../CoreGraphics/cgrectnull.md) if not implemented.

## Parameters

- `context`: The context associated with the running web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/screenframe(for:))*