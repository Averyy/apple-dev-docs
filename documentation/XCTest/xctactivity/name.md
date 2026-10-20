# name

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A human-readable name for the activity.

## Declaration

```swift
var name: String { get }
```

```objc
@property (copy, readonly) NSString * name;
```

#### Discussion

The activity’s name is used to group the activity within test output in Xcode test reports.

For activities created with the [`XCTContext`](../xctcontext.md) [`runActivityNamed:block:`](../xctcontext/runactivitynamed_block_.md) class method, the [`name`](./name.md) property will match the `name` parameter passed to the class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctactivity/name)*