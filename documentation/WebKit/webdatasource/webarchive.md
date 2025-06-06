# webArchive

**Framework**: Webkit  
**Kind**: property

A web archive representing the data source, its subresources, and subframes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var webArchive: WebArchive! { get }
```

#### Discussion

In the case of HTML, if the current content is preferred, then send [`webArchive`](webdatasource/webarchive.md) to the appropriate DOM object.

## See Also

- [var mainResource: WebResource!](webdatasource/mainresource.md)
  A`WebResource` object representing the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/webarchive)*