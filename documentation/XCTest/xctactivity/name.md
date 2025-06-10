# name

**Framework**: XCTest  
**Kind**: property  
**Required**: Yes

A human-readable name for the activity.

## Declaration

```swift
var name: String { get }
```

#### Discussion

The activity’s name is used to group the activity within test output in Xcode test reports.

For activities created with the [`XCTContext`](xctcontext.md) [`runActivityNamed:block:`](xctcontext/runactivitynamed:block:.md) class method, the [`name`](xctactivity/name.md) property will match the `name` parameter passed to the class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctactivity/name)*