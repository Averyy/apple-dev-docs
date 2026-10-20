# init(waitUntilResponsive:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithWaitUntilResponsive:(BOOL) waitUntilResponsive;
```

## Parameters

- `waitUntilResponsive`: A Boolean that enables the metric to track time until the main thread is responsive after displaying the first frame.

  If `false`, the metric tracks time until the app has displayed its first frame and completed all extended launch tasks that [`extendLaunchMeasurement(forTaskID:)`](../../MetricKit/mxmetricmanager/extendlaunchmeasurement%28fortaskid%29.md) starts.

## See Also

### Related Documentation
- [class MXMetricManager](../../MetricKit/mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
### Initializers
- [init()](./init%28%29.md)
  Initializes a metric that records the time for an app to display its first frame to screen and complete all extended launch tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctapplicationlaunchmetric/init(waituntilresponsive:))*