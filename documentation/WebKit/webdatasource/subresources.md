# subresources

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The data source’s subresources that have finished downloading.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var subresources: [Any]! { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray * subresources;
```

## See Also

### Accessing subresources
- [var mainResource: WebResource!](./mainresource.md)
  A`WebResource` object representing the data source.
- [func addSubresource(WebResource!)](./addsubresource%28_%29.md)
  Adds a resource to the data source’s list of subresources.
- [func subresource(for: URL!) -> WebResource!](./subresource%28for%29.md)
  Returns a subresource for the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/subresources)*