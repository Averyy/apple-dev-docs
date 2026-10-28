# matches(_:options:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Matches the receiver pattern against the specified URL with options.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func matches(_ url: URL?, options: WKWebExtension.MatchPattern.Options = []) -> Bool
```

```objc
- (BOOL) matchesURL:(NSURL *) url options:(WKWebExtensionMatchPatternOptions) options;
```

## Return Value

A Boolean value indicating if the pattern matches the specified URL.

## Parameters

- `url`: The URL to match against the receiver pattern.
- `options`: The options to use while matching.

## See Also

### Related Documentation
- [func matches(URL?) -> Bool](./matches%28_%29-471rf.md)
  Matches the receiver pattern against the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/matches(_:options:)-5wo3g)*