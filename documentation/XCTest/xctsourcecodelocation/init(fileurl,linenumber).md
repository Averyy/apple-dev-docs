# init(fileURL:lineNumber:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes a new instance with a file URL and a line number.

## Declaration

```swift
init(fileURL: URL, lineNumber: Int)
```

```objc
- (instancetype) initWithFileURL:(NSURL *) fileURL lineNumber:(NSInteger) lineNumber;
```

## Parameters

- `fileURL`: A file URL that represents the file-system location of the source code file.
- `lineNumber`: An integer that represents a line of code in the source code file.

## See Also

### Initializers
- [convenience init(filePath: String, lineNumber: Int)](./init%28filepath,linenumber%29-3hzmr.md)
  Initializes a new instance with a file path and a line number.
- [convenience init(filePath: StaticString, lineNumber: UInt)](./init%28filepath,linenumber%29-8qw52.md)
  Initializes a new instance with a file path and a line number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodelocation/init(fileurl:linenumber:))*