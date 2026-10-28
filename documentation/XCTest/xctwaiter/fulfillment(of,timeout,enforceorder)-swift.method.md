# fulfillment(of:timeout:enforceOrder:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@discardableResult
@nonobjc func fulfillment(of expectations: [XCTestExpectation], timeout seconds: TimeInterval = .infinity, enforceOrder enforceOrderOfFulfillment: Bool = false) async -> XCTWaiter.Result
```

## Return Value

A value describing the outcome of waiting for `expectations`.

## Discussion

Use this concurrency-safe alternative to [`wait(for:timeout:enforceOrder:)`](./wait%28for,timeout,enforceorder%29-swift.type.method.md) from async Swift functions. A call to [`wait(for:timeout:enforceOrder:)`](./wait%28for,timeout,enforceorder%29-swift.type.method.md) runs synchronously and blocks the calling thread, which can cause deadlocks or priority inversions.

The following example demonstrates how to wait on exceptions in a test using concurrency:

```swift
func testSprockets() async throws {
    // The test allows 60 seconds total for execution.
    self.executionTimeAllowance = 60

    let sprocket = MySprocket()
    
    let sprocketLoaded = expectation(description: "sprocket loaded")
    sprocket.load() { toothCount in
        if toothCount == 6 {
            sprocketLoaded.fulfill()
        }
    }
    await fulfillment(of: [sprocketLoaded])

    let orbitWobbled = expectation(that: \.orbitAngle.doubleValue, on: sprocket, willEqual: 90.0)
    Task {
        sprocket.wobbleOrbit()
    }
    await fulfillment(of: [orbitWobbled])
}
```

Expectations can only appear in the array once. The call may return before the timeout if the test fulfills all the expectations you provide.

> **Note**:  If you don’t specify a timeout when calling this function, enable test timeouts to prevent unfulfilled expectation from hanging the test.

## Parameters

- `expectations`: An array of expectations the test must satisfy.
- `seconds`: The time, in seconds, the test allows for the fulfillment of the expectations. The default timeout allows the test to run until it reaches its execution time allowance.
- `enforceOrderOfFulfillment`: If [`true`](../../Swift/true.md), the test must fulfill the expectations in the order they appear in the array.

## See Also

### Waiting for Expectations
- [func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](./wait%28for%29-swift.method.md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,enforceorder%29-swift.method.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](./wait%28for,timeout%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,timeout,enforceorder%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](./fulfillment%28of,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](./wait%28for%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations.
- [class func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](./wait%28for,timeout%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [XCTWaiter.Result](./result.md)
  Result states returned by a waiter when it completes, times out, fails, or is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/fulfillment(of:timeout:enforceorder:)-swift.method)*