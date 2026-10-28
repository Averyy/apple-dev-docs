# unload(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Unloads the specified extension context.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func unload(_ extensionContext: WKWebExtensionContext) throws
```

```objc
- (BOOL) unloadExtensionContext:(WKWebExtensionContext *) extensionContext error:(NSError **) error;
```

## Discussion

Causes the context to stop running.

## See Also

### Related Documentation
- [func unload(WKWebExtensionContext) throws](./unload%28_%29.md)
  Unloads the specified extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/unload(_:))*