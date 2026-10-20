# WKWebExtension.MatchPattern.Options

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Constants used by [`WKWebExtension.MatchPattern`](../matchpattern.md) to indicate matching options.

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

```c
enum WKWebExtensionMatchPatternOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
### Type Properties
- [static var ignorePaths: WKWebExtension.MatchPattern.Options](./options/ignorepaths.md)
  Indicates that the host components should be ignored while matching.
- [static var ignoreSchemes: WKWebExtension.MatchPattern.Options](./options/ignoreschemes.md)
  Indicates that the scheme components should be ignored while matching.
- [static var matchBidirectionally: WKWebExtension.MatchPattern.Options](./options/matchbidirectionally.md)
  Indicates that two patterns should be checked in either direction while matching.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/options)*