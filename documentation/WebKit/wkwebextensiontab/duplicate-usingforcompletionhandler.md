# duplicate(using:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Called to duplicate the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func duplicate(using configuration: WKWebExtension.TabConfiguration, for context: WKWebExtensionContext) async throws -> (any WKWebExtensionTab)?
```

#### Discussion

This is equivalent to the user selecting to duplicate the tab through a menu item, with the specified configuration.

No action is performed if not implemented.

## Parameters

- `configuration`: The tab configuration influencing the duplicated tab’s properties.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes two arguments: the duplicated tab (or \c nil if no tab was created) and an error, which should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/duplicate(using:for:completionhandler:))*