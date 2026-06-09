# Addressing CPU bottlenecks

**Framework**: Xcode

Locate and fix pipeline stalls, cache misses, and other performance issues.

#### Overview

To keep a device’s CPU running at its highest effectiveness while it’s processing your app, tune your app to best use the CPU instruction set and ensure that the CPU microarchitecture delivers and processes instructions efficiently. Modern processors have multiple facilities to improve the flow of instructions they process, including:

- **Pipelining**: The processor runs distinct parts of different instructions in parallel; for example, it can decode one instruction while it performs the operations requested by another instruction.
- **Out-of-order execution**: Logic that detects upcoming instructions that don’t depend on the results of instructions that appear earlier in the code, and runs those independent instructions in parallel.
- **Speculative execution**: Logic that attempts to guess whether the program counter will follow a conditional jump instruction, and directs the processor to speculatively run the subsequent instructions.
- **Superscalar architecture**: The processor contains parallel components that perform the same step on multiple instructions in parallel; for example, fetching data for multiple instructions concurrently.
- **Memory caches**: Replicated memory located on the system-on-a-chip that hold instructions and data to make repeated access to the same locations in main memory, or predictable access patterns, faster. These areas are arranged in a hierarchy, with faster but smaller storage located nearby each CPU.

In situations where your app’s design, or the hints you provide to the compiler, don’t let the CPU take advantage of these features, the CPU can encounter a *bottleneck* where it can’t run at its maximum efficiency. Examples of CPU bottlenecks include situations that cause the CPU to wait because the next instruction it needs to process isn’t available yet, or where processing an instruction *stalls* because the CPU is waiting for a relatively slow access to memory. CPU bottlenecks reduce the rate at which the processor can finish your app’s work, increasing the time someone waits for your app to complete a task. Bottlenecks that occur on your app’s main thread contribute to freezes and hitches in your app’s UI.

Additionally, using the CPU inefficiently increases the power used by the CPU when it runs your app. For information on measuring your app’s power use, see [`Measuring your app’s power use with Power Profiler`](measuring-your-app-s-power-use-with-power-profiler.md).

Use coding strategies that avoid CPU bottlenecks. Identify areas in your app that need performance improvement, set performance targets, and write performance tests to validate that your changes improve performance. Use Instruments to detect situations where the CPU encounters a bottleneck while it runs your app’s code. Take steps to remove the bottlenecks, and improve your app’s performance.

> **Note**:  Remove other sources of processor overhead, including inefficient algorithms and redundant memory management code, before you investigate CPU bottlenecks. For more information, see [`Analyzing CPU usage with the Processor Trace instrument`](analyzing-cpu-usage-with-processor-trace.md).

##### Design Your App to Avoid Cpu Bottlenecks

The following design principles help the system to optimize CPU performance when someone uses your app.

Use system frameworks. Where the system provides a framework to perform a task, that framework’s implementation is optimized to use device resources efficiently.

Prefer dynamic task allocation to static thread pools. The system assigns your app’s threads to run on different cores in the processor, which can complete work at different rates depending on the type of core and the other work running on the device. Work assigned to threads in a static pool can finish at different times, leaving some threads without work to do while other threads catch up.

Consider using [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks) to create tasks that the system schedules dynamically, based on resource availability.

Indicate quality-of-service for background tasks. The system uses quality-of-service information to dynamically schedule tasks and make efficient use of available processing resources.

