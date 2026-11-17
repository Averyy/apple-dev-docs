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

The following example uses that type in a test that checks that every scenario ran and every intent expectation passed:

```swift
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")
let startQuizIntent = quizExampleIntents.intents["StartQuizIntent"]

@Suite(.serialized)
struct QuizExampleTests {
    @Test(
        .evaluates(QuizExampleEvaluation(
            name: "Start a science quiz",
            dataset: SiriScenarioLoader {
                SiriScenario {
                    UserTurn("In QuizExample, start a Science quiz with 5 questions.") {
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

        // A scenario that doesn't run, or that can't be graded, has no
        // metrics and doesn't lower the mean, so check that none failed.
        #expect(result.errors.inferenceFailureCount == 0)
        #expect(result.errors.evaluatorFailureCount == 0)
        #expect(result.aggregateValue(.mean(of: .intentsAllPass)) == 1)
    }
}
```

A device runs one scenario at a time, and a scenario that starts while another is running gets no metrics. Swift Testing runs tests in parallel by default, and runs separate suites, and tests outside a suite, in parallel even when each suite is serialized. So put every evaluation test in one `.serialized` suite, nesting any other suites inside it, or turn off parallel testing in the test plan.

An evaluation runs your app’s intents the same way Siri does when a person asks, including requests to Private Cloud Compute. Because `subject(from:)` runs once for each scenario, you can use it to put your app in a known state before Siri runs a scenario and clean up afterward. If cleanup fails, record an issue with `Issue.record` instead of throwing. When `subject(from:)` throws, the evaluation discards the run, and the scenario counts toward no metric.

Pass the `sample` that `subject(from:)` receives to [`run(scenario:)`](./siriservice/run%28scenario%29.md). For a subject that Siri ran from any other scenario, including a copy you rebuild, [`SiriExpectationEvaluator`](./siriexpectationevaluator.md) throws instead of grading it, so none of its metrics count that scenario.

> **Note**: Every app a scenario names, other than Apple’s, must be installed and signed by the same development team as your test target, or the scenario doesn’t run. On a Mac, every installed copy of the app must be signed by that team. A check that names an Apple app fails, and the report says it can’t be evaluated. Your test target needs no entitlements of its own.

Create your evaluation in a UI testing target, because [`run(scenario:)`](./siriservice/run%28scenario%29.md) works only there. A UI testing target also lets you use [XCUIAutomation](../XCUIAutomation/XCUIAutomation.md) to launch your app and navigate to a screen before invoking Siri. In iOS and visionOS, turn on Developer Mode, then Enable UI Automation in Settings > Developer. For more information about enabling Developer Mode, see [Enabling Developer Mode on a device](../Xcode/enabling-developer-mode-on-a-device.md).

## Topics

### Running scenarios
- [static func run(scenario: SiriScenario) async throws -> SiriScenarioSubject](./siriservice/run%28scenario%29.md)
  Runs a scenario through Siri and returns what Siri did, for your evaluation to grade.

## See Also

### Evaluations
- [Evaluating your app’s integration with Siri](./evaluating-your-apps-integration-with-siri.md)
  Create conversations to confirm that Siri runs the correct intents from your app, with the parameter values you expect.
- [struct SiriExpectationEvaluator](./siriexpectationevaluator.md)
  An evaluator that grades a scenario against its expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriservice)*