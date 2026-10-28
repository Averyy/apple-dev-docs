# setPinned(_:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to set the pinned state of the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func setPinned(_ pinned: Bool, for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func setPinned(_ pinned: Bool, for context: WKWebExtensionContext) async throws
```

```objc
- (void) setPinned:(BOOL) pinned forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

This is equivalent to the user selecting to pin or unpin the tab through a menu item. When a tab is pinned, it should be moved to the front of the tab bar and usually reduced in size. When a tab is unpinned, it should be restored to a normal size and position in the tab bar. No action is performed if not implemented.

## Parameters

- `pinned`: A boolean value indicating whether to pin the tab.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

### Related Documentation
- [func isPinned(for: WKWebExtensionContext) -> Bool](./ispinned%28for%29.md)
  Called when the pinned state of the tab is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/setpinned(_:for:completionhandler:))*