# extensions

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A set of all the currently loaded extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var extensions: Set<WKWebExtension> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<WKWebExtension *> * extensions;
```

## See Also

### Related Documentation
- [var extensionContexts: Set<WKWebExtensionContext>](./extensioncontexts.md)
  A set of all the currently loaded extension contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/extensions)*