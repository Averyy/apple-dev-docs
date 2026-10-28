# parentTab(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when the parent tab for the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func parentTab(for context: WKWebExtensionContext) -> (any WKWebExtensionTab)?
```

```objc
- (id<WKWebExtensionTab>) parentTabForWebExtensionContext:(WKWebExtensionContext *) context;
```

## Discussion

Defaults to `nil` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

### Related Documentation
- [func setParentTab((any WKWebExtensionTab)?, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](./setparenttab%28_,for,completionhandler%29.md)
  Called to set or clear the parent tab for the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/parenttab(for:))*