If you use Background Tasks, pick the correct task type for the work you assign to the task. For more information, see [`Choosing Background Strategies for Your App`](https://developer.apple.com/documentation/BackgroundTasks/choosing-background-strategies-for-your-app). If you use Grand Central Dispatch, dispatch your work to a queue with the appropriate [`DispatchQoS`](https://developer.apple.com/documentation/Dispatch/DispatchQoS).

For more guidance on optimizing your code for Apple silicon, see [`Tuning your code’s performance for Apple silicon`](https://developer.apple.com/documentation/Apple-Silicon/tuning-your-code-s-performance-for-apple-silicon).

##### Establish Performance Goals

Use information from the Metrics Organizer, and feedback from people who test and use your app, to identify performance issues and define targets for improvement. For more information, see [`Improving your app’s performance`](improving-your-app-s-performance.md).

##### Write Performance Tests

When you identify features that need performance improvements, create performance tests to automatically exercise those features and measure their performance. Set a performance baseline and run the tests when you make code changes, to compare your app’s performance with the baseline and detect regressions.

Use [`XCTCPUMetric`](https://developer.apple.com/documentation/XCTest/XCTCPUMetric) to measure CPU activity in your tests, and [`XCTClockMetric`](https://developer.apple.com/documentation/XCTest/XCTClockMetric) to measure time elapsed during your tests. For more information, see [`Writing and running performance tests`](writing-and-running-performance-tests.md).

##### Detect Cpu Bottlenecks

When your performance tests reveal that your app doesn’t meet your performance goals, use the CPU Counters instrument to identify situations where the system encounters CPU bottlenecks when it runs your app.

Record your app’s CPU access patterns by following these steps:

1. In Xcode, Control-click the test indicator next to the test that demonstrates the performance problem, and choose Profile *the test’s name*.
2. In Instruments the Choose a Template… window opens, choose the CPU Counters template.
3. Set the CPU Counters instrument mode to CPU Bottlenecks.
4. Click record to start gathering data.

If you don’t have a performance test for the features you want to analyze, follow these steps instead:

1. In Xcode, choose Product > Profile.
2. In Instruments the Choose a Template… window opens, choose the CPU Counters template.
3. Choose the target device and app to record.
4. Set the CPU Counters instrument mode to CPU Bottlenecks.
5. Click record to start gathering data.
6. Interact with the features in your app that you want to analyze.
7. In Instruments, click the Stop button to stop gathering data.

##### Discover Code That Causes Cpu Bottlenecks

The CPU Counters instrument adds mode-specific lanes to the CPU Counters, process, and thread tracks you use to analyze the processor’s workload. In the initial CPU bottlenecks mode, the lane divides the maximum sustainable CPU bandwidth into four categories:

- **Useful**: The CPU doesn’t encounter bottlenecks and completes instructions that contribute to making progress in your app’s code.
- **Instruction Delivery Bottleneck**: The CPU encounters a bottleneck because it fetches instructions at a slower rate than it completes them; for example, the processor needs to follow a large number of jump instructions to locate the instructions it needs to fetch.
- **Instruction Processing Bottleneck**: The CPU encounters a bottleneck because it completes instructions at a slower rate than it fetches them; for example, many instructions require the processor to load data from memory and take a long time to complete.
- **Discarded Bottleneck**: The CPU encounters a bottleneck because it is busy with instructions that don’t contribute to making progress in your app’s code; for example, the CPU makes incorrect branch predictions and completes instructions only to discard the results.

![A screenshot of Instruments, showing the CPU bandwidth categorized into useful bandwidth and bottlenecks in the CPU Counters lane.](https://docs-assets.developer.apple.com/published/772f4222ceee7b4ea6c21dc5d33da3ef/cpu-bottlenecks-counter-instrument%402x.png)

While the presence of CPU bottlenecks indicates opportunities to improve your app’s performance, the absence of bottlenecks doesn’t necessarily mean your code is as efficient as possible. For example, there might be a more efficient algorithm available to implement your app’s features, or your app might encounter other overhead that doesn’t result in CPU bottlenecks.

Use the Time Profiler track, and the tracks for your app’s threads, to correlate the presence of CPU bottlenecks with the code that runs in your app. Additionally, record another trace in Instruments using a sampling mode, which examines specific instructions that can frequently result in CPU bottlenecks.

Click the CPU Counters track to see the Summary: Metrics view, which shows the fraction of time the CPU spends doing useful work or encountering bottlenecks. Select a range in the timeline to focus the Summary: Metrics view on that range.

##### Identify Causes of Cpu Bottlenecks

When you locate the code in your app that causes CPU bottlenecks and the category of bottleneck the processor encounters, gather more detailed information to determine the specific situations that lead to CPU bottlenecks, and plan to address those bottlenecks in code.

> 💡 **Tip**:  Use [`OSSignposter`](https://developer.apple.com/documentation/os/OSSignposter) to add signposts to the code that causes CPU bottlenecks, so that it’s easier to identify the relevant region in the timeline in your subsequent analysis work.

Follow these steps in Instruments:

1. Expand the thread timeline for your app’s threads to reveal lanes that indicate when your app encountered bottlenecks.
2. Click on a bottleneck in the thread timeline to scroll the detail view to that bottleneck.
3. Control-click the bottleneck in the detail view and choose “Suggested Next” to start a new recording in Instruments that changes the CPU Counters instrument mode to gather more information about that bottleneck.
4. If you aren’t profiling a performance test, interact with the feature in your app that caused the bottleneck in the first recording, then click the Stop button to stop gathering data.

The CPU Counters track and Summary: Metrics view show the fraction of particular categories of CPU bottlenecks that the processor encounters. Switch to the Remarks view to see information about bottleneck events that Instruments detected. Click a metric or remark in the detail view to read more information about the cause of that type of CPU bottleneck, and suggested code strategies to mitigate the bottleneck.

![A screenshot of Instruments. A CPU bottleneck is highlighted in the Remarks view, and Instruments suggests how to mitigate the bottleneck.](https://docs-assets.developer.apple.com/published/43f398a7c11ab4d2db02ac470878f777/cpu-bottlenecks-remarks-view%402x.png)

Refer to the [`Apple Silicon CPU Optimization Guide Version 4`](https://developer.apple.com/documentation/Apple-Silicon/cpu-optimization-guide) for more information on Apple silicon and guidance on optimizing your code.

After you make a code change, re-run your performance tests, and use the CPU Counters instrument again to validate that your change improves your app’s processor usage.

## See Also

- [Analyzing CPU usage with the Processor Trace instrument](analyzing-cpu-usage-with-processor-trace.md)
  Identify code where your app uses the CPU inefficiently.
- [Analyzing CPU profiles with call tree views](analyzing-cpu-profiles-with-call-tree-views.md)
  Use call tree visualizations to find performance bottlenecks in Instruments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/addressing-cpu-bottlenecks)*