# takeStringURLFrom(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s current location by obtaining a URL string from the sender.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func takeStringURLFrom(_ sender: Any?)
```

```objc
- (void) takeStringURLFrom:(id) sender;
```

#### Discussion

This method sets the receiver’s current location to the value obtained by sending a `stringValue` message to `sender`, then starts loading the URL returned by `sender`.

## Parameters

- `sender`: The object that sent this message.

## See Also

### Related Documentation
- [func load(URLRequest!)](../webframe/load%28_%29-47p2s.md)
  Connects to a given URL by initiating an asynchronous client request.
### Loading Content
- [func stopLoading(Any?)](./stoploading%28_%29.md)
  An action method that stops the loading of any web frame content managed by the receiver.
- [func reload(Any?)](./reload%28_%29.md)
  An action method that reloads the current page.
- [func reloadFromOrigin(Any?)](./reloadfromorigin%28_%29.md)
  Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.
- [var estimatedProgress: Double](./estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/takestringurlfrom(_:))*