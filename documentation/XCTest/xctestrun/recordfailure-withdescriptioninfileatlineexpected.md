# recordFailure(withDescription:inFile:atLine:expected:)

**Framework**: XCTest  
**Kind**: method

Records a failure during test execution for the test run.

**Availability**:
- Unknown ?+ - Deprecated

## Declaration

```swift
func recordFailure(withDescription description: String, inFile filePath: String?, atLine lineNumber: Int, expected: Bool)
```

#### Discussion

Don’t call this method before the test run starts or after it stops.

## Parameters

- `description`: The description of the failure.
- `filePath`: The file path to the source file where the failure occurred or   if unknown.
- `lineNumber`: The line number in the source file at   where the failure occurred.
- `expected`:   if the failure was the result of a failed assertion,   if it was the result of an uncaught exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/recordfailure(withdescription:infile:atline:expected:))*