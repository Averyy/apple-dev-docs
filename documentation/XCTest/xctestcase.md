# XCTestCase

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

The primary class for defining test cases, test methods, and performance tests.

## Declaration

```swift
class XCTestCase
```

```objc
@interface XCTestCase : XCTest
```

## Mentions

- [Defining Test Cases and Test Methods](./defining-test-cases-and-test-methods.md)
- [Set Up and Tear Down State in Your Tests](./set-up-and-tear-down-state-in-your-tests.md)
- [Adding Attachments to Tests, Activities, and Issues](./adding-attachments-to-tests-activities-and-issues.md)
- [Grouping Tests into Substeps with Activities](./grouping-tests-into-substeps-with-activities.md)

## Overview

A test case is a group of related test methods, with optional setup and teardown before and after tests run. See [Defining Test Cases and Test Methods](./defining-test-cases-and-test-methods.md) for more information.

`XCTestCase` conforms to [`XCTActivity`](./xctactivity.md), so you can simplify complex tests by organizing them into activities, and attach output to tests for later analysis. For more information, see [Activities and Attachments](./activities-and-attachments.md).

Create tests for asynchronous operations using expectations. For more information, see `Testing Asynchronous Operations with Expectations`. If your app uses Swift [Concurrency](../Swift/concurrency.md), annotate test methods with `async` or `async throws` instead to test asynchronous operations, and use standard Swift concurrency patterns in your tests.

Create tests to measure performance for specific blocks of code using the methods in the Measuring Performance section below. Build performance tests as part of a continuous improvement cycle for performance in your app. For more information, see [Improving your app’s performance](../Xcode/improving-your-app-s-performance.md).

## Topics

### Customizing Test Setup and Teardown
- [Set Up and Tear Down State in Your Tests](./set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [class func setUp()](./xctestcase/setup%28%29.md)
  Provides an opportunity to customize initial state before a test case begins.
- [func addTeardownBlock(() async throws -> Void)](./xctestcase/addteardownblock%28_%29-2guon.md)
  Registers a block of teardown code to run after the current test method ends.
- [func addTeardownBlock(() throws -> Void)](./xctestcase/addteardownblock%28_%29-5zw6c.md)
  Registers a block of teardown code to run after the current test method ends.
- [class func tearDown()](./xctestcase/teardown%28%29.md)
  Provides an opportunity to perform cleanup after a test case ends.
- [- addAsyncTeardownBlock:](./xctestcase/addasyncteardownblock_.md)
  Registers a block of asynchronous teardown code to run after the current test method ends.
- [- addTeardownBlock:](./xctestcase/addteardownblock_.md)
  Registers a block of teardown code to run after the current test method ends.
### Managing Test Case Execution
- [class var runsForEachTargetApplicationUIConfiguration: Bool](./xctestcase/runsforeachtargetapplicationuiconfiguration.md)
  A Boolean value that indicates whether your UI tests run once for each possible combination of orientation, localization, and other appearance settings your app supports.
- [var continueAfterFailure: Bool](./xctestcase/continueafterfailure.md)
  A Boolean value that indicates whether a test method should continue running after a failure occurs.
- [var executionTimeAllowance: TimeInterval](./xctestcase/executiontimeallowance.md)
  The number of seconds, rounded up to the nearest minute, for a test to run before it fails with a timeout error.
### Measuring Performance
- [func measure(() -> Void)](./xctestcase/measure%28_%29.md)
  Measures the performance of a block of code.
- [func measureMetrics([XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for: () -> Void)](./xctestcase/measuremetrics%28_,automaticallystartmeasuring,for%29.md)
  Measures the performance of a block of code, optionally deferring the starting point for measurement.
- [func measure(metrics: [any XCTMetric], block: () -> Void)](./xctestcase/measure%28metrics,block%29.md)
  Records the selected metrics for a block of code.
- [func measure(metrics: [any XCTMetric], options: XCTMeasureOptions, block: () -> Void)](./xctestcase/measure%28metrics,options,block%29.md)
  Records the selected metrics, using the specified measurement options, for a block of code.
- [func measure(options: XCTMeasureOptions, block: () -> Void)](./xctestcase/measure%28options,block%29.md)
  Records the performance, using the specified measurement options, for a block of code.
- [func startMeasuring()](./xctestcase/startmeasuring%28%29.md)
  Starts recording performance metrics within a block of code.
- [func stopMeasuring()](./xctestcase/stopmeasuring%28%29.md)
  Ends recording performance metrics within a block of code.
- [class var defaultPerformanceMetrics: [XCTPerformanceMetric]](./xctestcase/defaultperformancemetrics.md)
  An array of default performance metrics the test records.
- [class var defaultMetrics: [any XCTMetric]](./xctestcase/defaultmetrics.md)
  An array of default metrics the test uses to record performance.
- [class var defaultMeasureOptions: XCTMeasureOptions](./xctestcase/defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.
- [struct XCTPerformanceMetric](./xctperformancemetric.md)
  Performance metrics that the test records.
### Creating Asynchronous Test Expectations
- [func expectation(description: String) -> XCTestExpectation](./xctestcase/expectation%28description%29.md)
  Creates a new expectation with an associated description.
- [func expectation(for: NSPredicate, evaluatedWith: Any?, handler: XCTNSPredicateExpectation.Handler?) -> XCTestExpectation](./xctestcase/expectation%28for,evaluatedwith,handler%29.md)
  Creates an expectation that the test fulfills by evaluating the predicate with the specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](./xctestcase/expectation%28fornotification,object,handler%29.md)
  Creates an expectation that the test fulfills when it receives a specific notification for a specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](./xctestcase/expectation%28fornotification,object,notificationcenter,handler%29.md)
  Creates an expectation that the test fulfills when it receives a specific notification from a specific notification center for a specified object.
- [func keyValueObservingExpectation(for: Any, keyPath: String, expectedValue: Any?) -> XCTestExpectation](./xctestcase/keyvalueobservingexpectation%28for,keypath,expectedvalue%29.md)
  Creates an expectation that uses Key-Value Observing to observe a value until it matches an expected value.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willEqual: V) -> XCTKeyPathExpectation<T, V>](./xctestcase/expectation%28that,on,options,willequal%29.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes to an expected value.
- [func keyValueObservingExpectation(for: Any, keyPath: String, handler: XCTKVOExpectation.Handler?) -> XCTestExpectation](./xctestcase/keyvalueobservingexpectation%28for,keypath,handler%29.md)
  Creates an expectation that uses Key-Value Observing to observe a value and respond to changes in that value by calling a provided handler.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.Predicate?) -> XCTKeyPathExpectation<T, V>](./xctestcase/expectation%28that,on,options,willsatisfy%29-6itb.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes and satisfies the conditions of a predicate’s evaluation.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.AsynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./xctestcase/expectation%28that,on,options,willsatisfy%29-292oj.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.SynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./xctestcase/expectation%28that,on,options,willsatisfy%29-85or0.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
### Waiting for Expectations
- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async](./xctestcase/fulfillment%28of,timeout,enforceorder%29.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation])](./xctestcase/wait%28for%29.md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool)](./xctestcase/wait%28for,enforceorder%29.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval)](./xctestcase/wait%28for,timeout%29.md)
  Waits for the test to fulfill a set of expectations within a specified time.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool)](./xctestcase/wait%28for,timeout,enforceorder%29.md)
  Waits for the test to satisfy an array of expectations and specifies whether they must occur in the array’s order.
