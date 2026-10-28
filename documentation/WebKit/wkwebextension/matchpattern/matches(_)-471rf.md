# matches(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Matches the receiver pattern against the specified URL.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func matches(_ url: URL?) -> Bool
```

```objc
- (BOOL) matchesURL:(NSURL *) url;
```

## Return Value

A Boolean value indicating if the pattern matches the specified URL.

## Parameters

- `url`: The URL to match against the receiver pattern.

## See Also

### Related Documentation
- [func matches(URL?, options: WKWebExtension.MatchPattern.Options) -> Bool](./matches%28_,options%29-5wo3g.md)
  Matches the receiver pattern against the specified URL with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/matches(_:)-471rf)*