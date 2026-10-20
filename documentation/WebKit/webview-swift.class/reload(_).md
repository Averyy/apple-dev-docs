# reload(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that reloads the current page.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func reload(_ sender: Any?)
```

```objc
- (void) reload:(id) sender;
```

## Parameters

- `sender`: The object that sent this message.

## See Also

### Related Documentation
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](./resourceloaddelegate.md)
  The receiver’s resource load delegate.
### Loading Content
- [func stopLoading(Any?)](./stoploading%28_%29.md)
  An action method that stops the loading of any web frame content managed by the receiver.
- [func takeStringURLFrom(Any?)](./takestringurlfrom%28_%29.md)
  Sets the receiver’s current location by obtaining a URL string from the sender.
- [func reloadFromOrigin(Any?)](./reloadfromorigin%28_%29.md)
  Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.
- [var estimatedProgress: Double](./estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/reload(_:))*