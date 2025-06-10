# takeStringURLFrom(_:)

**Framework**: WebKit  
**Kind**: method

Sets the receiver’s current location by obtaining a URL string from the sender.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func takeStringURLFrom(_ sender: Any?)
```

#### Discussion

This method sets the receiver’s current location to the value obtained by sending a `stringValue` message to `sender`, then starts loading the URL returned by `sender`.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func load(URLRequest!)](webframe/load(_:)-47p2s.md)
  Connects to a given URL by initiating an asynchronous client request.
- [func stopLoading(Any?)](webview-swift.class/stoploading(_:).md)
  An action method that stops the loading of any web frame content managed by the receiver.
- [func reload(Any?)](webview-swift.class/reload(_:).md)
  An action method that reloads the current page.
- [func reloadFromOrigin(Any?)](webview-swift.class/reloadfromorigin(_:).md)
  Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.
- [var estimatedProgress: Double](webview-swift.class/estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/takestringurlfrom(_:))*