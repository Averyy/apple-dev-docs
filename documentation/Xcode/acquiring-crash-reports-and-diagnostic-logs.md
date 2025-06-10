# Acquiring crash reports and diagnostic logs

**Framework**: Xcode

Gather crash reports and device logs from the App Store, TestFlight, and directly from devices.

#### Overview

After your app is distributed to customers, learn ways to improve it by collecting crash reports and diagnostic logs. If a customer reports an issue with your app, use the Crashes organizer in Xcode to get a report about the issue, as described in [`How are reports created?`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev675635e70) If the Crashes organizer doesn’t contain the diagnostic information you need or is unavailable to you, the customer can collect logs from their device and share them directly with you to resolve the issue. Once you have a crash report, you may need to add identifiable symbol information to the crash report—see [`Adding identifiable symbol names to a crash report`](adding-identifiable-symbol-names-to-a-crash-report.md) for more information.

For issues that aren’t crashes, inspect the operating system’s console log to find important information for diagnosing the issue’s source.

##### Collect Crash Reports From Testflight and the App Store

TestFlight and the App Store collect crash reports for every submitted version of your app. Crash reports automatically contain identifiable symbol information if you include symbol information when submitting a build to the App Store. Review [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md) for the recommended settings.

Crash reports from customers who send diagnostic and usage information are presented in the Crashes organizer, as described in [`Share crash, energy, and metrics data with developers`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/deve2819c518). TestFlight users of your app automatically share crash reports with you, regardless of the device settings for sharing diagnostic and use data. If no crash reports appear in the Crashes organizer, see [`If no crash, energy, or metrics reports appear in the organizer`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev9a80ab71d) to enable collection of crash reports from your customers.

The following crash report types aren’t available through the Crashes organizer, but are available by other means. See [`Transfer crash reports and device logs to a Mac`](acquiring-crash-reports-and-diagnostic-logs#Transfer-crash-reports-and-device-logs-to-a-Mac.md) and [`Locate crash reports and memory logs on the device`](acquiring-crash-reports-and-diagnostic-logs#Locate-crash-reports-and-memory-logs-on-the-device.md).

- Watchdog events, such as those from slow app launch times
- Invalid code-signature crashes
- Thermal events, where a device overheats because an app uses too much CPU
- Jetsam events, where an app has high memory use

##### Transfer Crash Reports and Device Logs to a Mac

If you have access to the device on which your app crashes, you can transfer diagnostic logs by connecting the device to your Mac. You can view these logs using the Devices and Simulators window in Xcode, described in [`About Devices and Simulators window`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev7b20475ba).

If a customer reports a crash, they can transfer the crash report to either a Mac or Windows computer. See [`Find device crash and energy logs on a Mac or Windows computer`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev0f3181c2c).

##### Locate Crash Reports and Memory Logs on the Device

If a customer reports a crash in your app and you don’t have a crash report for it in the Crashes organizer, ask the customer to e-mail you the crash report from their device.

> **Note**: Crash reports from watchOS are available on the paired iPhone.

To locate and email crash reports for iOS, iPadOS, tvOS, visionOS, and watchOS apps:

1. Open the Analytics & Improvements section of Settings on the device. See [`Share analytics, diagnostics, and usage information with Apple`](https://developer.apple.comhttps://support.apple.com/en-us/HT202100).
2. Tap Analytics Data.
3. Locate the log for your app. The log name starts with `<AppBinaryName>_<DateTime>` for crash reports, or `JetsamEvent_<DateTime>` for high-memory use crashes.
4. Select the desired log.
5. Tap the Share icon, and select Mail to send the crash report as a mail attachment.

To locate and email crash reports for macOS and Mac Catalyst apps:

1. Open the Console app, from Applications > Utilities in Finder.
2. Select .
3. Locate crash reports for your app in the list. Logs are listed by your app’s binary name.
4. Right-click the desired log’s file name.
5. Select Reveal in Finder.
6. Drag the file displayed in Finder to Mail to send the crash report as a mail attachment.

##### Create a Crash Report While Debugging

If you encounter a crash while debugging your app using Xcode, the debugger intercepts the crash so you can inspect your app’s state. If you’d like to gather the full crash report for the issue, detach the debugger, either by using the Debug > Detach menu item in Xcode, or by issuing the `detach` command in the debugging console. This allows the app to finish crashing and lets the operating system generate the crash report. See [`Locate crash reports and memory logs on the device`](acquiring-crash-reports-and-diagnostic-logs#Locate-crash-reports-and-memory-logs-on-the-device.md) for how to collect the crash report file.

##### Access Device Console Logs

If a customer reports an issue in your app that isn’t a crash, look at the device’s console log for additional information about the issue.

To access a device’s console logs:

1. For iOS, iPadOS, tvOS, and visionOS issues, connect the device to your Mac. For watchOS issues, install the logging profile to the paired iPhone and then connect the iPhone to your Mac. See [`Profiles and Logs`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/?name=sysdiagnose&platform=watchos) to download the profile. For macOS issues, proceed to the next step.
2. On the Mac, open the Console app, from Applications > Utilities in Finder.
3. Select the device in the Console sidebar.
4. Reproduce the issue and note the exact time.
5. Look for logs that pertain to the issue from around the time you reproduced the issue.
6. Use information from the log as clues to further guide your investigation of the issue.

## See Also

- [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md)
  Replace hexadecimal addresses in a crash report with function names and line numbers that correspond to your app’s code.
- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)
  Find patterns in crash reports that identify common problems, and investigate the issue based on the pattern.
- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Identifying high-memory use with jetsam event reports](identifying-high-memory-use-with-jetsam-event-reports.md)
  Discover why the operating system terminated your app when available memory was low.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs)*