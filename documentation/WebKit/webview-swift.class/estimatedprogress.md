# estimatedProgress

**Framework**: WebKit  
**Kind**: property

An estimate, as a percentage, of the amount of content that is currently loaded.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var estimatedProgress: Double { get }
```

#### Discussion

A number ranging from `0` to `1.0` and, once a load completes, `1.0` until a new load starts, at which point it resets to `0`.

The value is an estimate based on the total number of bytes expected to be received for a document, including all its possible subresources. For more accurate load progress information, implement delegates conforming to the WebFrameLoadDelegate and WebResourceLoadDelegate informal protocols.

## See Also

- [func stopLoading(Any?)](webview-swift.class/stoploading(_:).md)
  An action method that stops the loading of any web frame content managed by the receiver.
- [func takeStringURLFrom(Any?)](webview-swift.class/takestringurlfrom(_:).md)
  Sets the receiver’s current location by obtaining a URL string from the sender.
- [func reload(Any?)](webview-swift.class/reload(_:).md)
  An action method that reloads the current page.
- [func reloadFromOrigin(Any?)](webview-swift.class/reloadfromorigin(_:).md)
  Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/estimatedprogress)*