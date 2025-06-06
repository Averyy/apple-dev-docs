# matches(_:options:)

**Framework**: Webkit  
**Kind**: method

Matches the receiver pattern against the specified URL with options.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func matches(_ url: URL?, options: WKWebExtension.MatchPattern.Options = []) -> Bool
```

#### Return Value

A Boolean value indicating if the pattern matches the specified URL.

## Parameters

- `url`: The URL to match against the receiver pattern.
- `options`: The options to use while matching.

## See Also

- [func matches(URL?) -> Bool](wkwebextension/matchpattern/matches(_:)-471rf.md)
  Matches the receiver pattern against the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/matches(_:options:)-5wo3g)*