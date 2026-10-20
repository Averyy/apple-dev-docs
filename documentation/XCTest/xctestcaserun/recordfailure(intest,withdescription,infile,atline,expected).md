# recordFailure(inTest:withDescription:inFile:atLine:expected:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Records a test failure during test execution for this test run.

> **Deprecated**: Use [`record(_:)`](../xctestrun/record%28_%29.md) instead.

## Declaration

```swift
func recordFailure(inTest testCase: XCTestCase, withDescription description: String, inFile filePath: String, atLine lineNumber: Int, expected: Bool)
```

```objc
- (void) recordFailureInTest:(XCTestCase *) testCase withDescription:(NSString *) description inFile:(NSString *) filePath atLine:(NSUInteger) lineNumber expected:(BOOL) expected;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcaserun/recordfailure(intest:withdescription:infile:atline:expected:))*