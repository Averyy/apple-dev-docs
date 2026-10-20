# testDuration

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The number of seconds that elapse between when the run starts and when it stops.

## Declaration

```swift
var testDuration: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval testDuration;
```

## See Also

### Tracking Test Durations
- [var startDate: Date?](./startdate.md)
  The date and time when the test run started, or no value if the test hasn’t run.
- [var stopDate: Date?](./stopdate.md)
  The date and time when the test run stopped, or no value if the test hasn’t run.
- [var totalDuration: TimeInterval](./totalduration.md)
  The number of seconds that elapse between when the run starts and when it stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/testduration)*