# Asynchronous Tests and Expectations

**Framework**: Xctest

Verify that asynchronous code behaves as expected.

#### Overview

Asynchronous code doesn’t execute directly within the current flow of code. This might be because the code runs on a different thread or dispatch queue, in a delegate method, or in a callback, or because it’s a Swift function marked with `async`.

`XCTest` provides two approaches for testing asynchronous code. For Swift code that uses `async` and `await` for concurrency, you mark your test methods `async` or `async` `throws` to test asynchronously. For any other types of asynchronous code, within your test you create one or more , which are objects that XCTest uses to handle waiting. Then you  those expectations when the asynchronous code finishes running to tell XCTest to stop waiting. Your test method waits until all expectations are fulfilled or a specified timeout expires.

##### Build Asynchronous Tests with Swift Concurrency

To test Swift code that uses `async` and `await` for concurrency, mark your test method `async` or `async` `throws`. `XCTest` executes your test method asynchronously so that your test waits until `async` calls complete.

```swift
func testDownloadWebDataWithConcurrency() async throws {
    // Create a URL for a webpage to download.
    let url = URL(string: "https://apple.com")!
    
    // Use an asynchronous function to download the webpage.
    let dataAndResponse: (data: Data, response: URLResponse) = try await URLSession.shared.data(from: url, delegate: nil)
    
    // Assert that the actual response matches the expected response.
    let httpResponse = try XCTUnwrap(dataAndResponse.response as? HTTPURLResponse, "Expected an HTTPURLResponse.")
    XCTAssertEqual(httpResponse.statusCode, 200, "Expected a 200 OK response.")
}
```

When the asynchronous task completes, perform assertions to confirm that the task’s actual results meet your expected results.

If your test encounters a thrown error, `XCTest` records a test failure.

> ❗ **Important**:  If your test code needs to run on the Main actor, specify `@MainActor` for your test method or class. If you don’t specify an actor, the test method executes on an arbitrary actor.

 If your test code needs to run on the Main actor, specify `@MainActor` for your test method or class. If you don’t specify an actor, the test method executes on an arbitrary actor.

##### Build Asynchronous Tests with Expectations

When you can’t use Swift `async`, use expectations to test asynchronous code. For example, use expectations when there isn’t a Swift `async` alternative available or when your asynchronous code runs in:

- Objective-C
- An asynchronous block in a dispatch queue
- A delegate method
- An asynchronous callback, closure, or completion block
- A `Future` or `Promise` in Swift Combine
- A situation where it needs to complete within a specific amount of time

Before you perform an asynchronous task in your test method, create an instance of [`XCTestExpectation`](xctestexpectation.md) with a description of the task.

```swift
// Create an expectation for an asynchronous task.
let expectation = XCTestExpectation(description: "Open a file asynchronously.")
```

Start the asynchronous task, and then tell the test to wait for the expectation to complete within an amount of time you specify.

```swift
let fileManager = ExampleFileManager()

// Perform the asynchronous task.
fileManager.openFileAsync(with: "exampleFilename") { file, error in
    //...
}

// Wait for the expectation to fulfill or time out.
wait(for: [expectation], timeout: 10.0)
```

When the asynchronous task returns (for example, in a callback), perform assertions to confirm that the task’s actual results meet your expected results. When the task completes, call the [`fulfill()`](xctestexpectation/fulfill().md) method on the expectation to indicate to the test that it can stop waiting and proceed with the next test.

```swift
fileManager.openFileAsync(with: "exampleFilename") { file, error in

    // Assert that the asynchronous task worked.
    XCTAssertNotNil(file, "Expected to load a file.")

    // Assert that no errors occurred opening the file asynchronously.
    XCTAssertNil(error, "Expected no errors loading a file.")
    
    // Fulfill the expectation.
    expectation.fulfill()
}

```

If the test doesn’t execute the `fulfill()` method before the wait statement’s timeout expires, `XCTest` records a test failure.

## Topics

### Expectations
- [class XCTestExpectation](xctestexpectation.md)
  An expected outcome in an asynchronous test.
### Key Value Observing Expectations
- [class XCTKVOExpectation](xctkvoexpectation.md)
  An expectation that a specific key-value observing (KVO) condition fulfills.
- [class XCTKeyPathExpectation](xctkeypathexpectation.md)
  An expectation that a specific key-value observing (KVO) condition fulfills.
### Notification-Based Expectations
- [class XCTNSNotificationExpectation](xctnsnotificationexpectation.md)
  An expectation that is fulfilled when an expected `NSNotification` is received.
- [class XCTDarwinNotificationExpectation](xctdarwinnotificationexpectation.md)
  An expectation that is fulfilled when an expected Darwin notification is received.
### Predicate-Based Expectations
- [class XCTNSPredicateExpectation](xctnspredicateexpectation.md)
  An expectation that’s fulfilled when an `NSPredicate` is satisfied.
### Expectation Waiters
- [class XCTWaiter](xctwaiter.md)
  Waits for the fulfillment of a group of expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations)*