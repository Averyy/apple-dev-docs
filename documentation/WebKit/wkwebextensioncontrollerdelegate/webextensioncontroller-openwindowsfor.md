# webExtensionController(_:openWindowsFor:)

**Framework**: WebKit  
**Kind**: method

Called when an extension context requests the list of ordered open windows.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webExtensionController(_ controller: WKWebExtensionController, openWindowsFor extensionContext: WKWebExtensionContext) -> [any WKWebExtensionWindow]
```

#### Discussion

This method should be implemented by the app to provide the extension with the ordered open windows. Depending on your app’s requirements, you may return different windows for each extension or the same windows for all extensions. The first window in the returned array must correspond to the currently focused window and match the result of [`webExtensionController(_:focusedWindowFor:)`](wkwebextensioncontrollerdelegate/webextensioncontroller(_:focusedwindowfor:).md).

If [`webExtensionController(_:focusedWindowFor:)`](wkwebextensioncontrollerdelegate/webextensioncontroller(_:focusedwindowfor:).md) returns `nil`, indicating that no window has focus or the focused window is not visible to the extension, the first window in the list returned by this method will be considered the presumed focused window. An empty result indicates no open windows are available for the extension. Defaults to an empty array if not implemented.

## Parameters

- `controller`: The web extension controller that is managing the extension.
- `extensionContext`: The context in which the web extension is running.

## See Also

- [func webExtensionController(WKWebExtensionController, focusedWindowFor: WKWebExtensionContext) -> (any WKWebExtensionWindow)?](wkwebextensioncontrollerdelegate/webextensioncontroller(_:focusedwindowfor:).md)
  Called when an extension context requests the currently focused window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontrollerdelegate/webextensioncontroller(_:openwindowsfor:))*