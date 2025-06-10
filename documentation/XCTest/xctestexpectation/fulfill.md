# fulfill()

**Framework**: XCTest  
**Kind**: method

Marks the expectation as having been met.

## Declaration

```swift
func fulfill()
```

#### Discussion

It is an error to call this method on an expectation that has already been fulfilled, or when the test case that vended the expectation has already completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/fulfill())*