# init(_:file:line:)

**Framework**: XCTest  
**Kind**: init

Intitializes an error to skip a test.

## Declaration

```swift
init(_ message: String? = nil, file: StaticString = #filePath, line: UInt = #line)
```

## Parameters

- `message`: A description of the skip.
- `file`: The file in which the skip occurred. This value defaults to the file name of the test case in which this error was initialized.
- `line`: The line number on which the skip occurred. This value defaults to the line number on which this error was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctskip-swift.struct/init(_:file:line:))*