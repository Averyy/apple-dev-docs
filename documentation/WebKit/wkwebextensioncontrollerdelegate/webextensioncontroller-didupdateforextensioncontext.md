# webExtensionController(_:didUpdate:forExtensionContext:)

**Framework**: WebKit  
**Kind**: method

Called when an action’s properties are updated.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webExtensionController(_ controller: WKWebExtensionController, didUpdate action: WKWebExtension.Action, forExtensionContext context: WKWebExtensionContext)
```

#### Discussion

This method is called when an action’s properties are updated and should be reflected in the app’s user interface.

The app should ensure that any visible changes, such as icons and labels, are updated accordingly.

## Parameters

- `controller`: The web extension controller initiating the request.
- `action`: The web extension action whose properties are updated.
- `context`: The context within which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontrollerdelegate/webextensioncontroller(_:didupdate:forextensioncontext:))*