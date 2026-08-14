# WKWebExtension.MatchPattern.Options

**Framework**: WebKit  
**Kind**: struct

Constants used by [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) to indicate matching options.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct Options
```

## Topics

### Initializers
- [init(rawValue: UInt)](wkwebextension/matchpattern/options/init(rawvalue:).md)
### Type Properties
- [static var ignorePaths: WKWebExtension.MatchPattern.Options](wkwebextension/matchpattern/options/ignorepaths.md)
  Indicates that the host components should be ignored while matching.
- [static var ignoreSchemes: WKWebExtension.MatchPattern.Options](wkwebextension/matchpattern/options/ignoreschemes.md)
  Indicates that the scheme components should be ignored while matching.
- [static var matchBidirectionally: WKWebExtension.MatchPattern.Options](wkwebextension/matchpattern/options/matchbidirectionally.md)
  Indicates that two patterns should be checked in either direction while matching.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/options)*