# init(description:)

**Framework**: Xctest  
**Kind**: init

Creates a new [`XCTestExpectation`](xctestexpectation.md) with the provided description.

## Declaration

```swift
init(description expectationDescription: String)
```

#### Discussion

To fulfill an expectation that was created with this initializer, call the expectation’s [`fulfill()`](xctestexpectation/fulfill().md) method when the asynchronous task in your test has completed.

## Parameters

- `expectationDescription`: A string to display in the test log for this expectation, to help diagnose failures.

## See Also

- [var expectationDescription: String](xctestexpectation/expectationdescription.md)
  A human readable string used to describe the expectation in log output and test reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/init(description:))*