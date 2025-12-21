# Scheduling CPU work efficiently

**Framework**: Xcode

Use concurrent programming and adjust the prioritization of background activities to improve the performance of your app.

#### Overview

Reduce the total computation your app does by adopting these strategies:

- Choose an efficient algorithm.
- Cache frequently used results in memory, instead of recalculating them each time your app needs to use the results.
- Reuse structures and objects to avoid the overhead of releasing and reallocating instances.
- Prefer an event-driven design, in which your app’s code receives notifications when it needs to perform work, instead of polling for available tasks.
- Use high-level system frameworks to achieve your app’s goals, because these are optimized to reduce power overhead. For example, use [`Core ML`](https://developer.apple.com/documentation/CoreML) to work with machine learning models, and [`Core Video`](https://developer.apple.com/documentation/CoreVideo) to perform video processing.

Additionally, reduce the amount of energy your app uses to perform calculations on the CPU by avoiding CPU bottlenecks, which reduce the CPU’s efficiency. For more information, see [`Addressing CPU bottlenecks`](addressing-cpu-bottlenecks.md).

##### Adopt Concurrent Programming

Use concurrent programming techniques, such as [`Swift Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) or [`Dispatch`](https://developer.apple.com/documentation/Dispatch), to efficiently schedule work on multiple CPU cores. Adopting concurrent programming also helps to avoid hangs and hitches in your app by moving processing work to background threads. For more information, see [`Improving app responsiveness`](improving-app-responsiveness.md).

Identify a granularity for concurrent operations that balances creating multiple operations that the CPU can schedule on multiple cores, with performing enough work in each operation to avoid creating too much overhead in managing the operations. Ideally, each independent operation requires between 10-100 ms to complete.

Set the [`DispatchQoS`](https://developer.apple.com/documentation/Dispatch/DispatchQoS) (quality-of-service, or QoS) level for concurrent operations, to ensure that the system schedules UI-related tasks responsively and uses efficient strategies to complete background operations. In general, use the lowest QoS value that makes sense for your task, because the system uses more energy-efficient scheduling for tasks with lower QoS. For more information on setting QoS for operations, see [`Tuning your code’s performance for Apple silicon`](https://developer.apple.com/documentation/Apple-Silicon/tuning-your-code-s-performance-for-apple-silicon).

The Thread Performance Checker in Xcode reports runtime issues if you create dependencies from high-QoS operations on low-QoS operations. For more information on using the Thread Performance Checker, see [`Diagnosing performance issues early`](diagnosing-performance-issues-early.md).

##### Schedule Work in the Background

Use [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks) to perform work in the background. The system optimizes the schedule for background tasks — for example by batching tasks together or by running the tasks when the device is charging. For more information, see [`Choosing Background Strategies for Your App`](https://developer.apple.com/documentation/BackgroundTasks/choosing-background-strategies-for-your-app).

##### Prioritize Live Activities Appropriately

Whenever you send a push notification that contains an update to your app’s Live Activity that doesn’t require immediate attention from someone, set the value for the `apns-priority` HTTP header to `5`, which indicates to the Apple Push Notification service (APNs) server that it can deliver the push notification in an energy-efficient way. Notifications with `apns-priority` set to `5` don’t count toward your app’s budget for Live Activity updates, so setting the value to `5` helps reduce the likelihood that your app exceeds its budget. If the app does exceed its budget, the system reduces the rate at which it delivers your notifications. For more information, see [`Starting and updating Live Activities with ActivityKit push notifications`](https://developer.apple.com/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency).

## See Also

- [Responding to power notifications](responding-to-power-notifications.md)
  Adopt more power-efficient strategies to prolong the device’s battery life.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/scheduling-cpu-work-efficiently)*