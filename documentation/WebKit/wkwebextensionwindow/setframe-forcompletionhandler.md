# setFrame(_:for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Called to set the frame of the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func setFrame(_ frame: CGRect, for context: WKWebExtensionContext) async throws
```

#### Discussion

On macOS, the implementation of both [`frame(for:)`](wkwebextensionwindow/frame(for:).md) and [`screenFrame(for:)`](wkwebextensionwindow/screenframe(for:).md) are prerequisites. On iOS, iPadOS, and visionOS, only [`frame(for:)`](wkwebextensionwindow/frame(for:).md) is a prerequisite. Without the respective method(s), this method will not be called.

## Parameters

- `frame`: The new frame of the window, in screen coordinates.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

- [func frame(for: WKWebExtensionContext) -> CGRect](wkwebextensionwindow/frame(for:).md)
  Called when the frame of the window is needed.
- [func screenFrame(for: WKWebExtensionContext) -> CGRect](wkwebextensionwindow/screenframe(for:).md)
  Called when the screen frame containing the window is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/setframe(_:for:completionhandler:))*