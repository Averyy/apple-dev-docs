# stopLoading(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Stops loading all resources on the current page.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func stopLoading(_ sender: Any?)
```

```objc
- (void) stopLoading:(id) sender;
```

#### Discussion

Make this method the action of any controls that stop the loading of your web content. Connect your controls to this method programmatically or in Interface Builder.

## Parameters

- `sender`: The object that sent the message.

## See Also

### Managing the loading process
- [func reload() -> WKNavigation?](./reload%28%29.md)
  Reloads the current webpage.
- [func reload(Any?)](./reload%28_%29.md)
  Reloads the current webpage.
- [func reloadFromOrigin() -> WKNavigation?](./reloadfromorigin%28%29.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func reloadFromOrigin(Any?)](./reloadfromorigin%28_%29.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func stopLoading()](./stoploading%28%29.md)
  Stops loading all resources on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/stoploading(_:))*