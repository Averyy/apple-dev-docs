# matches(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Matches the receiver pattern against the specified pattern.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func matches(_ pattern: WKWebExtension.MatchPattern?) -> Bool
```

```objc
- (BOOL) matchesPattern:(WKWebExtensionMatchPattern *) pattern;
```

#### Return Value

A Boolean value indicating if the receiver pattern matches the specified pattern.

## Parameters

- `pattern`: The pattern to match against the receiver pattern.

## See Also

### Related Documentation
- [func matches(WKWebExtension.MatchPattern?, options: WKWebExtension.MatchPattern.Options) -> Bool](./matches%28_,options%29-fnde.md)
  Matches the receiver pattern against the specified pattern with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/matches(_:)-4d84f)*