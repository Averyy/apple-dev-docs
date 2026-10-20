# reload(fromOrigin:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to reload the current page in the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func reload(fromOrigin: Bool, for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func reload(fromOrigin: Bool, for context: WKWebExtensionContext) async throws
```

```objc
- (void) reloadFromOrigin:(BOOL) fromOrigin forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Reloads the tab’s web view via [`reload()`](../wkwebview/reload%28%29.md) or [`reloadFromOrigin()`](../wkwebview/reloadfromorigin%28%29.md) if not implemented.

## Parameters

- `fromOrigin`: A boolean value indicating whether to reload the tab from the origin, bypassing the cache.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/reload(fromorigin:for:completionhandler:))*