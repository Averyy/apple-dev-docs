# reload()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Reloads the current webpage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func reload() -> WKNavigation?
```

```objc
- (WKNavigation *) reload;
```

## Return Value

A new navigation object to represent the reload operation.

## See Also

### Managing the loading process
- [func reload(Any?)](./reload%28_%29.md)
  Reloads the current webpage.
- [func reloadFromOrigin() -> WKNavigation?](./reloadfromorigin%28%29.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func reloadFromOrigin(Any?)](./reloadfromorigin%28_%29.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func stopLoading()](./stoploading%28%29.md)
  Stops loading all resources on the current page.
- [func stopLoading(Any?)](./stoploading%28_%29.md)
  Stops loading all resources on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/reload())*