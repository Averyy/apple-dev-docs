# pendingURL(for:)

**Framework**: WebKit  
**Kind**: method

Called when the pending URL of the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func pendingURL(for context: WKWebExtensionContext) -> URL?
```

#### Discussion

The pending URL is the URL of a page that is in the process of loading. If there is no pending URL, return `nil`.

Defaults to `nil` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/pendingurl(for:))*