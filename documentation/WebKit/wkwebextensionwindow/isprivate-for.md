# isPrivate(for:)

**Framework**: Webkit  
**Kind**: method

Called when the private state of the window is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func isPrivate(for context: WKWebExtensionContext) -> Bool
```

#### Discussion

Defaults to `NO` if not implemented. This value is cached and will not change for the duration of the window or its contained tabs.

> **Note**: To ensure proper isolation between private and non-private data, web views associated with private data must use a different [`WKUserContentController`](wkusercontentcontroller.md). Likewise, to be identified as a private web view and to ensure that cookies and other website data are not shared, private web views must be configured to use a non-persistent [`WKWebsiteDataStore`](wkwebsitedatastore.md).

To ensure proper isolation between private and non-private data, web views associated with private data must use a different [`WKUserContentController`](wkusercontentcontroller.md). Likewise, to be identified as a private web view and to ensure that cookies and other website data are not shared, private web views must be configured to use a non-persistent [`WKWebsiteDataStore`](wkwebsitedatastore.md).

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/isprivate(for:))*