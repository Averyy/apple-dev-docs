# focus(for:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Called to focus the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func focus(for context: WKWebExtensionContext) async throws
```

#### Discussion

No action is performed if not implemented.

## Parameters

- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/focus(for:completionhandler:))*