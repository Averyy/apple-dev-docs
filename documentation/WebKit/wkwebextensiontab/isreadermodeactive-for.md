# isReaderModeActive(for:)

**Framework**: WebKit  
**Kind**: method

Called to check if the tab is currently showing reader mode.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func isReaderModeActive(for context: WKWebExtensionContext) -> Bool
```

#### Discussion

Defaults to `NO` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

- [func isReaderModeAvailable(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/isreadermodeavailable(for:).md)
  Called to check if reader mode is available for the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/isreadermodeactive(for:))*