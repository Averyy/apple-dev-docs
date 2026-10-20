# mainResource

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A`WebResource` object representing the data source.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var mainResource: WebResource! { get }
```

```objc
@property (nonatomic, strong, readonly) WebResource * mainResource;
```

## See Also

### Accessing subresources
- [func addSubresource(WebResource!)](./addsubresource%28_%29.md)
  Adds a resource to the data source’s list of subresources.
- [func subresource(for: URL!) -> WebResource!](./subresource%28for%29.md)
  Returns a subresource for the given URL.
- [var subresources: [Any]!](./subresources.md)
  The data source’s subresources that have finished downloading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/mainresource)*