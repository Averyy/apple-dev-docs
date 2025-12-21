# App Crashes

**Framework**: Analytics Reports

Review crashes for your App Store apps based on app version and device type.

#### Overview

Use this report to understand crashes for your App Store apps by app version and device type.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day
- Weekly: Every Friday for the previous week (Monday to Sunday).
- Monthly: On the fifth day of the following month.
- Completeness: Within five days. Weekly and monthly reports are complete by default.
- History: On request, data is available beginning from January 1, 2024.
- Privacy: - Includes app crashes data from users who have opted to share their data with Apple and developers. Data is provided only when events exist from at least five users for the respective report.

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` |
| App Name | The name of the app provided  by you during app setup in App Store Connect. | `string` |
| App Apple Identifier | Your app’s Apple ID. | `integer` |
| App Version | The version of the app associated with the crash. | `string` |
| Device | The device on which the event occurred. | `string` |
| Platform Version | The OS version of the device on which the event occurred. | `string` |
| Crashes | The total number of crashes. | `integer` |
| Unique Devices | Number of unique devices  where app crashed | `integer` |

## See Also

- [App Clip Usage](app-clip-usage.md)
  Analyze how users engage with your App Clips.
- [App Store Installations and Deletions](app-installs.md)
  Analyze details on the number of times users install and delete your apps.
- [App Store Opt-in](app-store-opt-in.md)
  Analyze the percentage of first-time app downloaders who choose to share their data with you.
- [App Sessions](app-sessions.md)
  Analyze how often people open your App Store apps, and the average session duration.
- [CarPlay App Usage](carplay-app-usage.md)
  Review how people use CarPlay in your app.
- [Platform App Installs](platform-app-installs.md)
  Analyze your app’s install data by date, install type, channel, device, platform version, and territory.
- [Shortcuts Actions Usage](shortcuts-actions-usage.md)
  Analyze how often people run shortcuts with your app’s actions.
- [Shortcut App Usage](shortcut-app-usage.md)
  Analyze how often people use a shortcut action in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-crashes)*