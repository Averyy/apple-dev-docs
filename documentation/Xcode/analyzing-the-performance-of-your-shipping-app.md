# Analyzing the performance of your shipping app

**Framework**: Xcode

View power and performance metrics for apps you distribute through the App Store.

#### Overview

Use the Xcode Organizer to view anonymized performance data from your app’s users, including launch times, memory usage, UI responsiveness, and impact on the battery. Use the data to tune the next version of your app and catch regressions that make it into a specific version of your app.

In Xcode, choose Window > Organizer to open the Organizer window, and then select the desired metric or report. In some cases, the pane shows “Insufficient usage data available” because there may not be enough anonymized data reported from participating user devices. When this happens, try checking back in a few days.

When Xcode has enough information to calculate a recommendation, it displays a recommended value for a metric on the chart displaying your app’s metrics. Use this information to plan and prioritize performance engineering work.

##### Read Data for a Metric

The Xcode Organizer shows a title, description, and graph for each type of metric. In the graph, each bar represents a version of your app. Use the pop-up menus to filter the metric data for different devices and the median or high value. If your app has an App Clip available, use the pop-up menu to filter by app type and switch between viewing metrics for the main app and the App Clip.

![A labeled screenshot of the Hang Rate metric pane in the Xcode Organizer. From left to right are the list of metrics and reports, the metric UI with a bar graph showing the hang rate for the past 12 app versions, and data for the latest app version.](https://docs-assets.developer.apple.com/published/470a1a1e4b68f6a672fd7c01b63b330c/analyzing-the-performance-of-your-shipping-app-1%402x.png)

Metrics that show   in the detail section include an associated margin of error because the existing data is limited. Use this margin of error to determine the upper and lower bounds of the displayed value. The margin of error decreases as data increases. The release date information in this section provides the date when the selected app version is ready for sale.

##### Compare Performance with a Previous App Release

To explore changes between versions for a metric, such as those for Hang Rate in the image below, click the vertical bar for your selected version.

The data for both the selected and latest versions appear to the right of the graph with the higher of the two values in bold. Change information for those versions appears in the details section below the latest version data.

![A labeled screenshot of the comparison view in the Hang Rate metric pane of the Xcode Organizer. Key pieces are the highlighted selected version bar, data for the latest and selected app versions, and change information between those two versions.](https://docs-assets.developer.apple.com/published/dec652d302d51a04c683c1ac27692d45/analyzing-the-performance-of-your-shipping-app-2%402x.png)

##### Compare Your Apps Metrics with Recommended Values

Xcode compares your app’s launch time metrics with other sources, including metrics from similar apps and historical data from your app. If your app has sufficient metrics data available and Xcode determines that the launch time metrics for the current version of your app are greater than the values from other sources, it displays a recommended value for the metric as a dashed line on the histogram in the Xcode Organizer.

> **Note**:  In Xcode 17 Beta 1, metric recommendations are available for the app launch time metric.

##### Read Data for Smart Insights

The Xcode Organizer presents a list of smart insights whenever the system detects new performance regressions for the latest version of your app. Each item in the insights list contains information that provides a brief summary.

![A screenshot that describes each user interface section of the Xcode Organizer. Below the window title is the filter bar to select different metric filter criteria. The Regressions item is selected in the left sidebar to show the Smart Insights regressions for an app. To the right is the insights list and to its right is the detail pane that shows the corresponding insight chart and insight data.](https://docs-assets.developer.apple.com/published/ac2f8ede3e97d808c835b6b3ef07036a/using-smart-insights-to-analyze-the-performance-of-your-shipping-app-2%402x.png)

To the right of the list is the detail pane that shows a chart corresponding to the selected smart insight. Note that the insight for Scroll Hitch Rate for the typical percentile of samples from “iPad (All)” devices is selected. When a selected insight corresponds to more than one percentile, or to different sets of devices, the detail pane presents a scrollable list of additional charts.

To the right of the chart is the insight data showing the metric value for the latest version, as well as the average metric values for the previous four versions. Use this information to see how your latest app version is performing with respect to the average of the previous versions.

Select the Notifications button in the upper-right corner to opt in to power and performance regression notifications. Xcode sends you a notification for the latest version of each of your shipped apps when it detects a high-impact regression. A regression is considered high impact if performance data is available and indicates the latest version of your app regresses 75 percent or more compared to the average of the previous four app versions available in the App Store. Xcode notifies you once per 24-hour period when Xcode is running. To keep notifications to a minimum, Xcode sends you no more than one notification for the same app version.

##### Identify Trending Insights

Xcode displays a flame icon next to reports in the list of smart insight reports for the issues that exhibit the largest regressions over the most recent five versions of your app, if it has enough data available. Click on an individual report to view a bar chart showing the impact trend for the most recent five versions of your app. Use this information to prioritize performance engineering work.

Xcode identifies trending insights for disk writes, hang rate, and launch time metrics.

##### Improve Your Apps Performance

For more details about how to use the data in the Organizer panes to improve the performance of the next version of your app, see the topics below.

## See Also

- [Analyzing responsiveness issues in your shipping app](analyzing-responsiveness-issues-in-your-shipping-app.md)
  Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.
- [Analyzing your app’s battery use](analyzing-your-app-s-battery-use.md)
  Increase the available use time for your app on a single battery charge by reducing your appʼs power consumption.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Reducing disk writes](reducing-disk-writes.md)
  Improve your app’s responsiveness by optimizing how it writes data to permanent storage.
- [Reducing your app’s launch time](reducing-your-app-s-launch-time.md)
  Create a more responsive experience with your app by minimizing time spent in startup.
- [Reducing your app’s memory use](reducing-your-app-s-memory-use.md)
  Improve your app’s performance by analyzing memory-use metrics and making changes to maximize memory efficiency.
- [Improving your app’s performance](improving-your-app-s-performance.md)
  Model, measure, and boost the performance of your app by using a continuous-improvement cycle.
- [Profiling apps using Instruments](https://developer.apple.com/tutorials/instruments)
  Use Instruments to analyze the performance, resource usage, and behavior of your apps. Learn how to improve responsiveness, reduce memory usage, and analyze complex behavior over time.
- [Creating a performance plan for your visionOS app](../visionOS/creating-a-performance-plan-for-visionos-app.md)
  Identify your app’s performance and power goals and create a plan to measure and assess them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-the-performance-of-your-shipping-app)*