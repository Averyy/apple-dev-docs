# matchBidirectionally

**Framework**: WebKit  
**Kind**: property  
**Role**: Type Property

Indicates that two patterns should be checked in either direction while matching.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
static var matchBidirectionally: WKWebExtension.MatchPattern.Options { get }
```

```c
WKWebExtensionMatchPatternOptionsMatchBidirectionally
```

## Discussion

For example, A matches B, or B matches A. Invalid for matching URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/options/matchbidirectionally)*