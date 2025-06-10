# webExtensionController(_:openNewWindowUsing:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Called when an extension context requests a new window to be opened.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webExtensionController(_ controller: WKWebExtensionController, openNewWindowUsing configuration: WKWebExtension.WindowConfiguration, for extensionContext: WKWebExtensionContext) async throws -> (any WKWebExtensionWindow)?
```

#### Discussion

This method should be implemented by the app to handle requests to open new windows. The app can decide how to handle the process based on the provided configuration and existing windows. Once handled, the app should call the completion handler with the opened window or `nil` if the request was declined or failed. If not implemented, the extension will be unable to open new windows.

## Parameters

- `controller`: The web extension controller that is managing the extension.
- `configuration`: The configuration specifying how the new window should be created.
- `extensionContext`: The context in which the web extension is running.
- `completionHandler`: A block to be called with the newly created window or   if the window wasn’t created. An error should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontrollerdelegate/webextensioncontroller(_:opennewwindowusing:for:completionhandler:))*