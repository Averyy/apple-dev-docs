# screenFrame(for:)

**Framework**: WebKit  
**Kind**: method

Called when the screen frame containing the window is needed.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
optional func screenFrame(for context: WKWebExtensionContext) -> CGRect
```

#### Discussion

Defaults to [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull) if not implemented.

## Parameters

- `context`: The context associated with the running web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/screenframe(for:))*