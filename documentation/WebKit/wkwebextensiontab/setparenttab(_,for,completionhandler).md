# setParentTab(_:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to set or clear the parent tab for the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func setParentTab(_ parentTab: (any WKWebExtensionTab)?, for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func setParentTab(_ parentTab: (any WKWebExtensionTab)?, for context: WKWebExtensionContext) async throws
```

```objc
- (void) setParentTab:(id<WKWebExtensionTab>) parentTab forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

No action is performed if not implemented.

## Parameters

- `parentTab`: The tab that should be set as the parent of the tab. If \c nil is provided, the current parent tab should be cleared.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

### Related Documentation
- [func parentTab(for: WKWebExtensionContext) -> (any WKWebExtensionTab)?](./parenttab%28for%29.md)
  Called when the parent tab for the tab is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/setparenttab(_:for:completionhandler:))*