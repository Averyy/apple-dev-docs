# setReaderModeActive(_:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to set the reader mode for the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func setReaderModeActive(_ active: Bool, for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func setReaderModeActive(_ active: Bool, for context: WKWebExtensionContext) async throws
```

```objc
- (void) setReaderModeActive:(BOOL) active forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

No action is performed if not implemented.

## Parameters

- `active`: A boolean value indicating whether to activate reader mode.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

### Related Documentation
- [func isReaderModeAvailable(for: WKWebExtensionContext) -> Bool](./isreadermodeavailable%28for%29.md)
  Called to check if reader mode is available for the tab.
- [func isReaderModeActive(for: WKWebExtensionContext) -> Bool](./isreadermodeactive%28for%29.md)
  Called to check if the tab is currently showing reader mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/setreadermodeactive(_:for:completionhandler:))*