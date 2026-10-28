# perform(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Executes a specific test.

## Declaration

```swift
func perform(_ run: XCTestRun)
```

```objc
- (void) performTest:(XCTestRun *) run;
```

## Discussion

Must be overridden by subclasses.

## Parameters

- `run`: The test run to perform.

## See Also

### Running Tests
- [func run()](./run%28%29.md)
  Creates a test run instance and starts the test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/perform(_:))*