# issueMatcher

**Framework**: Xctest  
**Kind**: property

A block of code that determines whether the test issue fulfills the expected failure.

## Declaration

```swift
var issueMatcher: (XCTIssue) -> Bool { get set }
```

#### Discussion

Provide code to examine the issue and respond with a Boolean value indicating whether the issue fulfills the expected failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options/issuematcher)*