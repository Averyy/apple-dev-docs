# stopLoading(_:)

**Framework**: WebKit  
**Kind**: method

An action method that stops the loading of any web frame content managed by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func stopLoading(_ sender: Any?)
```

#### Discussion

Stops any content in the process of being loaded by the main frame or any of its children frames. Does nothing if no content is being loaded.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func takeStringURLFrom(Any?)](webview-swift.class/takestringurlfrom(_:).md)
  Sets the receiver’s current location by obtaining a URL string from the sender.
- [func reload(Any?)](webview-swift.class/reload(_:).md)
  An action method that reloads the current page.
- [func reloadFromOrigin(Any?)](webview-swift.class/reloadfromorigin(_:).md)
  Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.
- [var estimatedProgress: Double](webview-swift.class/estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/stoploading(_:))*