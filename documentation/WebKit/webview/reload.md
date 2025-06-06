# reload(_:)

**Framework**: Webkit  
**Kind**: method

An action method that reloads the current page.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func reload(_ sender: Any?)
```

## Parameters

- `sender`: The object that sent this message.

## See Also

- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](webview/resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [func stopLoading(Any?)](webview/stoploading(_:).md)
  An action method that stops the loading of any web frame content managed by the receiver.
- [func takeStringURLFrom(Any?)](webview/takestringurlfrom(_:).md)
  Sets the receiver’s current location by obtaining a URL string from the sender.
- [func reloadFromOrigin(Any?)](webview/reloadfromorigin(_:).md)
  Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.
- [var estimatedProgress: Double](webview/estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/reload(_:))*