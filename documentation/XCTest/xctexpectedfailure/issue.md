# issue

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The issue that fulfills the expected failure.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var issue: XCTIssue { get }
```

*macOS*

```swift
@NSCopying
var issue: XCTIssueReference { get }
```

```objc
@property (copy, readonly) XCTIssue * issue;
```

## See Also

### Detailing Expected Failure
- [var failureReason: String?](./failurereason.md)
  An optional string that describes why the test expects a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/issue)*