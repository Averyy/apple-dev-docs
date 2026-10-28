# registerClass(_:representationClass:forMIMEType:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Specifies the view and representation objects to be used for specific MIME types.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
class func registerClass(_ viewClass: AnyClass!, representationClass: AnyClass!, forMIMEType MIMEType: String!)
```

```objc
+ (void) registerViewClass:(Class) viewClass representationClass:(Class) representationClass forMIMEType:(NSString *) MIMEType;
```

## Discussion

After invoking this method, when `MIMEType` content is encountered, instances of `representationClass` and `viewClass` are created to handle and display it.

## Parameters

- `viewClass`: A class conforming to the [`WebDocumentView`](../webdocumentview.md) protocol that displays the specified MIME types.
- `representationClass`: The class conforming to [`WebDocumentRepresentation`](../webdocumentrepresentation.md) protocol that represents the specified MIME types.
- `MIMEType`: The MIME type of the content.

  This may be a primary MIME type or subtype. For example, if `MIMEType` is “video/” the specified view and representation objects are used for all video types. More specific subtype mappings, such as “image/gif”, takes precedence over primary type matching, such as “image/”.

## See Also

### Registering Document Views and Representations
- [class func registerURLScheme(asLocal: String!)](./registerurlscheme%28aslocal%29.md)
  Adds the specified URL scheme to the list of local schemes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/registerclass(_:representationclass:formimetype:))*