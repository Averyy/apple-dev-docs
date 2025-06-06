# activate(for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Called to activate the tab, making it frontmost.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func activate(for context: WKWebExtensionContext) async throws
```

#### Discussion

Upon activation, the tab should become the frontmost and either be the sole selected tab or be included among the selected tabs. No action is performed if not implemented.

## Parameters

- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

- [func setSelected(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setselected(_:for:completionhandler:).md)
  Called to set the selected state of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/activate(for:completionhandler:))*