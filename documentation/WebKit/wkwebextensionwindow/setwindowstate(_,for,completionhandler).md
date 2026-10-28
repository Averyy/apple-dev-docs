# setWindowState(_:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to set the state of the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func setWindowState(_ state: WKWebExtension.WindowState, for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func setWindowState(_ state: WKWebExtension.WindowState, for context: WKWebExtensionContext) async throws
```

```objc
- (void) setWindowState:(WKWebExtensionWindowState) state forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

The implementation of [`windowState(for:)`](./windowstate%28for%29.md) is a prerequisite.

Without it, this method will not be called.

## Parameters

- `state`: The new state of the window.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

### Related Documentation
- [func windowState(for: WKWebExtensionContext) -> WKWebExtension.WindowState](./windowstate%28for%29.md)
  Called when the state of the window is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/setwindowstate(_:for:completionhandler:))*