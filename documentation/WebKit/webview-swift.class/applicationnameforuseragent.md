# applicationNameForUserAgent

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s application name that is used in the user-agent string.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var applicationNameForUserAgent: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * applicationNameForUserAgent;
```

#### Discussion

The user-agent is used by websites to identify the client browser.

## See Also

### Getting and Setting User-agent Strings
- [func userAgent(for: URL!) -> String!](./useragent%28for%29.md)
  Returns the appropriate user-agent string for a given URL.
- [var customUserAgent: String!](./customuseragent.md)
  The receiver’s custom user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/applicationnameforuseragent)*