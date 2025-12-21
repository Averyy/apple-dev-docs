# init(waitUntilResponsive:)

**Framework**: XCTest  
**Kind**: init

Initializes a metric that records the time for an app to display its first frame to screen and complete all extended launch tasks, or to display its first frame and wait until the app is responsive.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(waitUntilResponsive: Bool)
```

## Parameters

- `waitUntilResponsive`: If  , the metric tracks time until the app has displayed its first frame and completed all extended launch tasks that   starts.

## See Also

- [class MXMetricManager](../MetricKit/MXMetricManager#4001121.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [init()](xctapplicationlaunchmetric/init.md)
  Initializes a metric that records the time for an app to display its first frame to screen and complete all extended launch tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctapplicationlaunchmetric/init(waituntilresponsive:))*