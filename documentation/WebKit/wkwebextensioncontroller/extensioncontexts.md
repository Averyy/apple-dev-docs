# extensionContexts

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A set of all the currently loaded extension contexts.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var extensionContexts: Set<WKWebExtensionContext> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<WKWebExtensionContext *> * extensionContexts;
```

## See Also

### Related Documentation
- [var extensions: Set<WKWebExtension>](./extensions.md)
  A set of all the currently loaded extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/extensioncontexts)*