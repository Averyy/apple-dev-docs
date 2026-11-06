# SiriService

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A service that runs a scenario through Siri and records what Siri does.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum SiriService
```

## Overview

A Siri evaluation runs a dataset of scenarios through Siri and reports metrics across them. To define one, declare a type in your test target that conforms to [`Evaluation`](../Evaluations/evaluation.md), and attach an instance to a test with an evaluation trait. In the type’s `subject(from:)` method, call [`run(scenario:)`](./siriservice/run%28scenario%29.md) to run each scenario through Siri. The method returns a [`SiriScenarioSubject`](./siriscenariosubject.md) that holds the results for the evaluation to grade.

This example declares an evaluation type that runs every scenario with `SiriService`, grades every kind of expectation, and reports the standard Siri metrics:

```swift
// One evaluation type can serve every test in the target, because each test 
// passes its own name and dataset.
struct QuizExampleEvaluation: Evaluation {
    // The title of the evaluation's report in Xcode.
    let name: String

    // The loader that holds the scenarios you write.
    let dataset: SiriScenarioLoader

    // The method that runs one scenario through Siri.
    func subject(from sample: SiriScenario) async throws -> SiriScenarioSubject {
        try await SiriService.run(scenario: sample)
    }

    // The evaluators that grade what Siri does.
    var evaluators: Evaluators {
        SiriExpectationEvaluator()
    }

    // The method that decides which metrics the evaluation reports.
    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        Self.computeSiriMetrics(into: &aggregator)
    }
}
```

The following example uses that type in a test that checks that every intent expectation passed:

```swift
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")
let startQuizIntent = quizExampleIntents.intents["StartQuizIntent"]

@Test(
    .evaluates(QuizExampleEvaluation(
        name: "Start a science quiz",
        dataset: SiriScenarioLoader {
            SiriScenario {
                UserTurn("In QuizExample, start a science quiz with 5 questions") {
                    Calls {
                        startQuizIntent
                            .expect(topic: .equals("Science"))
                    }
                }
            }
        }
    ))
)
func startsScienceQuiz() async throws {
    let result = EvaluationContext.current.result
    #expect(result.aggregateValue(.mean(of: .intentsAllPass)) == 1)
}
```

An evaluation runs your app’s intents the same way Siri does when a person asks, including requests to Private Cloud Compute. Because `subject(from:)` runs once for each scenario, you can use it to put your app in a known state before Siri runs a scenario and clean up afterward. Pass the `sample` that `subject(from:)` receives to [`run(scenario:)`](./siriservice/run%28scenario%29.md). [`SiriExpectationEvaluator`](./siriexpectationevaluator.md) doesn’t grade a subject that Siri ran from any other scenario, including a copy you rebuild.

> **Note**: You can only evaluate apps that are signed by the same development team as your test target.

When you create an evaluation, use a UI testing target. A UI testing target lets you use [XCUIAutomation](../XCUIAutomation/XCUIAutomation.md) to launch your app and navigate to a screen before invoking Siri. To turn on UI automation, turn on Developer Mode, then Enable UI Automation in Settings > Developer. For more information about enabling Developer Mode, see [Enabling Developer Mode on a device](../Xcode/enabling-developer-mode-on-a-device.md).

## Topics

### Running scenarios
- [static func run(scenario: SiriScenario) async throws -> SiriScenarioSubject](./siriservice/run%28scenario%29.md)
  Runs a scenario through Siri and returns what Siri did, for your evaluation to grade.

## See Also

### Evaluations
- [struct SiriExpectationEvaluator](./siriexpectationevaluator.md)
  An evaluator that grades a scenario against its expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriservice)*