# Measuring your app’s power use with Power Profiler

**Framework**: Xcode

Profile your app’s power impact whether or not your device is connected to Xcode.

#### Overview

Various subsystems of a device require the device to draw additional power from its battery when your app uses them. Using these subsystems efficiently can reduce your app’s power demand, increasing the time before someone needs to recharge the battery and improving their experience of using your app. For more information, see [`Analyzing your app’s battery use`](analyzing-your-app-s-battery-use.md).

Use Power Profiler in Instruments to gather and analyze data on your app’s use of device subsystems that increase power consumption. Alternatively, record a performance trace using Power Profiler on your device while you’re away from your desk, and visualize the data in Instruments.

Create a plan to adopt power-efficient designs and API best practice to reduce your app’s power consumption, based on what you find in your analysis. Compare the trace data before and after you make changes to verify that the changes reduce your app’s power consumption.

##### Record and Analyze a Power Trace Using Instruments

Make sure your device is available in Xcode, either wirelessly or using a cable, and set the Run Destination in Xcode to the device you want to use. For more information, see [`Running your app in Simulator or on a device`](running-your-app-in-simulator-or-on-a-device.md). Record a power trace by following these steps:

1. In Xcode, choose Product > Profile.
2. In Instruments the Choose a Template… window opens, choose the Blank template.
3. Click the Add Instrument button, and choose the Power Profiler instrument.
4. Choose the target device and app to record. If you choose All Processes, Instruments only records a power trace for the overall system, and doesn’t report power metrics for your app.
5. Click record to start gathering data.
6. Interact with the features in your app that you want to analyze.
7. In Instruments, click the Stop button to stop gathering data.

The Power Profiler track in Instruments shows the overall system power usage, represented as a fraction of total battery energy consumed per hour. Additionally, it shows the following information:

- Whether the device is connected to a charger
- The device’s thermal state
- The display brightness
- Periods when Apple silicon is asleep

> **Note**:  When the device is charging, either via a cable or MagSafe, Instruments reports the overall system power usage as `0`. To record overall system power usage, pair your device to Xcode and use wireless debugging.

Click the disclosure triangle to the left of the track to expand the Power Profiler track. The Power Profiler shows a track for the app or extension you target. The track includes lanes that show the power impact that the process causes due to its use of CPU, GPU, display, and networking.

Higher values for power impact metrics represent greater power use. You can compare the power impact metrics with each other in the timeline, for example, to see whether your app causes greater power impact due to its networking use than its CPU use, and prioritize subsystems for further investigation. You can compare power impact metrics over time, including for multiple traces on the same device.

> ❗ **Important**:  The power impact metric values are different for different device models, so you can’t compare values for power impact metrics recorded on different models of device.

Click the disclosure triangle next to your app’s track to reveal lanes that provide more detailed information about your app’s usage of device subsystems.

##### Gather Power Consumption Data on a Device

Some scenarios are difficult to replicate on a device that’s connected to your Mac, for example, low-battery situations, and using your app with CarPlay. In these cases, collect a performance trace on the device, and transfer it to your Mac later to analyze in Instruments. People testing your app can also collect performance traces as they use your app, and share the trace files with you.

To set up a device to gather a performance trace that contains power metrics:

1. Follow the steps in [`Enabling Developer Mode on a device`](enabling-developer-mode-on-a-device.md) to turn on Developer Mode.
2. Open Settings, and navigate to Developer > Performance Trace.
3. Turn on Performance Trace, and follow any on-device prompts.
4. Change the tracing mode to Power Profiler.
5. Tap the switch next to your app’s name in the list of monitored apps to turn on tracing for your app. If you don’t turn on tracing for any apps, Performance Trace only records overall system power metrics.
6. Swipe down from the top-right of the screen to open Control Center.
7. Tap the Add (+) button.
8. Tap Add a Control.
9. Choose the Performance Trace control.

To gather a power trace:

1. Open Control Center.
2. Tap the Performance Trace control.
3. Interact with your app. Performance Trace gathers data for up to 10 hours.
4. Tap the Performance Trace control again in Control Center to stop gathering performance data.

To send the power trace to your Mac or another developer:

1. Open Settings.
2. Navigate to Developer > Performance Trace.
3. Tap the Share button next to the trace file in the list of available trace files.
4. Share the trace file with another developer, or use AirDrop to send it to your Mac.

In Finder, double-click the `*.aar` file you receive to expand it into a `*.atrc` file that you can open in Instruments.

##### Make Changes to Reduce Power Usage

Combine the information from Power Profiler with data you gather using other tools to identify how your app’s features use power, and plan your performance-engineering work.

If your app uses a lot of CPU power, combine Power Profiler with the Time Profiler or Processor Trace instruments to correlate the high power usage with the code your app runs and identify functions to make more efficient. For more information, see [`Analyzing CPU usage with the Processor Trace instrument`](analyzing-cpu-usage-with-processor-trace.md).

If your app uses a lot of GPU power, use the Metal debugger to identify opportunities to make your app’s GPU usage more efficient. For more information, see [`Optimizing GPU performance`](optimizing-gpu-performance.md).

If your app uses a lot of display power, consider adapting your app’s UI to reduce its average pixel luminance. For example, make sure your app supports Dark Mode. For more information, see [`Supporting Dark Mode in your interface`](https://developer.apple.com/documentation/UIKit/supporting-dark-mode-in-your-interface).

If your app uses a lot of networking power, combine Power Profiler with the Network Connections and HTTP Traffic instruments to correlate the high power usage with the network requests your app makes, and identify strategies to reduce the frequency of network connections or the amount of data the app transfers. For more information, see [`Analyzing HTTP traffic with Instruments`](https://developer.apple.com/documentation/Foundation/analyzing-http-traffic-with-instruments).

After you make a change, use Power Profiler again to validate that your change improves your app’s power usage. Consider capturing multiple recordings before and after the change, as the device’s state and other external factors can affect the specific values recorded for each metric.

## See Also

- [Analyzing your app’s battery use](analyzing-your-app-s-battery-use.md)
  Increase the available use time for your app on a single battery charge by reducing your appʼs power consumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/measuring-your-app-s-power-use-with-power-profiler)*