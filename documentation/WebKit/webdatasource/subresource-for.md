# subresource(for:)

**Framework**: Webkit  
**Kind**: method

Returns a subresource for the given URL.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func subresource(for URL: URL!) -> WebResource!
```

#### Return Value

The subresource for `URL` or `nil` if the data source hasn’t finished downloading the subresource.

## Parameters

- `URL`: The subresource’s URL.

## See Also

- [var mainResource: WebResource!](webdatasource/mainresource.md)
  A`WebResource` object representing the data source.
- [func addSubresource(WebResource!)](webdatasource/addsubresource(_:).md)
  Adds a resource to the data source’s list of subresources.
- [var subresources: [Any]!](webdatasource/subresources.md)
  The data source’s subresources that have finished downloading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/subresource(for:))*