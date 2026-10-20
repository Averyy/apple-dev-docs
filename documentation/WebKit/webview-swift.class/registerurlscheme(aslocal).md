# registerURLScheme(asLocal:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Adds the specified URL scheme to the list of local schemes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
class func registerURLScheme(asLocal scheme: String!)
```

```objc
+ (void) registerURLSchemeAsLocal:(NSString *) scheme;
```

#### Discussion

You need to register a scheme as local to access resources with file URLs and to have the same security checks as a local file.

## Parameters

- `scheme`: The scheme to add to the list.

## See Also

### Registering Document Views and Representations
- [class func registerClass(AnyClass!, representationClass: AnyClass!, forMIMEType: String!)](./registerclass%28_,representationclass,formimetype%29.md)
  Specifies the view and representation objects to be used for specific MIME types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/registerurlscheme(aslocal:))*