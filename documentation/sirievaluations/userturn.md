# UserTurn

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

A single utterance a person says, with what you expect Siri to do in response.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct UserTurn
```

## Overview

A user turn is one thing the person says to Siri. Create a turn with only an utterance to give Siri context for a later turn, or add a closure of expectations to check what Siri does in response. A turn accepts [`Calls`](./calls.md), [`Finds`](./finds.md), [`OnScreen`](./onscreen.md), [`Loads`](./loads.md), and [`SiriResponse`](./siriresponse.md) expectations. It compares them only with that turn, so something Siri does in another turn can’t satisfy them.

Each turn has an [`id`](./userturn/id.md). After a run, the framework matches each action Siri performs to its turn by identifier. A run that stops early never checks one turn’s expectations against another turn.

The following shows a turn that expects Siri to start a science quiz, not to create a reminder, and to include the name of the topic in its reply:

```swift
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")
let startQuizIntent = quizExampleIntents.intents["StartQuizIntent"]
let createQuizReminderIntent = quizExampleIntents.intents["CreateQuizReminderIntent"]

UserTurn("In QuizExample, start a science quiz with 5 questions") {
    Calls {
        startQuizIntent
            .expect(topic: .equals("Science"))
    }

    // Fails if Siri runs or asks the person to confirm the intent.
    Calls(.disallowed) {
        createQuizReminderIntent
    }

    // Checks if the reply names the topic.
    SiriResponse(.contains("Science"))
}
```

Place turns in a [`SiriScenario`](./siriscenario.md) to run them as a conversation.

## Topics

### Creating a user turn
- [init(String)](./userturn/init%28_%29.md)
  Creates a turn with no expectations of its own.
### Creating a user turn with expectations
- [init(String, () -> SiriTurnExpectationBuilder.Component)](./userturn/init%28_,_%29.md)
  Creates a turn from an utterance and what Siri should do in response to it.
- [enum SiriTurnExpectationBuilder](./siriturnexpectationbuilder.md)
  A result builder that collects the expectations you attach to a user turn.
### Inspecting a user turn
- [let id: UUID](./userturn/id.md)
  An identifier for the turn.
- [let utterance: String](./userturn/utterance.md)
  The text a person says to Siri in this turn.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scenarios
- [struct SiriScenarioLoader](./siriscenarioloader.md)
  A loader that supplies the scenarios an evaluation runs, in the order you write them.
- [struct SiriScenario](./siriscenario.md)
  An ordered, multiturn interaction run in one Siri session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/userturn)*