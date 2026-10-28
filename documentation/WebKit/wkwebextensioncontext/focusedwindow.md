# focusedWindow

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The window that currently has focus for this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
weak var focusedWindow: (any WKWebExtensionWindow)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<WKWebExtensionWindow> focusedWindow;
```

## Discussion

Provides the window that currently has focus, as set by the [`didFocusWindow(_:)`](./didfocuswindow%28_%29.md) method.

It will be `nil` if no window has focus or if a window has focus that is not visible to the extension. Initially populated by the window returned by the extension controller delegate method [`webExtensionController(_:focusedWindowFor:)`](../wkwebextensioncontrollerdelegate/webextensioncontroller%28_,focusedwindowfor%29.md).

## See Also

### Related Documentation
- [func didFocusWindow((any WKWebExtensionWindow)?)](./didfocuswindow%28_%29.md)
  Called by the app when a window gains focus to fire appropriate events with only this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/focusedwindow)*