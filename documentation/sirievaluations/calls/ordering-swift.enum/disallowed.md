# Calls.Ordering.disallowed

**Framework**: Siri Evaluations  
**Kind**: case  
**Role**: Case

A requirement that Siri doesn’t call any of the intents.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
case disallowed
```

## Discussion

A property of the argument or result entity itself whose name begins with `_`, or that is named `liveAppEntityFeedId`, is never relayed, so a prohibition that requires it to have a value never matches, and holds whatever Siri bound. An entity nested in the argument or result keeps such properties.

## See Also

### Specifying ordering
- [Calls.Ordering.ordered](./ordered.md)
  A requirement that Siri calls the intents in the order written.
- [Calls.Ordering.unordered](./unordered.md)
  A requirement that Siri calls every intent, in any order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/calls/ordering-swift.enum/disallowed)*