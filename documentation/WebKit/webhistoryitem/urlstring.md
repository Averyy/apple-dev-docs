# urlString

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The string representation of the URL for the receiver’s page.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var urlString: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * URLString;
```

## Discussion

This URL may differ from the original URL if the page was, for example, redirected to a new location.

## See Also

### Getting URL information
- [var originalURLString: String!](./originalurlstring.md)
  The string representation of the original URL for the receiver’s page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitem/urlstring)*