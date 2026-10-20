# run()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Creates a test run instance and starts the test.

## Declaration

```swift
func run()
```

```objc
- (void) runTest;
```

#### Discussion

Creates an instance of the class that [`testRunClass`](./testrunclass.md) specifies, and passes it as a parameter to the [`perform(_:)`](./perform%28_%29.md) method.

## See Also

### Running Tests
- [func perform(XCTestRun)](./perform%28_%29.md)
  Executes a specific test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/run())*