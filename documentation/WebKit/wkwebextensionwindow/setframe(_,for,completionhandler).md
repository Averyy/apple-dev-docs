# setFrame(_:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to set the frame of the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func setFrame(_ frame: CGRect, for context: WKWebExtensionContext, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
optional func setFrame(_ frame: CGRect, for context: WKWebExtensionContext) async throws
```

```objc
- (void) setFrame:(CGRect) frame forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

On macOS, the implementation of both [`frame(for:)`](./frame%28for%29.md) and [`screenFrame(for:)`](./screenframe%28for%29.md) are prerequisites. On iOS, iPadOS, and visionOS, only [`frame(for:)`](./frame%28for%29.md) is a prerequisite. Without the respective method(s), this method will not be called.

## Parameters

- `frame`: The new frame of the window, in screen coordinates.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

### Related Documentation
- [func frame(for: WKWebExtensionContext) -> CGRect](./frame%28for%29.md)
  Called when the frame of the window is needed.
- [func screenFrame(for: WKWebExtensionContext) -> CGRect](./screenframe%28for%29.md)
  Called when the screen frame containing the window is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/setframe(_:for:completionhandler:))*