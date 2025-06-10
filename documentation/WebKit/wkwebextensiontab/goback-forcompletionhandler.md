# goBack(for:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Called to navigate the tab to the previous page in its history.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func goBack(for context: WKWebExtensionContext) async throws
```

#### Discussion

Navigates to the previous page in the tab’s web view via [`goBack()`](wkwebview/goback().md) if not implemented.

## Parameters

- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/goback(for:completionhandler:))*