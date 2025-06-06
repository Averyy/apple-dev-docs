# XCTestCase

**Framework**: Xctest  
**Kind**: class

The primary class for defining test cases, test methods, and performance tests.

## Declaration

```swift
class XCTestCase
```

## Mentions

- [Defining Test Cases and Test Methods](defining-test-cases-and-test-methods.md)
- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)
- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)
- [Grouping Tests into Substeps with Activities](grouping-tests-into-substeps-with-activities.md)

#### Overview

A test case is a group of related test methods, with optional setup and teardown before and after tests run. See [`Defining Test Cases and Test Methods`](defining-test-cases-and-test-methods.md) for more information.

`XCTestCase` conforms to [`XCTActivity`](xctactivity.md), so you can simplify complex tests by organizing them into activities, and attach output to tests for later analysis. For more information, see [`Activities and Attachments`](activities-and-attachments.md).

Create tests for asynchronous operations using expectations. For more information, see `Testing Asynchronous Operations with Expectations`. If your app uses Swift [`Concurrency`](https://developer.apple.com/documentation/Swift/concurrency), annotate test methods with `async` or `async throws` instead to test asynchronous operations, and use standard Swift concurrency patterns in your tests.

Create tests to measure performance for specific blocks of code using the methods in the Measuring Performance section below. Build performance tests as part of a continuous improvement cycle for performance in your app. For more information, see [`Improving your app’s performance`](https://developer.apple.com/documentation/Xcode/improving-your-app-s-performance).

## Topics

### Customizing Test Setup and Teardown
- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [class func setUp()](xctestcase/setup.md)
  Provides an opportunity to customize initial state before a test case begins.
- [func addTeardownBlock(() async throws -> Void)](xctestcase/addteardownblock(_:)-2guon.md)
  Registers a block of teardown code to run after the current test method ends.
- [func addTeardownBlock(() throws -> Void)](xctestcase/addteardownblock(_:)-5zw6c.md)
  Registers a block of teardown code to run after the current test method ends.
- [class func tearDown()](xctestcase/teardown.md)
  Provides an opportunity to perform cleanup after a test case ends.
### Managing Test Case Execution
- [class var runsForEachTargetApplicationUIConfiguration: Bool](xctestcase/runsforeachtargetapplicationuiconfiguration.md)
  A Boolean value that indicates whether your UI tests run once for each possible combination of orientation, localization, and other appearance settings your app supports.
- [var continueAfterFailure: Bool](xctestcase/continueafterfailure.md)
  A Boolean value that indicates whether a test method should continue running after a failure occurs.
- [var executionTimeAllowance: TimeInterval](xctestcase/executiontimeallowance.md)
  The number of seconds, rounded up to the nearest minute, for a test to run before it fails with a timeout error.
### Measuring Performance
- [func measure(() -> Void)](xctestcase/measure(_:).md)
  Measures the performance of a block of code.
- [func measureMetrics([XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for: () -> Void)](xctestcase/measuremetrics(_:automaticallystartmeasuring:for:).md)
  Measures the performance of a block of code, optionally deferring the starting point for measurement.
- [func measure(metrics: [any XCTMetric], block: () -> Void)](xctestcase/measure(metrics:block:).md)
  Records the selected metrics for a block of code.
- [func measure(metrics: [any XCTMetric], options: XCTMeasureOptions, block: () -> Void)](xctestcase/measure(metrics:options:block:).md)
  Records the selected metrics, using the specified measurement options, for a block of code.
- [func measure(options: XCTMeasureOptions, block: () -> Void)](xctestcase/measure(options:block:).md)
  Records the performance, using the specified measurement options, for a block of code.
- [func startMeasuring()](xctestcase/startmeasuring.md)
  Starts recording performance metrics within a block of code.
- [func stopMeasuring()](xctestcase/stopmeasuring.md)
  Ends recording performance metrics within a block of code.
- [class var defaultPerformanceMetrics: [XCTPerformanceMetric]](xctestcase/defaultperformancemetrics.md)
  An array of default performance metrics the test records.
- [class var defaultMetrics: [any XCTMetric]](xctestcase/defaultmetrics.md)
  An array of default metrics the test uses to record performance.
- [class var defaultMeasureOptions: XCTMeasureOptions](xctestcase/defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.
- [struct XCTPerformanceMetric](xctperformancemetric.md)
  Performance metrics that the test records.
### Creating Asynchronous Test Expectations
- [func expectation(description: String) -> XCTestExpectation](xctestcase/expectation(description:).md)
  Creates a new expectation with an associated description.
- [func expectation(for: NSPredicate, evaluatedWith: Any?, handler: XCTNSPredicateExpectation.Handler?) -> XCTestExpectation](xctestcase/expectation(for:evaluatedwith:handler:).md)
  Creates an expectation that the test fulfills by evaluating the predicate with the specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](xctestcase/expectation(fornotification:object:handler:).md)
  Creates an expectation that the test fulfills when it receives a specific notification for a specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](xctestcase/expectation(fornotification:object:notificationcenter:handler:).md)
  Creates an expectation that the test fulfills when it receives a specific notification from a specific notification center for a specified object.
- [func keyValueObservingExpectation(for: Any, keyPath: String, expectedValue: Any?) -> XCTestExpectation](xctestcase/keyvalueobservingexpectation(for:keypath:expectedvalue:).md)
  Creates an expectation that uses Key-Value Observing to observe a value until it matches an expected value.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willEqual: V) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willequal:).md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes to an expected value.
