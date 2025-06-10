# addSubresource(_:)

**Framework**: WebKit  
**Kind**: method

Adds a resource to the data source’s list of subresources.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func addSubresource(_ subresource: WebResource!)
```

#### Discussion

If the data source needs to reload the resource’s URL, it loads the data from `subresource` instead of the network. For example, use this method if you want to use a previously downloaded image rather than accessing the network to reload a resource. If the data source already has a resource with the same URL as `subresource`, then this method replaces it.

## Parameters

- `subresource`: The resource to add to the data source.

## See Also

- [var mainResource: WebResource!](webdatasource/mainresource.md)
  A`WebResource` object representing the data source.
- [func subresource(for: URL!) -> WebResource!](webdatasource/subresource(for:).md)
  Returns a subresource for the given URL.
- [var subresources: [Any]!](webdatasource/subresources.md)
  The data source’s subresources that have finished downloading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/addsubresource(_:))*