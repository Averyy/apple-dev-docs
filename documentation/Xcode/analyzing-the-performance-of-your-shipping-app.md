# Analyzing the performance of your shipping app

**Framework**: Xcode

View power and performance metrics for apps you distribute through the App Store.

#### Overview

Use the Xcode Organizer to view anonymized performance data from your app’s users, including launch times, memory usage, UI responsiveness, and impact on the battery. Use the data to tune the next version of your app and catch regressions that make it into a specific version of your app.

In Xcode, choose Window > Organizer to open the Organizer window, and then select the desired metric or report. In some cases, the pane shows “Insufficient usage data available” because there may not be enough anonymized data reported from participating user devices. When this happens, try checking back in a few days.

When Xcode has enough information to determine a goal for a metric, the chart includes the goal value. Use this information to plan and prioritize performance engineering work.

##### View Key Insights Into Your App

When you open Xcode Organizer, the Insights overview provides a unified view of the most actionable performance information for your app. It surfaces performance regressions, top and trending signatures, and the metrics most likely to need your attention, so you spend less time navigating between individual metric and diagnostic report pages.

![A screenshot of the Insights overview in Xcode Organizer, showing a Memory metric regression with a summary chart, metric recommendation, and links to relevant diagnostic pages.](https://docs-assets.developer.apple.com/published/1d229f9efaf07f55eda560520e4b4b23/analyzing-the-performance-of-your-shipping-app-insights-overview%402x.png)

The Insights overview highlights the highest-impact metrics for your app and displays information for each one. When Xcode detects a regression, it displays a regression chart that calls out the affected metric. When Xcode has enough data to compute a goal for a metric, it displays a recommendation chart for that metric regardless of whether a regression exists. A single metric can appear with a regression chart, a recommendation chart, or both. Even if your app has no regressions, the Insights overview will surface actionable recommendations you can act on. From there, you can follow links to the relevant diagnostic reports and metric pages for further investigation.

Select the Notifications button in the upper-right corner to opt in to power and performance regression notifications. Xcode sends you a notification for the latest version of each of your shipped apps when it detects a high-impact regression. A regression is considered high impact if performance data is available and indicates the latest version of your app regresses 75 percent or more compared to the average of the previous four app versions available in the App Store. Xcode notifies you once per 24-hour period when Xcode is running. To keep notifications to a minimum, Xcode sends you no more than one notification for the same app version. The Notifications button covers power and performance metric regressions only. It does not send notifications for diagnostic signatures listed in the Insights overview.

The first time you open Organizer, it opens to the Insights overview. On subsequent launches, Organizer restores the last section you visited.

##### Read Data for a Metric

The Xcode Organizer shows a title, description, and graph for each type of metric. In the graph, each bar represents a version of your app. Use the pop-up menus to filter the metric data for different devices and the median or high value. If your app has an App Clip available, use the pop-up menu to filter by app type and switch between viewing metrics for the main app and the App Clip.

![A screenshot of the Hang Rate metric pane in the Xcode Organizer. From left to right are the list of metrics and reports, the metric UI with a bar graph showing the hang rate for the past 16 app versions, and data for the latest app version.](https://docs-assets.developer.apple.com/published/031175a44e74fef7a78bb04842e56564/analyzing-the-performance-of-your-shipping-app-1%402x.png)

Metrics that show *limited usage* in the detail section include an associated margin of error because the existing data is limited. Use this margin of error to determine the upper and lower bounds of the displayed value. The margin of error decreases as data increases. The release date information in this section provides the date when the selected app version is ready for sale.

##### Compare Performance with a Previous App Release

To explore changes between versions for a metric, such as those for Hang Rate in the image below, click the vertical bar for your selected version.

The data for both the selected and latest versions appear to the right of the graph with the higher of the two values in bold. Change information for those versions appears in the details section below the latest version data.

![A screenshot of the comparison view in the Hang Rate metric pane of the Xcode Organizer. Key pieces are the highlighted selected version bar, data for the latest and selected app versions, and change information between those two versions.](https://docs-assets.developer.apple.com/published/e23db2c9e6cdf19aa4bc46c14885b6fc/analyzing-the-performance-of-your-shipping-app-2%402x.png)

##### Compare Your Apps Metrics with Goal Values

Xcode Organizer compares your app’s metrics against two types of goals: similar-app goals, which are based on metrics from apps with functional and technical similarities to yours, and historical performance goals, which are based on your app’s own historical data. If your app has sufficient metrics data available and the metric values for the current version of your app are greater than the goal values, Xcode displays a *goal* as a dashed line on the histogram in the Xcode Organizer.

For metrics that support them, similar-app goals serve as realistic and actionable targets that reflect your app’s true technical profile. For onscreen battery usage and disk writes, similar-app goals are normalized for usage time, ensuring a fair comparison across apps with different usage.

Historical performance goals use your app’s own past metric values as a baseline, helping you detect regressions and track improvements over time.

![A screenshot of the Launch Time metric pane in Xcode Organizer, showing previous app versions as blue bars and a dotted line indicating the similar-app performance goal.](https://docs-assets.developer.apple.com/published/bb10cdcfa2e8668561d62d4eb84aea8f/analyzing-the-performance-of-your-shipping-app-metric-goals%402x.png)

##### Improve Your Apps Performance

For more details about how to use the data in the Organizer panes to improve the performance of the next version of your app, see the topics below.

## See Also

- [Analyzing responsiveness issues in your shipping app](analyzing-responsiveness-issues-in-your-shipping-app.md)
  Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.
- [Analyzing your app’s battery use](analyzing-your-app-s-battery-use.md)
  Increase the available use time for your app on a single battery charge by reducing your appʼs power consumption.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Monitoring your app’s storage metrics](monitoring-your-app-s-storage-metrics.md)
  Track your app’s storage footprint over time using Xcode Organizer to catch regressions in Documents & Data and App Size.
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