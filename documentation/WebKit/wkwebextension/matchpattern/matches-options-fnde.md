# matches(_:options:)

**Framework**: Webkit  
**Kind**: method

Matches the receiver pattern against the specified pattern with options.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func matches(_ pattern: WKWebExtension.MatchPattern?, options: WKWebExtension.MatchPattern.Options = []) -> Bool
```

#### Return Value

A Boolean value indicating if the receiver pattern matches the specified pattern.

## Parameters

- `pattern`: The pattern to match against the receiver pattern.
- `options`: The options to use while matching.

## See Also

- [func matches(WKWebExtension.MatchPattern?) -> Bool](wkwebextension/matchpattern/matches(_:)-4d84f.md)
  Matches the receiver pattern against the specified pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/matches(_:options:)-fnde)*