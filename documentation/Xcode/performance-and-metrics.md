# Performance and metrics

**Framework**: Xcode

Measure, investigate, and address the use of system resources and issues impacting performance using Instruments and Xcode Organizer.

## Topics

### Essentials
- [Improving your app’s performance](improving-your-app-s-performance.md)
  Model, measure, and boost the performance of your app by using a continuous-improvement cycle.
- [Profiling apps using Instruments](https://developer.apple.com/tutorials/instruments)
  Use Instruments to analyze the performance, resource usage, and behavior of your apps. Learn how to improve responsiveness, reduce memory usage, and analyze complex behavior over time.
- [Analyzing the performance of your shipping app](analyzing-the-performance-of-your-shipping-app.md)
  View power and performance metrics for apps you distribute through the App Store.
- [Creating a performance plan for your visionOS app](../visionOS/creating-a-performance-plan-for-visionos-app.md)
  Identify your app’s performance and power goals and create a plan to measure and assess them.
### Responsiveness
- [Analyzing responsiveness issues in your shipping app](analyzing-responsiveness-issues-in-your-shipping-app.md)
  Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Understanding user interface responsiveness](understanding-user-interface-responsiveness.md)
  Make your app more responsive by examining the event-handling and rendering loop.
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
### Processor usage
- [Analyzing CPU usage with the Processor Trace instrument](analyzing-cpu-usage-with-processor-trace.md)
  Identify code where your app uses the CPU inefficiently.
### Memory and size
- [Reducing your app’s memory use](reducing-your-app-s-memory-use.md)
  Improve your app’s performance by analyzing memory-use metrics and making changes to maximize memory efficiency.
- [Reducing your app’s size](reducing-your-app-s-size.md)
  Measure your app’s size, optimize its assets and settings, and adopt technologies that help streamline installation over a mobile internet connection.
### Graphics
- [Analyzing the performance of your Metal app](analyzing-the-performance-of-your-metal-app.md)
  Ensure consistent, smooth rendering by profiling your app’s frame time.
- [Analyzing the memory usage of your Metal app](analyzing-the-memory-usage-of-your-metal-app.md)
  Keep your app alive in the background by managing its memory footprint.
### Power
- [Analyzing your app’s battery use](analyzing-your-app-s-battery-use.md)
  Increase the available use time for your app on a single battery charge by reducing your appʼs power consumption.
### Network
- [Analyzing HTTP traffic with Instruments](../Foundation/analyzing-http-traffic-with-instruments.md)
  Measure HTTP-based network performance and usage of your apps.
### Custom instruments
- [Creating custom modelers for intelligent instruments](creating-custom-modelers-for-intelligent-instruments.md)
  Create Custom Modelers with the CLIPS language and learn how the embedded rules engine works.

## See Also

- [Devices and Simulator](devices-and-simulator.md)
  Configure and manage devices connected to your Mac or devices in Simulator and use them to run your app.
- [Debugging](debugging.md)
  Identify and address issues in your app using the Xcode debugger, Xcode Organizer, Metal debugger, and Instruments.
- [Testing](testing.md)
  Develop and run tests to detect logic failures, UI problems, and performance regressions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/performance-and-metrics)*