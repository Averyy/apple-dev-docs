# testLog(withFormat:arguments:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Logs test results to the test log.

## Declaration

```swift
func testLog(withFormat format: String!, arguments: CVaListPointer)
```

```objc
- (void) testLogWithFormat:(NSString *) format arguments:(va_list) arguments;
```

## Parameters

- `format`: A string that describes a test result by replacing format indicators with variable data, such as failure details, source code filenames, and line numbers.
- `arguments`: Variable data to replace in the format string, such as failure details, source code filenames, and line numbers.

## See Also

### Logging Test Results
- [var logFileHandle: FileHandle!](./logfilehandle.md)
  An object to interact with the test log file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestlog/testlog(withformat:arguments:))*