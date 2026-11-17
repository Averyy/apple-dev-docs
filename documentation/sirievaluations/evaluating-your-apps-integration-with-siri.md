# Evaluating your app’s integration with Siri

**Framework**: Siri Evaluations  
**Role**: Article

Create conversations to confirm that Siri runs the correct intents from your app, with the parameter values you expect.

## Overview

When someone asks Siri to do something in your app, Siri can choose one of your app’s intents and fill in the parameters it needs to perform that action. You can test this by making requests to Siri yourself, but the response alone doesn’t show the decisions Siri made. A Siri evaluation shows you which intent Siri chooses, the parameter values it passes, and the app entities it finds. You can then adjust the names and descriptions of your intents, parameters, and skills, and run the evaluation again to see whether Siri responds more reliably.

In a Siri evaluation, you create the conversations you want to test and describe what Siri needs to do at each step. The evaluation runs each conversation through Siri on a device, records what Siri does, and grades it against your expectations. You run an evaluation as a Swift Testing test inside a UI test target and review the results in Xcode.

## Check the prerequisites

Before you write an evaluation, make sure your app has at least one app intent that you mark as callable by Siri by adding the [`tool`](../AppIntents/appintenttraits/tool.md) trait to its `@AppIntent` macro. An *app intent* is an action a person can do in your app, such as creating a quiz reminder in a quiz app. Its parameters hold the values the action needs, such as the quiz topic and the reminder’s date. For more information, see [`ToolIntent`](../AppIntents/toolintent.md).

Siri evaluations run only in a UI testing target. Starting in Xcode 27.3, you can write UI tests with Swift Testing, so you can run an evaluation as a Swift Testing test in that target. To add a UI testing target, choose File > New > Target, and then choose UI Testing Bundle.

> **Note**: To turn on UI automation in iOS and visionOS, turn on Developer Mode, then Enable UI Automation in Settings > Developer. For more information about turning on Developer Mode, see [Enabling Developer Mode on a device](../Xcode/enabling-developer-mode-on-a-device.md).

Siri evaluations don’t run in Simulator; you need a physical device with Siri turned on and fully set up. Siri performs your intents during an evaluation the same way it does when a person asks, so use a dedicated test device and fictional test data. This approach also keeps your personal information out of the requests Siri handles and the results that the evaluation records.

Follow these steps as you set up the evaluation:

- The app you evaluate needs to be installed on the test device and signed by the same development team as your test target.
- Set up a test device to resemble the devices of the people who use your app. A device with few other apps or little data can produce a higher pass rate than people get on devices with many apps and more data.
- To get results closer to what people experience, install apps that handle similar requests, and stage as much fictional data as people typically keep in your app.

For more information on custom app intents and Siri, see [Bringing custom actions and content to Siri](../AppIntents/bringing-custom-actions-and-content-to-siri.md). For more information on testing app intents, see [Testing your App Intents code](../AppIntentsTesting/testing-your-app-intents-code.md).

## Plan your evaluation’s structure

An evaluation is a type you define that conforms to [`Evaluation`](../Evaluations/evaluation.md). It runs a dataset through Siri and reports metrics. The dataset is a [`SiriScenarioLoader`](./siriscenarioloader.md) that holds your scenarios. Each [`SiriScenario`](./siriscenario.md) is one conversation made of [`UserTurn`](./userturn.md) values, and each turn contains what a person says to Siri and the expectations for how Siri responds. A scenario can also have its own expectations, which the evaluation checks against all of its turns together. The following figure shows the structure of an evaluation:

