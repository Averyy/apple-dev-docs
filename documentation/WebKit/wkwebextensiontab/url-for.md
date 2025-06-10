# url(for:)

**Framework**: WebKit  
**Kind**: method

Called when the URL of the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func url(for context: WKWebExtensionContext) -> URL?
```

#### Discussion

Defaults to `URL` of the tab’s web view if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/url(for:))*