# init(_:_:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a turn from an utterance and what Siri should do in response to it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(_ utterance: String, @SiriTurnExpectationBuilder _ content: () -> SiriTurnExpectationBuilder.Component)
```

## Discussion

The trailing block holds the turn’s expectations — any of `Calls`, `Finds`, `OnScreen`, `SiriResponse` and `Loads`, each graded only against this turn’s observations:

```swift
UserTurn("Create a Launch Party event tomorrow at 7 PM") {
    Calls { CreateEventIntent }
    Finds { EventEntity.expect(title: .equals("Launch Party")) }
}
```

## See Also

### Creating a user turn with expectations
- [enum SiriTurnExpectationBuilder](../siriturnexpectationbuilder.md)
  A result builder that collects the expectations you attach to a user turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/userturn/init(_:_:))*