![A diagram of an evaluation’s structure. An evaluation contains a dataset of](https://developer.apple.com/tutorials/images/com.apple.sirievaluations/evaluating-your-apps-integration-with-siri-structure@2x.png)

The evaluation checks each expectation separately by comparing what Siri did with what you wrote. The framework provides the following expectations:

- **[`Calls`](./calls.md)**: The app intents Siri needs to run. By default, Siri needs to run them in the order you write them. You can also allow any order or list intents that Siri must not run.
- **[`Finds`](./finds.md)**: The app entities Siri needs to find, either by searching your app or by resolving an intent’s parameters.
- **[`OnScreen`](./onscreen.md)**: The app entities that need to be in the onscreen context Siri captures during the turn, which the evaluation includes in its report. You identify each entity by its type or identifier.
- **[`Loads`](./loads.md)**: The App Skills Siri needs to load. Each expectation states whether a skill is required or preferred. A preferred skill appears in the report but never affects the score.
- **[`SiriResponse`](./siriresponse.md)**: Text that Siri’s reply needs to contain. You can add this to a turn but not to a scenario.

For more information on App Skills, see [Orchestrating complex actions with app skills](../AppIntents/orchestrating-complex-actions-with-app-skills.md).

## Describe a request and the intent call you expect

Start by creating an [`IntentDefinitions`](../AppIntentsTesting/intentdefinitions.md) value with your app’s bundle identifier. This value gives your tests access to your app’s intents and entities. Then look up the intent you want to test by its type name so your expectations can refer to it:

```swift
import Testing
import SiriEvaluations

// The intents and entities of the app under test.
let quizExampleIntents = IntentDefinitions(bundleIdentifier: "com.example.QuizExample")

// The app intent to test.
let createQuizReminderIntent = quizExampleIntents.intents["CreateQuizReminderIntent"]
```

A [`UserTurn`](./userturn.md) holds a request and the intent call you expect. A turn contains the words a person says to Siri, followed by a closure that lists what Siri needs to do in that turn. To make sure Siri sends the request to your app instead of another app, include your app’s name in the request:

```swift
UserTurn("In QuizExample, create a History quiz reminder for tomorrow at 7 PM.") {
    // The expectations for Siri's response to the request.
}
```

Inside the closure, add a [`Calls`](./calls.md) expectation that names the intent Siri needs to call. To check a parameter value, call `expect` on the intent, using the parameter’s name as the argument label, and pass a matcher. For example, the following checks whether Siri calls the intent with the expected topic:

```swift
Calls {
    createQuizReminderIntent
        .expect(topic: .equals("History"))
}
```

This expectation passes only when Siri runs `CreateQuizReminderIntent` with its `topic` parameter set to `History`. If Siri stops to ask the person for a missing value or for confirmation, the call doesn’t run in that turn. If the call runs and fails, the expectation doesn’t pass either. To test a conversation where Siri asks a follow-up question, add a turn with the answer.

To form the dataset you pass to your evaluation, wrap the turn in a [`SiriScenario`](./siriscenario.md), and then wrap the scenario in a [`SiriScenarioLoader`](./siriscenarioloader.md):

```swift
let dataset = SiriScenarioLoader {
    SiriScenario {
        UserTurn("In QuizExample, create a History quiz reminder for tomorrow at 7 PM.") {
            Calls {
                createQuizReminderIntent
                    .expect(topic: .equals("History"))
            }
        }
    }
}
```

## Create an evaluation type

Define the evaluation as a type that conforms to [`Evaluation`](../Evaluations/evaluation.md). The type defines how to run each scenario through Siri, how to grade the results, and which metrics to report. Declare it once in your test target, then create an instance for each test with its own name and dataset:

```swift
struct QuizExampleEvaluation: Evaluation {
    // The title of the evaluation's report in Xcode.
    let name: String

    // The scenarios to run.
    let dataset: SiriScenarioLoader

    // Grades each scenario against its expectations.
    var evaluators: Evaluators {
        SiriExpectationEvaluator()
    }

    // Runs one scenario through Siri and returns what Siri did.
    func subject(from sample: SiriScenario) async throws -> SiriScenarioSubject {
        try await SiriService.run(scenario: sample)
    }

    // Adds the standard Siri metrics to the report.
    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        Self.computeSiriMetrics(into: &aggregator)
    }
}
```

Each run of an evaluation can change state on the device. To keep one run from affecting the next, reset the app to a known state before each scenario by running a test-only app intent in `subject(from:)` before you call [`run(scenario:)`](./siriservice/run%28scenario%29.md):

```swift
// A test-only intent that deletes every quiz reminder.
let deleteAllRemindersIntent = quizExampleIntents.intents["DeleteAllRemindersIntent"]

func subject(from sample: SiriScenario) async throws -> SiriScenarioSubject {
    // Delete reminders left over from an earlier run.
    try await deleteAllRemindersIntent.makeIntent().run()
    return try await SiriService.run(scenario: sample)
}
```

Attach an instance of your evaluation to a test function with the `.evaluates` trait, which runs the evaluation as part of that test. Inside the test, get the result from the current [`EvaluationContext`](../Evaluations/evaluationcontext.md). The following test calls [`aggregateValue(_:)`](../Evaluations/evaluationresult/aggregatevalue%28_%29.md) to check that the mean of [`intentsAllPass`](../Evaluations/metric/intentsallpass.md) equals `1`:

```swift
@Test(.evaluates(QuizExampleEvaluation(name: "Create a history quiz reminder",
                                       dataset: dataset)))
func createsHistoryQuizReminder() async throws {
    let result = EvaluationContext.current.result
    #expect(result.aggregateValue(.mean(of: .intentsAllPass)) == 1)
}
```

The `intentsAllPass` metric scores a scenario as a pass only when every [`Calls`](./calls.md) expectation in it holds, including calls that Siri needs to avoid. The evaluation averages that score across the scenarios that contain a [`Calls`](./calls.md) expectation, so a value of `1` means every one of those scenarios passes.

A device runs one scenario at a time, and Swift Testing runs tests in parallel by default. Put all your evaluation tests in one `.serialized` suite, or turn off parallel testing in your test plan.

## Run the evaluation

Connect and unlock your test device, select it as the run destination, and choose Product > Test. After the tests complete, choose View > Navigators > Reports to open the Report navigator, and then select Evaluations from the test run. This figure shows the resulting report:

![A screenshot of the Evaluations report in Xcode, open from the Report navigator.](https://developer.apple.com/tutorials/images/com.apple.sirievaluations/evaluating-your-apps-integration-with-siri-evals@2x.png)

## Examine the evaluation results

The Evaluations report lists each evaluation in the test run with its metrics. Double-click an evaluation to see its scenarios, and select a scenario to open its report. The scenario’s report shows a card for each metric and a table that compares what you expected with what Siri did:

![A screenshot of the report for the evaluation Create a history quiz reminder,](https://developer.apple.com/tutorials/images/com.apple.sirievaluations/evaluating-your-apps-integration-with-siri-conversation@2x.png)

In the table, Subject shows what Siri did, and Expected shows what your scenario asked for. When they differ, Xcode shows a warning in the Issues column. The table groups its rows as follows:

- **Diagnostics**: How many turns completed, any observations the framework was unable to decode, whether Siri started before your app’s intents were ready, and how many app entities the app indexed before Siri ran.
- **Scenario**: The expectations on the scenario itself, if it has any.
- **Turn**: A row for the person’s request, a row for each expectation, and Siri’s response.

When a check fails, look for one of the following causes:

- ****Siri passes the wrong value**.**: Revise the parameter’s title and description in your intent so Siri knows what to put there.
- ****Siri plans the call but doesn’t run it**.**: The call’s row gives the reason. Siri might stop to ask for a missing value or for confirmation.
- ****Siri never calls your intent**.**: Read Siri’s response at the end of the turn to see what Siri did instead, such as sending the request to another app or opening your app without calling an intent.

A failure can also mean that a turn doesn’t run. When a run stops partway, the expectations on the turns that didn’t run fail, except for disallowed calls, which usually still pass. Check Diagnostics to see how many turns completed. If a scenario can’t run at all, such as when Siri hasn’t finished setting up, the report shows the error instead of metrics. A scenario without metrics doesn’t count toward any average, so a metric can still equal `1` when one of your scenarios didn’t run.

## Add more expectations

After your first evaluation passes, add expectations for what Siri needs to avoid. A [`Calls.Ordering.disallowed`](./calls/ordering-swift.enum/disallowed.md) expectation fails if one of its intents runs, even if the call fails, or if Siri asks the person to confirm the call or one of its values. A question about which item the person means, rather than whether to act, isn’t a confirmation. For example, the following checks that Siri creates a reminder and doesn’t start a quiz:

```swift
let startQuizIntent = quizExampleIntents.intents["StartQuizIntent"]

UserTurn("In QuizExample, create a History quiz reminder for tomorrow at 7 PM.") {
    Calls {
        createQuizReminderIntent
            .expect(topic: .equals("History"))
    }
    Calls(.disallowed) {
        startQuizIntent
    }
}
```

To check that Siri finds the right entity in your app, add a [`Finds`](./finds.md) expectation. For example, the following checks that Siri finds a quiz topic whose title contains the words from the request:

```swift
let quizTopicEntity = quizExampleIntents.entities["QuizTopicEntity"]

UserTurn("In QuizExample, start the Ancient Rome quiz.") {
    Finds {
        quizTopicEntity
            .expect(title: .contains("Ancient Rome"))
    }
}
```

The evaluation can reliably check only the properties Siri sees for an entity. When Siri finds the entity in your app’s Spotlight index, those are the properties your app indexes. When Siri queries your app directly, those are the properties in the query’s results. A property that Siri doesn’t read has no value, so an expectation that needs a value fails, and `.isNil` passes.

To check something across a whole conversation, add expectations to the scenario instead of a turn. The evaluation compares a scenario’s expectations with all of its turns together, so an expectation passes no matter which turn satisfies it. To match calls in any order, use [`Calls.Ordering.unordered`](./calls/ordering-swift.enum/unordered.md). For example, the following checks that Siri creates the reminder in either turn and doesn’t start a quiz:

```swift
SiriScenario {
    UserTurn("In QuizExample, remind me to take a History quiz.")
    // A second utterance that answers a question about when, if Siri asks.
    UserTurn("Tomorrow at 7 p.m.")
} expectation: {
    Calls(.unordered) {
        createQuizReminderIntent
            .expect(topic: .equals("History"))
    }
    Calls(.disallowed) {
        startQuizIntent
    }
}
```

## Load scenarios from a file

Because [`SiriScenario`](./siriscenario.md) conforms to [`Codable`](../Swift/codable.md), you can store scenarios in a JSON file instead of only writing them in Swift. The evaluation runs and grades decoded scenarios the same way it does scenarios you write in Swift. The following loads scenarios from a JSON file:

```swift
func makeDataset(from scenariosURL: URL) throws -> SiriScenarioLoader {
    let data = try Data(contentsOf: scenariosURL)
    let scenarios = try JSONDecoder().decode([SiriScenario].self, from: data)
    return SiriScenarioLoader { scenarios }
}
```

## See Also

### Evaluations
- [enum SiriService](./siriservice.md)
  A service that runs a scenario through Siri and records what Siri does.
- [struct SiriExpectationEvaluator](./siriexpectationevaluator.md)
  An evaluator that grades a scenario against its expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/evaluating-your-apps-integration-with-siri)*