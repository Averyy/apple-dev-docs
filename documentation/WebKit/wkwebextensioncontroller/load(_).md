# load(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Loads the specified extension context.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func load(_ extensionContext: WKWebExtensionContext) throws
```

```objc
- (BOOL) loadExtensionContext:(WKWebExtensionContext *) extensionContext error:(NSError **) error;
```

#### Discussion

Causes the context to start, loading any background content, and injecting any content into relevant tabs.

## See Also

### Related Documentation
- [func load(WKWebExtensionContext) throws](./load%28_%29.md)
  Loads the specified extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/load(_:))*