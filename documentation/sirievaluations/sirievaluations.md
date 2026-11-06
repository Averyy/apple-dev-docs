# Siri Evaluations

**Framework**: Siri Evaluations  
**Kind**: module  
**Role**: Framework

Evaluate how well Siri engages your app’s intents and entities by running scripted conversations and checking what Siri does.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Overview

Use the Siri Evaluations framework to script requests to Siri and measure how Siri handles them, with metrics you can check in a test. The test records which intents Siri calls and which entities Siri finds, and compares each step against your expectations. Use it to catch changes in how Siri responds as you update your intents and entities.

![The Siri logo beside the Evaluations framework icon. Together they represent](https://developer.apple.com/tutorials/images/com.apple.sirievaluations/siri-evaluations-framework-hero@2x.png)

Write a conversation as a scenario that contains user turns. In each turn, you describe what the person asks and what you expect Siri to do. Your expectations can include the intents Siri calls, the parameter values Siri passes, the entities Siri finds, and the text Siri responds with. Each check compares what Siri does with the values you specify, and the comparison is deterministic.

Start with a few scenarios that use simple, direct requests to confirm that your integration works end to end, alongside trying requests with Siri on a device. Then build a broad set of scenarios that reflects the many ways people phrase requests, and include indirect, incomplete, and unexpected wording. Because Siri’s responses can vary between runs, run the set more than once, and improve your intents, their parameter names and descriptions, and your App Skills until more of the set passes, and passes consistently.

Siri Evaluations works with the [Evaluations](../Evaluations/Evaluations.md) and [Swift Testing](../Testing/Testing.md) frameworks. If you’ve used either one, the workflow is similar to what you do in these frameworks:

- Define a Siri evaluation.
- Run it from a test.
- Check the metrics it produces.

After a run, Xcode shows a report of what Siri says and does in each turn.

> **Note**: The Siri AI developer preview is available on platforms and devices that support Apple Intelligence. During the developer preview, App Intents API and Siri functionality may change. For more information about getting your app ready for Siri AI, see [Siri AI Developer Preview](../AppIntents/siri-ai-developer-preview.md).

## Topics

### Evaluations
- [enum SiriService](./siriservice.md)
  A service that runs a scenario through Siri and records what Siri does.
- [struct SiriExpectationEvaluator](./siriexpectationevaluator.md)
  An evaluator that grades a scenario against its expectations.
### Scenarios
- [struct SiriScenarioLoader](./siriscenarioloader.md)
  A loader that supplies the scenarios an evaluation runs, in the order you write them.
- [struct SiriScenario](./siriscenario.md)
  An ordered, multiturn interaction run in one Siri session.
- [struct UserTurn](./userturn.md)
  A single utterance a person says, with what you expect Siri to do in response.
### Expectations
- [struct Calls](./calls.md)
  An expectation that Siri calls, or doesn’t call, a set of intents during a turn or scenario.
- [struct Finds](./finds.md)
  An expectation that Siri surfaces specific app entities by search or resolution.
- [struct Loads](./loads.md)
  An expectation that Siri loads specific app skills.
- [struct OnScreen](./onscreen.md)
  An expectation that specific app entities are onscreen.
- [struct SiriResponse](./siriresponse.md)
  An expectation that the reply Siri gives contains specific text.
### Results
- [struct SiriScenarioSubject](./siriscenariosubject.md)
  A record of one scenario’s run through Siri, as the Evaluations framework sees it.
- [struct SiriTranscript](./siritranscript.md)
  The immutable record of one scenario’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations)*