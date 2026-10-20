# startDate

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The date and time when the test run started, or no value if the test hasn’t run.

## Declaration

```swift
var startDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * startDate;
```

## See Also

### Tracking Test Durations
- [var stopDate: Date?](./stopdate.md)
  The date and time when the test run stopped, or no value if the test hasn’t run.
- [var testDuration: TimeInterval](./testduration.md)
  The number of seconds that elapse between when the run starts and when it stops.
- [var totalDuration: TimeInterval](./totalduration.md)
  The number of seconds that elapse between when the run starts and when it stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/startdate)*