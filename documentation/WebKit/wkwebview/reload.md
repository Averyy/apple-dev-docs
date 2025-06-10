# reload(_:)

**Framework**: WebKit  
**Kind**: method

Reloads the current webpage.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func reload(_ sender: Any?)
```

#### Discussion

Make this method the action of any controls that trigger a reload of your web content. Connect your controls to this method programmatically or in Interface Builder.

## Parameters

- `sender`: The object that sent the message.

## See Also

- [func reload() -> WKNavigation?](wkwebview/reload.md)
  Reloads the current webpage.
- [func reloadFromOrigin() -> WKNavigation?](wkwebview/reloadfromorigin.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func reloadFromOrigin(Any?)](wkwebview/reloadfromorigin(_:).md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func stopLoading()](wkwebview/stoploading.md)
  Stops loading all resources on the current page.
- [func stopLoading(Any?)](wkwebview/stoploading(_:).md)
  Stops loading all resources on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/reload(_:))*