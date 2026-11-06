# Loads

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

An expectation that Siri loads specific app skills.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct Loads
```

## Overview

A skill is the Markdown instructions an app ships for a task, which can reference the app’s intents and chain them to satisfy a request. Use `Loads` to check whether Siri loads a skill into its planning for a turn.

`Loads` has no default enforcement, so you write [`Loads.Enforcement.required`](./loads/enforcement-swift.enum/required.md) or [`Loads.Enforcement.preferred`](./loads/enforcement-swift.enum/preferred.md). Only a required skill counts toward the [`skillsLoadedPass`](../Evaluations/metric/skillsloadedpass.md) metric. A turn fails a required `Loads` if Siri doesn’t load the skill.

A preferred skill appears in the report but never affects the score. Siri sees the app’s intents alongside the skill and might satisfy the request by calling them directly.

To name a skill, write its [`SkillDefinition`](../AppIntentsTesting/skilldefinition.md) in the closure. A skill has no properties to constrain, so the expectation matches by identity and checks only whether Siri loads that skill.

A passing check doesn’t show that Siri follows the skill’s instructions, because Siri doesn’t report which steps it performs in a skill. To verify the outcome, pair `Loads` with [`Calls`](./calls.md) for the intents the skill chains.

For more information about skills, see [Orchestrating complex actions with app skills](../AppIntents/orchestrating-complex-actions-with-app-skills.md).

## Topics

### Creating a load expectation
- [init(Loads.Enforcement, () -> [SkillDefinition])](./loads/init%28_,_%29.md)
  Creates an expectation that the skills in the block load, graded according to the enforcement.
- [enum SkillExpectationBuilder](./skillexpectationbuilder.md)
  A result builder that collects the skills in a loads expectation.
### Configuring enforcement
- [let enforcement: Loads.Enforcement](./loads/enforcement-swift.property.md)
  Whether a missed skill fails the expectation or only shows in the report.
- [Loads.Enforcement](./loads/enforcement-swift.enum.md)
  Whether a missed skill fails the expectation or only shows in the report.

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
- [struct OnScreen](./onscreen.md)
  An expectation that specific app entities are onscreen.
- [struct SiriResponse](./siriresponse.md)
  An expectation that the reply Siri gives contains specific text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/loads)*