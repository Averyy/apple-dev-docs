# indexInWindow(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when the index of the tab in the window is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func indexInWindow(for context: WKWebExtensionContext) -> Int
```

```objc
- (NSUInteger) indexInWindowForWebExtensionContext:(WKWebExtensionContext *) context;
```

## Discussion

This method should be implemented for better performance. Defaults to the window’s [`tabs(for:)`](../wkwebextensionwindow/tabs%28for%29.md) method to find the index if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/indexinwindow(for:))*