# customUserAgent

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s custom user-agent string.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var customUserAgent: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * customUserAgent;
```

#### Discussion

The custom user-agent string is used for all URLs. If `nil`, then the receiver constructs a user-agent string that produces the best rendering results for each URL.

## See Also

### Getting and Setting User-agent Strings
- [func userAgent(for: URL!) -> String!](./useragent%28for%29.md)
  Returns the appropriate user-agent string for a given URL.
- [var applicationNameForUserAgent: String!](./applicationnameforuseragent.md)
  The receiver’s application name that is used in the user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/customuseragent)*