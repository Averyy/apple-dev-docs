# SiriScenario

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

An ordered, multiturn interaction run in one Siri session.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct SiriScenario
```

## Overview

A *scenario* is a conversation made of a sequence of turns. Each turn is something a person says, and Siri handles the turns in one session in the order you write them. A turn carries its own expectations about what Siri does, and the scenario carries expectations about the whole conversation.

A turn’s expectations apply only to that turn. A scenario’s expectations apply to all of its turns together. Put an expectation on the scenario when it spans turns, such as an intent that finishes only after the person answers a question. Using a [`Calls`](./calls.md) structure’s expectation on the scenario with [`Calls.Ordering.disallowed`](./calls/ordering-swift.enum/disallowed.md) fails if the call runs in any turn, or if Siri asks the person to confirm it in any turn. Use [`Calls.Ordering.unordered`](./calls/ordering-swift.enum/unordered.md) when each call happens in at least one turn, in any order.

A scenario conforms to [`Codable`](../Swift/codable.md), so you can encode a set of scenarios as JSON to review alongside your project.

The following example shows a two-turn scenario with expectations that apply to the whole conversation:

```swift
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")
let startQuizIntent = quizExampleIntents.intents["StartQuizIntent"]
let createQuizReminderIntent = quizExampleIntents.intents["CreateQuizReminderIntent"]

let scenario = SiriScenario {
    // In turn one, the person names the app but not the topic, so Siri
    // asks for one.
    UserTurn("Start a quiz in QuizExample")

    // The second turn answers with a topic.
    UserTurn("Science")
} expectation: {
    Calls {
        // The topic label comes from the parameter on the intent.
        startQuizIntent
            .expect(topic: .equals("Science"))
    }

    // Fails if Siri runs or asks the person to confirm the intent in any turn.
    Calls(.disallowed) {
        createQuizReminderIntent
    }
}
```

To run a scenario through Siri, pass it to a [`SiriScenarioLoader`](./siriscenarioloader.md) to make it part of the dataset for an evaluation that runs with [`SiriService`](./siriservice.md).

## Topics

### Creating a scenario
- [init(() -> [UserTurn])](./siriscenario/init%28_%29.md)
  The turns of the conversation, in order.
- [enum SiriScenarioBuilder](./siriscenariobuilder.md)
  A result builder that collects the turns of a scenario.
### Creating a scenario with expectations
- [init(() -> [UserTurn], expectation: () -> SiriScenarioExpectationBuilder.Component)](./siriscenario/init%28_,expectation%29.md)
  Creates a scenario from its turns, plus expectations for the conversation as a whole.
- [enum SiriScenarioExpectationBuilder](./siriscenarioexpectationbuilder.md)
  A result builder that collects the expectations you attach to a scenario.
### Inspecting a scenario
- [let turns: [UserTurn]](./siriscenario/turns.md)
  The turns of the conversation in the order that the person says them.
- [var input: String](./siriscenario/input.md)
  The scenario’s utterances joined into one line for the report’s Input column.
- [var expected: SiriScenarioSubject.ScenarioReport?](./siriscenario/expected.md)
  The scenario’s expectations as the report’s Expected column.
### Encoding a scenario
- [func encode(to: any Encoder) throws](./siriscenario/encode%28to%29.md)
  The scenario’s own fields, plus the utterances as one line.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [SampleProtocol](../Evaluations/sampleprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scenarios
- [struct SiriScenarioLoader](./siriscenarioloader.md)
  A loader that supplies the scenarios an evaluation runs, in the order you write them.
- [struct UserTurn](./userturn.md)
  A single utterance a person says, with what you expect Siri to do in response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenario)*