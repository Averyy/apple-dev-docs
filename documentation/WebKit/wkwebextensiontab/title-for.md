# title(for:)

**Framework**: WebKit  
**Kind**: method

Called when the title of the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func title(for context: WKWebExtensionContext) -> String?
```

#### Discussion

Defaults to [`title`](wkwebview/title.md) of the tab’s web view if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/title(for:))*