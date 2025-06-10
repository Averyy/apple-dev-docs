# detectWebpageLocale(for:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Called to detect the locale of the webpage currently loaded in the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func detectWebpageLocale(for context: WKWebExtensionContext) async throws -> Locale?
```

#### Discussion

No action is performed if not implemented.

## Parameters

- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. The block takes two arguments: the detected locale (or   if the locale is unknown) and an error, which should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/detectwebpagelocale(for:completionhandler:))*