# Analyzing responsiveness issues in your shipping app

**Framework**: Xcode

Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.

#### Overview

Hitches and hangs are two types of responsiveness issues that negatively impact an app’s user experience. The system monitors for hangs and hitches for running apps, and periodically collects reports on the issues from a statistical sample. Xcode Organizer uses this data to display information about the hitch rate, the hang rate, and individual hang reports for your apps. All of this data is also available in [`MetricKit`](https://developer.apple.com/documentation/MetricKit), so you can gather and aggregate it in your own infrastructure. For more information about hangs and hitches, see [`Understanding user interface responsiveness`](understanding-user-interface-responsiveness.md).

##### View Your Apps Hitch Rate

The Scrolling pane of the Xcode Organizer window displays information about the hitch rate of your app over time.

![A screenshot of the Scrolling metric pane in the Xcode Organizer window. From left to right are the list of metrics and reports, the metric UI with a bar graph showing the scroll hitch rate for the past 12 app versions, the selected version, the comparison data for the selected and latest versions, and the goal keys.](https://docs-assets.developer.apple.com/published/c3c3c4a0f84ff4296c49fa46853d90c4/improving-app-responsiveness-1%402x.png)

Based on the scroll hitch rate for a version of your app, the bar appears in red, yellow, or green. Red bars indicate a poor scroll with a hitch rate of more than 10 milliseconds per second (ms/s), yellow bars indicate a fair scroll with a hitch rate of 5–10 ms/s, and green bars indicate a good scroll with a hitch rate of less than 5 ms/s. Aim for green bars to provide the best scroll experience for your users.

Hitch-rate data is only available for iOS and iPadOS devices.

##### View Your Apps Hang Rate

Xcode Organizer reports the hang rate as the number of seconds per hour that the app is unresponsive, while only counting periods of unresponsiveness of more than 250 ms. The Organizer window shows both the median hang rate of a typical user experience, and the extreme 90th percentile hang rate. [`MetricKit`](https://developer.apple.com/documentation/MetricKit) provides the same hang rate metric as a histogram.

![A screenshot of the Hang Rate metric pane in the Xcode Organizer window. From left to right are the list of metrics and reports, the metric UI with a bar graph showing the hang rate for the past 12 app versions, the selected version, and the comparison data for the selected and latest versions.](https://docs-assets.developer.apple.com/published/402d2ecc35e6998f4dc9fb27dd7ca9c7/improving-app-responsiveness-2%402x.png)

Apple operating systems support a broad variety of devices with different hardware capabilities and performance characteristics. Code that performs flawlessly on one hardware model can hang on another. Use the device filter at the top of the Organizer window to filter the hang rate for specific device types and uncover hangs that only manifest in certain circumstances.

Hang rate data is available for iOS and macOS devices.

##### Analyze Hang Reports to Determine a Course of Action

The hang rate provides general information about how responsive a specific app version is on average, while hang reports highlight individual causes of hangs. When the main thread is unresponsive for 1 s or longer, the system also samples the app to capture a backtrace profile, highlighting where the app is spending its time during the hang. The system sends anonymous diagnostic reports with hang stack traces to Apple for users who consent to share data with app developers. Xcode Organizer aggregates these individual hang reports and groups them by similar backtraces to identify common causes of hangs. Alternatively, you can create your own reports from logs that [`MetricKit`](https://developer.apple.com/documentation/MetricKit) collects.

![A screenshot of the Hang reports pane in the Xcode Organizer window. From left to](https://docs-assets.developer.apple.com/published/4e74644803213a17e7b261aa4f2ebeb1/analyzing-responsiveness-issues-in-your-shipping-app-1%402x.png)

Each report in the Report List shows the function call that generates the hang, and the percentage of total hang time it accounts for in the release. The Report List sorts function calls in descending order of hang-time contribution to the app release. Clicking a report shows a sample main thread stack trace, as well as additional details in the Inspector, including:

- iOS version
- Device model
- Number of logs received
- 14-day reporting trend
- Total hang time

Details such as iOS version, device model, number of logs received, and 14-day reporting trend refer to the report, whereas details such as total hang time refer to the function calls.

Identify the code that’s causing the hang by using the function calls for a specific report in the Report List and the corresponding stack trace.

Hang reports are only available for iOS and iPadOS devices.

##### Reproduce Problems to Analyze and Fix Them

The metrics in Xcode Organizer allow you to detect when your shipping app has a problem, such as the hitch rate increasing with the most recent release, but not necessarily what the cause of the problem is. To determine the source of the problem, consider the following steps:

- Filter the relevant metric by various dimensions, such as device type or app version, to identify whether the issue occurs only on a specific combination of device and version of your app.
- Identify the first app version that has the issue you’re looking for. Then use a version control system to identify the changes between app versions, and focus your testing on those areas.

After you narrow down the areas of the app where the issue may be occurring, focus your testing on trying to reproduce the issue. You can use the on-device hang detection in iOS and iPadOS to receive notifications about a hang that occurs while you use the device. Or you can attach your device to Instruments and profile your app using the Time Profiler template to see any hangs in the trace while also recording additional data about what happens in your app during the hang. Then, follow the steps in [`Improving app responsiveness`](improving-app-responsiveness.md) to analyze and fix the issues.

## See Also

- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Understanding user interface responsiveness](understanding-user-interface-responsiveness.md)
  Make your app more responsive by examining the event-handling and rendering loop.
- [Understanding and improving SwiftUI performance](understanding-and-improving-swiftui-performance.md)
  Identify and address long-running view updates, and reduce the frequency of updates.
- [Understanding hangs in your app](understanding-hangs-in-your-app.md)
  Determine the cause for delays in user interactions by examining the main thread and the main run loop.
- [Understanding hitches in your app](understanding-hitches-in-your-app.md)
  Determine the cause of interruptions in motion by examining the render loop.
- [Diagnosing performance issues early](diagnosing-performance-issues-early.md)
  Diagnose potential performance issues in your app during testing with the Thread Performance Checker tool in Xcode.
- [Reducing your app’s launch time](reducing-your-app-s-launch-time.md)
  Create a more responsive experience with your app by minimizing time spent in startup.
- [Reducing terminations in your app](reduce-terminations-in-your-app.md)
  Minimize how frequently the system stops your app by addressing common termination reasons.
- [Reducing disk writes](reducing-disk-writes.md)
  Improve your app’s responsiveness by optimizing how it writes data to permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-responsiveness-issues-in-your-shipping-app)*