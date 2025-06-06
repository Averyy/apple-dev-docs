# shouldBypassPermissions(for:)

**Framework**: Webkit  
**Kind**: method

Called to determine if the tab should bypass host permission checks.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func shouldBypassPermissions(for context: WKWebExtensionContext) -> Bool
```

#### Discussion

This method allows the app to dynamically control whether a tab can bypass standard host permission checks.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/shouldbypasspermissions(for:))*