# SiriResponse

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

An expectation that the reply Siri gives contains specific text.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct SiriResponse
```

## Overview

Use `SiriResponse` to check the text of the reply Siri gives for a turn. Every check must hold, and each check passes when the reply contains the text you give. The text is plain text, not a pattern. A check is case-sensitive unless you pass `false` for `caseSensitive`. In the Xcode evaluation report, a check that fails shows the reply Siri gives next to the text it requires.

The wording Siri uses varies between runs even when Siri responds correctly, so name something the reply has to say, such as a topic or a name the person provides, not how Siri says it. To check a value that an intent receives or returns, use [`Calls`](./calls.md) instead. Use `SiriResponse` for details that appear only in the reply.

Check a reply on the turn that gives it. A turn accepts a `SiriResponse`, but the expectation closure of [`init(_:expectation:)`](./siriscenario/init%28_,expectation%29.md) doesn’t, because the reply belongs to a single turn.

The following example shows a turn that expects the reply to name the topic in any capitalization:

```swift
UserTurn("In QuizExample, start a science quiz with 5 questions") {
    SiriResponse(.contains("science", caseSensitive: false))
}
```

## Topics

### Creating a response expectation
- [init(SiriResponse.Text...)](./siriresponse/init%28_%29.md)
  Creates an expectation that Siri’s reply satisfies every check.
### Matching response text
- [SiriResponse.Text](./siriresponse/text.md)
  One check on the reply’s text.

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
- [struct OnScreen](./onscreen.md)
  An expectation that specific app entities are onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriresponse)*