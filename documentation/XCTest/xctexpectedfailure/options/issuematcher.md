# issueMatcher

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

A block of code that determines whether the test issue fulfills the expected failure.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var issueMatcher: (XCTIssue) -> Bool { get set }
```

*macOS*

```swift
var issueMatcher: (XCTIssueReference) -> Bool { get set }
```

```objc
@property (copy) BOOL (^issueMatcher)(XCTIssue *);
```

#### Discussion

Provide code to examine the issue and respond with a Boolean value indicating whether the issue fulfills the expected failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options/issuematcher)*