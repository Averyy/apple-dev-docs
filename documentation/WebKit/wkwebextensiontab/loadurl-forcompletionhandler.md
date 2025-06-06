# loadURL(_:for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Called to load a URL in the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func loadURL(_ url: URL, for context: WKWebExtensionContext) async throws
```

#### Discussion

If the tab is already loading a page, calling this method should stop the current page from loading and start loading the new URL. Loads the URL in the tab’s web view via [`load(_:)`](wkwebview/load(_:).md) if not implemented.

## Parameters

- `url`: The URL to be loaded in the tab.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/loadurl(_:for:completionhandler:))*