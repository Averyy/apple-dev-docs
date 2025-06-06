# init()

**Framework**: Xctest  
**Kind**: init

Initializes a metric that records the time for an app to display its first frame to screen and complete all extended launch tasks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init()
```

#### Discussion

If you didn’t start any extended launch tasks using [`extendLaunchMeasurement(forTaskID:)`](https://developer.apple.com/documentation/MetricKit/MXMetricManager/extendLaunchMeasurement(forTaskID:)), this metric measures only the time for your app to display its first frame to screen.

## See Also

- [init(waitUntilResponsive: Bool)](xctapplicationlaunchmetric/init(waituntilresponsive:).md)
  Initializes a metric that records the time for an app to display its first frame to screen and complete all extended launch tasks, or to display its first frame and wait until the app is responsive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctapplicationlaunchmetric/init())*