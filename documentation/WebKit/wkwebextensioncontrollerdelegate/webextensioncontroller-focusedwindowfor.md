# webExtensionController(_:focusedWindowFor:)

**Framework**: WebKit  
**Kind**: method

Called when an extension context requests the currently focused window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webExtensionController(_ controller: WKWebExtensionController, focusedWindowFor extensionContext: WKWebExtensionContext) -> (any WKWebExtensionWindow)?
```

#### Discussion

This method can be optionally implemented by the app to designate the window currently in focus to the extension.

If not implemented, the first window in the result of [`webExtensionController(_:openWindowsFor:)`](wkwebextensioncontrollerdelegate/webextensioncontroller(_:openwindowsfor:).md) is used.

## Parameters

- `controller`: The web extension controller that is managing the extension.
- `extensionContext`: The context in which the web extension is running.

## See Also

- [func webExtensionController(WKWebExtensionController, openWindowsFor: WKWebExtensionContext) -> [any WKWebExtensionWindow]](wkwebextensioncontrollerdelegate/webextensioncontroller(_:openwindowsfor:).md)
  Called when an extension context requests the list of ordered open windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontrollerdelegate/webextensioncontroller(_:focusedwindowfor:))*