# init(description:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates a new [`XCTestExpectation`](../xctestexpectation.md) with the provided description.

## Declaration

```swift
init(description expectationDescription: String)
```

```objc
- (instancetype) initWithDescription:(NSString *) expectationDescription;
```

## Discussion

To fulfill an expectation that was created with this initializer, call the expectation’s [`fulfill()`](./fulfill%28%29.md) method when the asynchronous task in your test has completed.

## Parameters

- `expectationDescription`: A string to display in the test log for this expectation, to help diagnose failures.

## See Also

### Creating Expectations
- [var expectationDescription: String](./expectationdescription.md)
  A human readable string used to describe the expectation in log output and test reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/init(description:))*