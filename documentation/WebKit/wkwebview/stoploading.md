# stopLoading(_:)

**Framework**: WebKit  
**Kind**: method

Stops loading all resources on the current page.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func stopLoading(_ sender: Any?)
```

#### Discussion

Make this method the action of any controls that stop the loading of your web content. Connect your controls to this method programmatically or in Interface Builder.

## Parameters

- `sender`: The object that sent the message.

## See Also

- [func reload() -> WKNavigation?](wkwebview/reload.md)
  Reloads the current webpage.
- [func reload(Any?)](wkwebview/reload(_:).md)
  Reloads the current webpage.
- [func reloadFromOrigin() -> WKNavigation?](wkwebview/reloadfromorigin.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func reloadFromOrigin(Any?)](wkwebview/reloadfromorigin(_:).md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func stopLoading()](wkwebview/stoploading.md)
  Stops loading all resources on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/stoploading(_:))*