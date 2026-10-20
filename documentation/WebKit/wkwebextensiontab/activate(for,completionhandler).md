# activate(for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to activate the tab, making it frontmost.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func activate(for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func activate(for context: WKWebExtensionContext) async throws
```

```objc
- (void) activateForWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Upon activation, the tab should become the frontmost and either be the sole selected tab or be included among the selected tabs. No action is performed if not implemented.

## Parameters

- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

### Related Documentation
- [func setSelected(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](./setselected%28_,for,completionhandler%29.md)
  Called to set the selected state of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/activate(for:completionhandler:))*