- [func keyValueObservingExpectation(for: Any, keyPath: String, handler: XCTKVOExpectation.Handler?) -> XCTestExpectation](xctestcase/keyvalueobservingexpectation(for:keypath:handler:).md)
  Creates an expectation that uses Key-Value Observing to observe a value and respond to changes in that value by calling a provided handler.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.Predicate?) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willsatisfy:)-6itb.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes and satisfies the conditions of a predicate’s evaluation.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.AsynchronousFilter?) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willsatisfy:)-292oj.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.SynchronousFilter?) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willsatisfy:)-85or0.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
### Waiting for Expectations
- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async](xctestcase/fulfillment(of:timeout:enforceorder:).md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation])](xctestcase/wait(for:).md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool)](xctestcase/wait(for:enforceorder:).md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval)](xctestcase/wait(for:timeout:).md)
  Waits for the test to fulfill a set of expectations within a specified time.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool)](xctestcase/wait(for:timeout:enforceorder:).md)
  Waits for the test to satisfy an array of expectations and specifies whether they must occur in the array’s order.
- [func waitForExpectations(timeout: TimeInterval, handler: (((any Error)?) -> Void)?)](xctestcase/waitforexpectations(timeout:handler:).md)
  Waits until the test fulfills all expectations or until it times out.
- [typealias XCWaitCompletionHandler](xcwaitcompletionhandler.md)
  A block the test runner calls when the test fulfills a waiter’s expectations, or when it times out.
- [struct XCTestError](xctesterror.md)
  A type of error that can occur while the test waits to fulfill expectations.
- [XCTestError.Code](xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
- [let XCTestErrorDomain: String](xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.
### Monitoring UI Interruptions
- [Handling UI Interruptions](handling-ui-interruptions.md)
  Improve your UI test’s stability by handling interface changes that block the UI elements under test.
- [func addUIInterruptionMonitor(withDescription: String, handler: (XCUIElement) -> Bool) -> any NSObjectProtocol](xctestcase/adduiinterruptionmonitor(withdescription:handler:).md)
  Adds a handler to the current context.
- [func removeUIInterruptionMonitor(any NSObjectProtocol)](xctestcase/removeuiinterruptionmonitor(_:).md)
  Removes a handler using the token from when you added the handler.
### Creating Tests Programmatically
- [init(invocation: NSInvocation?)](xctestcase/init(invocation:).md)
  Initializes a test case with an invocation.
- [init(selector: Selector)](xctestcase/init(selector:).md)
  Initializes a test case with a selector.
- [class var testInvocations: [NSInvocation]](xctestcase/testinvocations.md)
  An array of invocations that represents each test method in the test case.
- [var invocation: NSInvocation?](xctestcase/invocation.md)
  The invocation for running the test.
- [func invokeTest()](xctestcase/invoketest.md)
  Invokes the test.
- [func record(XCTIssue)](xctestcase/record(_:).md)
  Records an issue during test execution.
- [func recordFailure(withDescription: String, inFile: String, atLine: Int, expected: Bool)](xctestcase/recordfailure(withdescription:infile:atline:expected:).md)
  Records a failure during text execution.
- [class var defaultTestSuite: XCTestSuite](xctestcase/defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.

## Relationships

### Inherits From
- [XCTest](xctest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [XCTActivity](xctactivity.md)
- [XCTWaiterDelegate](xctwaiterdelegate.md)

## See Also

- [Defining Test Cases and Test Methods](defining-test-cases-and-test-methods.md)
  Add test cases and test methods to a test target to confirm that your code performs as expected.
- [class XCTest](xctest.md)
  An abstract base class for creating, managing, and executing tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase)*