- [func waitForExpectations(timeout: TimeInterval, handler: (((any Error)?) -> Void)?)](./xctestcase/waitforexpectations%28timeout,handler%29.md)
  Waits until the test fulfills all expectations or until it times out.
- [typealias XCWaitCompletionHandler](./xcwaitcompletionhandler.md)
  A block the test runner calls when the test fulfills a waiter’s expectations, or when it times out.
- [struct XCTestError](./xctesterror.md)
  A type of error that can occur while the test waits to fulfill expectations.
- [XCTestError.Code](./xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
- [let XCTestErrorDomain: String](./xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.
### Monitoring UI Interruptions
- [Handling UI Interruptions](./handling-ui-interruptions.md)
  Improve your UI test’s stability by handling interface changes that block the UI elements under test.
- [func addUIInterruptionMonitor(withDescription: String, handler: (XCUIElement) -> Bool) -> any NSObjectProtocol](./xctestcase/adduiinterruptionmonitor%28withdescription,handler%29.md)
  Adds a handler to the current context.
- [func removeUIInterruptionMonitor(any NSObjectProtocol)](./xctestcase/removeuiinterruptionmonitor%28_%29.md)
  Removes a handler using the token from when you added the handler.
### Creating Tests Programmatically
- [init(invocation: NSInvocation?)](./xctestcase/init%28invocation%29.md)
  Initializes a test case with an invocation.
- [init(selector: Selector)](./xctestcase/init%28selector%29.md)
  Initializes a test case with a selector.
- [class var testInvocations: [NSInvocation]](./xctestcase/testinvocations.md)
  An array of invocations that represents each test method in the test case.
- [var invocation: NSInvocation?](./xctestcase/invocation.md)
  The invocation for running the test.
- [func invokeTest()](./xctestcase/invoketest%28%29.md)
  Invokes the test.
- [func record(XCTIssue)](./xctestcase/record%28_%29.md)
  Records an issue during test execution.
- [func recordFailure(withDescription: String, inFile: String, atLine: Int, expected: Bool)](./xctestcase/recordfailure%28withdescription,infile,atline,expected%29.md)
  Records a failure during text execution.
- [class var defaultTestSuite: XCTestSuite](./xctestcase/defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.
- [+ testCaseWithInvocation:](./xctestcase/testcasewithinvocation_.md)
  Creates a test case with an invocation.
- [+ testCaseWithSelector:](./xctestcase/testcasewithselector_.md)
  Creates a test case with a selector.

## Relationships

### Inherits From
- [XCTest](./xctest-page.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [XCTActivity](./xctactivity.md)
- [XCTWaiterDelegate](./xctwaiterdelegate.md)

## See Also

### Test cases and test methods
- [Defining Test Cases and Test Methods](./defining-test-cases-and-test-methods.md)
  Add test cases and test methods to a test target to confirm that your code performs as expected.
- [class XCTest](./xctest-page.md)
  An abstract base class for creating, managing, and executing tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase)*