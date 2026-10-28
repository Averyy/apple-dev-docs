# subresource(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a subresource for the given URL.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func subresource(for URL: URL!) -> WebResource!
```

```objc
- (WebResource *) subresourceForURL:(NSURL *) URL;
```

## Return Value

The subresource for `URL` or `nil` if the data source hasn’t finished downloading the subresource.

## Parameters

- `URL`: The subresource’s URL.

## See Also

### Accessing subresources
- [var mainResource: WebResource!](./mainresource.md)
  A`WebResource` object representing the data source.
- [func addSubresource(WebResource!)](./addsubresource%28_%29.md)
  Adds a resource to the data source’s list of subresources.
- [var subresources: [Any]!](./subresources.md)
  The data source’s subresources that have finished downloading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/subresource(for:))*