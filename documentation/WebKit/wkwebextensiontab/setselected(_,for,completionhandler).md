# setSelected(_:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to set the selected state of the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func setSelected(_ selected: Bool, for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func setSelected(_ selected: Bool, for context: WKWebExtensionContext) async throws
```

```objc
- (void) setSelected:(BOOL) selected forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

This is equivalent to the user command-clicking on the tab to add it to or remove it from a selection.

The method should update the tab’s selection state without changing the active tab. No action is performed if not implemented.

## Parameters

- `selected`: A boolean value indicating whether to select the tab.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

### Related Documentation
- [func isSelected(for: WKWebExtensionContext) -> Bool](./isselected%28for%29.md)
  Called when the selected state of the tab is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/setselected(_:for:completionhandler:))*