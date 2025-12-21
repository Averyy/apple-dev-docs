# Shortcuts Actions Usage

**Framework**: Analytics Reports

Analyze how often people run shortcuts with your app’s actions.

#### Overview

The data in this report contains information about how often people run actions provided by your app. The report also indicates whether the action completes successfully.

- Territories: Worldwide
- Platforms: iOS, iPadOS.  For more information about iOS and iPadOS, see the Platforms section in [`Data Completeness and Corrections`](data-completeness-corrections.md).
- Availability: - Daily: Every day.
- History: On request, data is available beginning with iOS 17.4 and iPadOS 17.4.
- Completeness: Data from devices that contribute to this report can arrive as late as 8 days after the date it generates on device. You can download recent data daily, but it might be incomplete, and data updates incrementally daily, until all late-arriving events are available.
- Privacy: - Includes data from users who have opted to share their data with Apple and developers.
- Individual rows will only appear if they have a value of 5 or more.
- Data Context: You can analyze your data with additional context by comparing it with the data in the [`App Sessions Context`](app-sessions-context.md) report, which provides a count of unique devices that use your app on a specific day. For example, if your app performed an action detailed in this report on 10 unique devices on a specific day, and the App Sessions Context report shows there were 100 unique devices running your app that day, then you can approximate that 10% of the devices running your app performed that action.

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Count | Number of times the event occurred | `integer` |
| Territory | Country or region in which the event occurred | `string` |
| Date | Date when the event occurred | `string` |
| Platform | OS version on the device on which the event occurred | `string` |
| Device | Type of device on which the event occurred | `string` |
| Build | Build of device on which event occurred | `string` |
| Unique Devices | The count of unique devices | `integer` |
| Release Type | Type of software release | `string` |
| Success | Action completed running without error | `boolean` |
| Action Identifier | Identifier of the action that ran | `string` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Action Identifier | AddDocument | Add a document to your app. |

## See Also

- [App Clip Usage](app-clip-usage.md)
  Analyze how users engage with your App Clips.
- [App Crashes](app-crashes.md)
  Review crashes for your App Store apps based on app version and device type.
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
- [Shortcut App Usage](shortcut-app-usage.md)
  Analyze how often people use a shortcut action in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/shortcuts-actions-usage)*