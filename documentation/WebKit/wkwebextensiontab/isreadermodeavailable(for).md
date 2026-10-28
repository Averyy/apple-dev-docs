# isReaderModeAvailable(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to check if reader mode is available for the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func isReaderModeAvailable(for context: WKWebExtensionContext) -> Bool
```

```objc
- (BOOL) isReaderModeAvailableForWebExtensionContext:(WKWebExtensionContext *) context;
```

## Discussion

Defaults to `NO` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

### Related Documentation
- [func isReaderModeActive(for: WKWebExtensionContext) -> Bool](./isreadermodeactive%28for%29.md)
  Called to check if the tab is currently showing reader mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/isreadermodeavailable(for:))*