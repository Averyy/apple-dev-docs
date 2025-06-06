# webExtensionController(_:promptForPermissionMatchPatterns:in:for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Called when an extension context requests access to a set of match patterns.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webExtensionController(_ controller: WKWebExtensionController, promptForPermissionMatchPatterns matchPatterns: Set<WKWebExtension.MatchPattern>, in tab: (any WKWebExtensionTab)?, for extensionContext: WKWebExtensionContext) async -> (Set<WKWebExtension.MatchPattern>, Date?)
```

#### Discussion

This method should be implemented by the app to prompt the user for permission and call the completion handler with the set of match patterns that were granted access to and an optional expiration date. If not implemented or the completion handler is not called within a reasonable amount of time, the request is assumed to have been denied. The expiration date can be used to specify when the match patterns expire. If `nil`, match patterns are assumed to not expire.

## Parameters

- `controller`: The web extension controller that is managing the extension.
- `matchPatterns`: The set of match patterns that the extension is requesting access to.
- `tab`: The tab in which the extension is running, or \c nil if the request is not specific to a tab.
- `extensionContext`: The context in which the web extension is running.
- `completionHandler`: A block to be called with the set of allowed match patterns and an optional expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontrollerdelegate/webextensioncontroller(_:promptforpermissionmatchpatterns:in:for:completionhandler:))*