# recordFailure(withDescription:inFile:atLine:expected:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Records a failure during test execution for the test run.

> **Deprecated**: Use [`record(_:)`](./record%28_%29.md) instead.

## Declaration

```swift
func recordFailure(withDescription description: String, inFile filePath: String?, atLine lineNumber: Int, expected: Bool)
```

```objc
- (void) recordFailureWithDescription:(NSString *) description inFile:(NSString *) filePath atLine:(NSUInteger) lineNumber expected:(BOOL) expected;
```

#### Discussion

Don’t call this method before the test run starts or after it stops.

## Parameters

- `description`: The description of the failure.
- `filePath`: The file path to the source file where the failure occurred or `nil` if unknown.
- `lineNumber`: The line number in the source file at `filePath` where the failure occurred.
- `expected`: [`true`](../../Swift/true.md) if the failure was the result of a failed assertion, [`false`](../../Swift/false.md) if it was the result of an uncaught exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/recordfailure(withdescription:infile:atline:expected:))*