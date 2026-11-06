# Calls

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

An expectation that Siri calls, or doesn’t call, a set of intents during a turn or scenario.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct Calls
```

## Overview

Use `Calls` to name the intents Siri calls during a turn or anywhere in a scenario. By default, the expectation requires Siri to call them in the order you list them. Pass [`Calls.Ordering.unordered`](./calls/ordering-swift.enum/unordered.md) to accept any order, or [`Calls.Ordering.disallowed`](./calls/ordering-swift.enum/disallowed.md) to require that Siri doesn’t call them.

The values [`Calls.Ordering.ordered`](./calls/ordering-swift.enum/ordered.md) and [`Calls.Ordering.unordered`](./calls/ordering-swift.enum/unordered.md) check only that Siri makes the calls you list. They don’t catch extra calls, such as Siri performing the wrong action. To catch an action Siri shouldn’t take, use [`Calls.Ordering.disallowed`](./calls/ordering-swift.enum/disallowed.md).

The framework checks two `Calls` groups in the same turn independently, so Siri can call another intent before, between, or after them. To require one sequence, write one group.

A call counts only if it runs. A call that Siri plans but doesn’t complete satisfies no `Calls` expectation. This includes a call that stops to ask the person for a missing value or for confirmation, and a call that fails. A [`Calls.Ordering.disallowed`](./calls/ordering-swift.enum/disallowed.md) expectation fails if the call runs. It also fails if Siri asks the person to confirm the call, because Siri already chooses the action and its arguments. A clarifying question from Siri, such as which topic the person means, doesn’t count.

Constrain an intent’s arguments with [`expect`](../AppIntentsTesting/appintentdefinition/expect.md), using the parameter names as labels. The string matchers, such as `.equals(_:)` and `.contains(_:)`, compare string values. To check a parameter of another type, such as an integer, use `.matches(_:requirement:)` with a predicate, as the following example shows:

```swift
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")
let startQuizIntent = quizExampleIntents.intents["StartQuizIntent"]

Calls {
    startQuizIntent
        .expect(
            topic: .equals("Science"),
            questionCount: .matches(#Predicate<Int> { $0 == 5 })
        )
}
```

The following example shows a turn that expects Siri to create a reminder for a topic and not to start a quiz:

```swift
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")
let startQuizIntent = quizExampleIntents.intents["StartQuizIntent"]
let createQuizReminderIntent = quizExampleIntents.intents["CreateQuizReminderIntent"]

UserTurn("Use QuizExample to create a history quiz reminder for tomorrow at 7 p.m.") {
    Calls {
        createQuizReminderIntent
            .expect(topic: .equals("History"))
    }

    // Fails if Siri runs or asks the person to confirm the intent.
    Calls(.disallowed) {
        startQuizIntent
    }
}
```

## Topics

### Creating a call expectation
- [init(Calls.Ordering, () -> [any AppIntentExpectationProviding])](./calls/init%28_,_%29.md)
  Creates an expectation that Siri calls the intents in the block, or doesn’t call them, as the ordering requires.
- [enum IntentExpectationBuilder](./intentexpectationbuilder.md)
  A result builder that collects the intents in a calls expectation.
### Configuring call order
- [let ordering: Calls.Ordering](./calls/ordering-swift.property.md)
  How Siri must call the intents, or that it must not call them.
- [Calls.Ordering](./calls/ordering-swift.enum.md)
  A requirement for how Siri must call the intents in an expectation, or that it doesn’t call them.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Expectations
- [struct Finds](./finds.md)
  An expectation that Siri surfaces specific app entities by search or resolution.
- [struct Loads](./loads.md)
  An expectation that Siri loads specific app skills.
- [struct OnScreen](./onscreen.md)
  An expectation that specific app entities are onscreen.
- [struct SiriResponse](./siriresponse.md)
  An expectation that the reply Siri gives contains specific text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/calls)*