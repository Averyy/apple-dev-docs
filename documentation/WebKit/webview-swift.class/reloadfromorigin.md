# reloadFromOrigin(_:)

**Framework**: WebKit  
**Kind**: method

Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func reloadFromOrigin(_ sender: Any?)
```

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func reloadFromOrigin()](webframe/reloadfromorigin.md)
  Performs an end-to-end revalidation using cache-validating conditionals if possible.
- [func stopLoading(Any?)](webview-swift.class/stoploading(_:).md)
  An action method that stops the loading of any web frame content managed by the receiver.
- [func takeStringURLFrom(Any?)](webview-swift.class/takestringurlfrom(_:).md)
  Sets the receiver’s current location by obtaining a URL string from the sender.
- [func reload(Any?)](webview-swift.class/reload(_:).md)
  An action method that reloads the current page.
- [var estimatedProgress: Double](webview-swift.class/estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/reloadfromorigin(_:))*