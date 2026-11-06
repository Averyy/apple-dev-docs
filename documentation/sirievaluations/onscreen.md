# OnScreen

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

An expectation that specific app entities are onscreen.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct OnScreen
```

## Overview

Use `OnScreen` to check that an entity is in the onscreen context Siri captures for a turn. `OnScreen` doesn’t show the entity itself, so before the evaluation runs, make sure your app is displaying it. For example, run an App Intent that opens the screen that shows the entity and then run the evaluation.

Unlike [`Finds`](./finds.md), `OnScreen` matches by identity only and doesn’t use property constraints like `.expect(title:)`. Write an empty entity definition to match any entity of that type, or call [`expectIdentifier(_:)`](../AppIntentsTesting/appentitydefinition/expectidentifier%28_%29.md) to name a specific one.

The following example shows a turn that expects a specific quiz topic to be onscreen:

```swift
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")
let quizTopicEntity = quizExampleIntents.entities["QuizTopicEntity"]

// The app is already showing the topic list.
UserTurn("Which quizzes are available in QuizExample?") {
    OnScreen {
        quizTopicEntity.expectIdentifier("Science")
    }
}
```

## Topics

### Creating an onscreen expectation
- [init(() -> [any ResolvableAppEntityExpectation])](./onscreen/init%28_%29.md)
  Creates an expectation that each entity in the block is onscreen.
- [enum OnScreenEntityExpectationBuilder](./onscreenentityexpectationbuilder.md)
  A result builder that collects the entities an onscreen expectation requires.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Expectations
- [struct Calls](./calls.md)
  An expectation that Siri calls, or doesn’t call, a set of intents during a turn or scenario.
- [struct Finds](./finds.md)
  An expectation that Siri surfaces specific app entities by search or resolution.
- [struct Loads](./loads.md)
  An expectation that Siri loads specific app skills.
- [struct SiriResponse](./siriresponse.md)
  An expectation that the reply Siri gives contains specific text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/onscreen)*