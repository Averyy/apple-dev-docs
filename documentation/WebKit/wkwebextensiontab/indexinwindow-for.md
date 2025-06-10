# indexInWindow(for:)

**Framework**: WebKit  
**Kind**: method

Called when the index of the tab in the window is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func indexInWindow(for context: WKWebExtensionContext) -> Int
```

#### Discussion

This method should be implemented for better performance. Defaults to the window’s [`tabs(for:)`](wkwebextensionwindow/tabs(for:).md) method to find the index if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/indexinwindow(for:))*