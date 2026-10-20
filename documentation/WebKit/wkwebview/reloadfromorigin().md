# reloadFromOrigin()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func reloadFromOrigin() -> WKNavigation?
```

```objc
- (WKNavigation *) reloadFromOrigin;
```

#### Return Value

A new navigation that represents the reloaded webpage.

## See Also

### Managing the loading process
- [func reload() -> WKNavigation?](./reload%28%29.md)
  Reloads the current webpage.
- [func reload(Any?)](./reload%28_%29.md)
  Reloads the current webpage.
- [func reloadFromOrigin(Any?)](./reloadfromorigin%28_%29.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func stopLoading()](./stoploading%28%29.md)
  Stops loading all resources on the current page.
- [func stopLoading(Any?)](./stoploading%28_%29.md)
  Stops loading all resources on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/reloadfromorigin())*