# testLogWithFormat:

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Logs test results to the test log.

## Declaration

```objc
- (void) testLogWithFormat:(NSString *) format;
```

## Parameters

- `format`: A string that describes a test result by replacing format indicators with variable data, such as failure details, source code file names, and line numbers.

## See Also

### Logging Test Results
- [var logFileHandle: FileHandle!](./logfilehandle.md)
  An object to interact with the test log file.
- [func testLog(withFormat: String!, arguments: CVaListPointer)](./testlog%28withformat,arguments%29.md)
  Logs test results to the test log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestlog/testlogwithformat:)*