# openWindows

**Framework**: WebKit  
**Kind**: property

The open windows that are exposed to this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var openWindows: [any WKWebExtensionWindow] { get }
```

#### Discussion

Provides the windows that are open and visible to the extension, as updated by the [`didOpenWindow(_:)`](wkwebextensioncontext/didopenwindow(_:).md) and [`didCloseWindow(_:)`](wkwebextensioncontext/didclosewindow(_:).md) methods.

Initially populated by the windows returned by the extension controller delegate method [`webExtensionController(_:openWindowsFor:)`](wkwebextensioncontrollerdelegate/webextensioncontroller(_:openwindowsfor:).md).

## See Also

- [func didOpenWindow(any WKWebExtensionWindow)](wkwebextensioncontext/didopenwindow(_:).md)
  Called by the app when a new window is opened to fire appropriate events with only this extension.
- [func didCloseWindow(any WKWebExtensionWindow)](wkwebextensioncontext/didclosewindow(_:).md)
  Called by the app when a window is closed to fire appropriate events with only this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/openwindows)*