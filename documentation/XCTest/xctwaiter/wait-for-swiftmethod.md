# wait(for:)

**Framework**: XCTest  
**Kind**: method

Waits on a group of expectations.

## Declaration

```swift
func wait(for expectations: [XCTestExpectation]) -> XCTWaiter.Result
```

#### Return Value

A value describing the outcome of waiting for `expectations`.

#### Discussion

The following example demonstrates how to wait on exceptions:

```objc
- (void)testSprockets {
    // The test allows 60 seconds total for execution.
    self.executionTimeAllowance = 60;

    MySprocket *sprocket = [[MySprocket alloc] init];

    XCTestExpectation *sprocketLoaded = [self expectationWithDescription:@"sprocket loaded"];
    [sprocket loadUsingBlock:^(NSUInteger toothCount) {
        if (toothCount == 6) {
            [sprocketLoaded fulfill];
        }
    }];
    [self waitForExpectations:@[sprocketLoaded]];

    id orbitWobbled = [self keyValueObservingExpectationForObject:sprocket
                                                          keyPath:@"orbitAngle.doubleValue"
                                                    expectedValue:@90.0];
    dispatch_async(myQueue, ^ {
        [sprocket wobbleOrbit];
    });
    [self waitForExpectations:@[orbitWobbled]];
}
```

Expectations can only appear in the array once.

The call may return before the timeout if the test fulfills all the expectations you provide.

In Objective-C code, you might use an expectation to wait on a call to an interface that uses a completion handler to return a result. From Swift code, consider calling `withCheckedContinuation(function:_:)` to use [`Concurrency`](https://developer.apple.com/documentation/Swift/concurrency) instead of an expectation to wait on the result of a completion handler.

## Parameters

- `expectations`: An array of expectations the test must satisfy.

## See Also

- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](xctwaiter/fulfillment(of:timeout:enforceorder:)-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:enforceorder:)-swift.method.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:)-swift.method.md)
  Waits on a group of expectations for up to the specified timeout.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:enforceorder:)-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](xctwaiter/fulfillment(of:timeout:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](xctwaiter/wait(for:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations.
- [class func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [XCTWaiter.Result](xctwaiter/result.md)
  Result states returned by a waiter when it completes, times out, fails, or is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/wait(for:)-swift.method)*