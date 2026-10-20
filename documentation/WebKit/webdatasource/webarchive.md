# webArchive

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A web archive representing the data source, its subresources, and subframes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var webArchive: WebArchive! { get }
```

```objc
@property (nonatomic, strong, readonly) WebArchive * webArchive;
```

#### Discussion

In the case of HTML, if the current content is preferred, then send [`webArchive`](./webarchive.md) to the appropriate DOM object.

## See Also

### Related Documentation
- [var mainResource: WebResource!](./mainresource.md)
  A`WebResource` object representing the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/webarchive)*