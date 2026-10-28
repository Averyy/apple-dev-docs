# matchPatternWithScheme:host:path:

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns a pattern object for the specified scheme, host, and path strings.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```objc
+ (instancetype) matchPatternWithScheme:(NSString *) scheme host:(NSString *) host path:(NSString *) path;
```

## Return Value

A pattern object, or `nil` if any of the strings are invalid.

## See Also

### Related Documentation
- [init(scheme: String, host: String, path: String) throws](../wkwebextension/matchpattern/init%28scheme,host,path%29.md)
  Returns a pattern object for the specified scheme, host, and path strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionmatchpattern/matchpatternwithscheme:host:path:)*