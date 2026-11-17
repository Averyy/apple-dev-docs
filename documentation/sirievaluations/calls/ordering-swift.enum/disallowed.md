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

## Mentions

- [Evaluating your app’s integration with Siri](../../evaluating-your-apps-integration-with-siri.md)

## Discussion

A property of the argument or result entity itself whose name begins with `_`, or that is named `liveAppEntityFeedId`, is never relayed. On an argument, or a result Siri returned whole, a prohibition that requires such a property to have a value never matches, so it holds whatever Siri bound. On a result Siri returned as a reference or a partial, the property isn’t read, so the call can’t be ruled out and the prohibition fails. An entity nested in the argument or result keeps such properties.

## See Also

### Specifying ordering
- [Calls.Ordering.ordered](./ordered.md)
  A requirement that Siri calls the intents in the order written.
- [Calls.Ordering.unordered](./unordered.md)
  A requirement that Siri calls every intent, in any order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/calls/ordering-swift.enum/disallowed)*