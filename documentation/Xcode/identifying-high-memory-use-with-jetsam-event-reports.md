# Identifying high-memory use with jetsam event reports

**Framework**: Xcode

Discover why the operating system terminated your app when available memory was low.

#### Overview

iOS, iPadOS, tvOS, visionOS, and watchOS have a virtual memory system that relies on all apps releasing memory when the operating system encounters , where available memory is low and the system can’t meet the demands of all running apps. Under memory pressure, apps free memory after receiving a low-memory notification. If all running apps release enough total memory to alleviate memory pressure, your app will continue to run. But, if memory pressure continues because apps haven’t relinquished enough memory, the system frees memory by terminating applications to reclaim their memory. This is a , and the system creates a jetsam event report with information about why it chose to jettison an app.

Jetsam event reports differ from crash reports because they contain the overall memory use of all apps and system processes on a device, they’re in JSON format, and they don’t contain the backtraces of any threads in your app. If the system jettisons your app due to memory pressure while the app is visible, it will look like your app crashed. Use jetsam event reports to identify your app’s role in jetsam events, even if your app didn’t get jettisoned.

##### Identify the Memory Page Size and Largest Process

The jetsam event report records how much memory each process used before jettisoning an app. The virtual memory system allocates and manages memory in chunks, called , and the report lists the memory use as the number of memory pages used. To convert the number of memory pages into the bytes of memory your app used, you need to know the , which is the number of bytes in one memory page.

The `pageSize` field in the jetsam event report header records the number of bytes in each memory page. In addition to the page size, the header of a jetsam report describes the overall device environment, such as the operating system version and hardware model. In this example, the page size is 16,384 bytes, or 16 KB.

```other
"crashReporterKey" : "b9aa251a63bd9e743afbb906f43eb7ea5f206292",
"product" : "iPad8,2",
"incident" : "32B05E3C-CB45-40F8-BA66-5668779740E1",
"date" : "2019-10-10 23:30:39.48 -0700",
"build" : "iPhone OS 13.1.2 (17A860)",
"memoryStatus" : {
   "pageSize" : 16384,
},
"largestProcess" : "OneCoolApp",

```

> **Note**: This example shows the header fields needed to diagnose a crash from a jetsam event report. The complete header information contains more fields than shown in this example.

This example shows the header fields needed to diagnose a crash from a jetsam event report. The complete header information contains more fields than shown in this example.

While inspecting the header, examine the `largestProcess` field—this field names the process using the highest number of memory pages on the system. If other apps in addition to yours are regularly jettisoned, and your app is the largest process, you should reduce your memory use to better cooperate with other apps’ memory needs.

##### Identify the Jetsam Reason

A jetsam event report contains a `processes` array, with each item in the array describing a single process in the system. Search for the `reason` key to identify the jettisoned process and why the system jettisoned it. Only the jettisoned process has the reason key.

> ❗ **Important**: If your app crashed, but the jettisoned process isn’t your app, then the crash isn’t due to memory pressure. To diagnose your app’s issue, see [`Acquiring crash reports and diagnostic logs`](acquiring-crash-reports-and-diagnostic-logs.md) to locate its crash report.

If your app crashed, but the jettisoned process isn’t your app, then the crash isn’t due to memory pressure. To diagnose your app’s issue, see [`Acquiring crash reports and diagnostic logs`](acquiring-crash-reports-and-diagnostic-logs.md) to locate its crash report.

This example is one process entry in the `processes` array:

```other
{
    "uuid" : "a02fb850-9725-4051-817a-8a5dc0950872",
    "states" : [
      "frontmost"
    ],
    "lifetimeMax" : 92802,
    "purgeable" : 0,
    "coalition" : 68,
    "rpages" : 92802,
    "reason" : "per-process-limit",
    "name" : "MyCoolApp"
}
```

> **Note**: This example shows the process fields needed for diagnosing a crash from a jetsam event report. The complete process information in a report contains more fields than shown in this example.

This example shows the process fields needed for diagnosing a crash from a jetsam event report. The complete process information in a report contains more fields than shown in this example.

If the jettisoned process is your app, the value of the `reason` key explains the conditions that led to the jetsam event:

- `per-process-limit`: The process crossed the resident memory limit imposed by the system on all apps. Crossing this limit makes the process eligible for termination. If the process is an app extension from your app, note that extensions have a much lower per-process memory limit than foreground apps. Carefully consider your needs before using technologies with a high-baseline memory cost, such as [`SpriteKit`](https://developer.apple.com/documentation/SpriteKit) or a [`MKMapView`](https://developer.apple.com/documentation/MapKit/MKMapView), in an extension point. Alternate solutions may be more appropriate. For example, an image created by [`MKMapSnapshotter`](https://developer.apple.com/documentation/MapKit/MKMapSnapshotter) has lower memory use than a [`MKMapView`](https://developer.apple.com/documentation/MapKit/MKMapView), and is a better choice for many extension-point scenarios.
- `vm-pageshortage`: The system experienced memory pressure and needed to free background process memory for the current foreground app.
- `vnode-limit`: Too many files were open across the system. The kernel has a finite number of , a memory structure backing open files, and these were almost exhausted. To avoid terminating the frontmost app when vnodes are nearly exhausted, the system may terminate your app in the background to free vnodes, even if your app isn’t the source of excess vnode use.
- `highwater`: A system daemon exceeded its highest-expected memory footprint.
- `fc-thrashing`: A process thrashed the system file cache. This occurs when non-sequential parts of memory-mapped files are read and written too frequently. To avoid terminating the frontmost app, the system may terminate your app in the background to free space in the file cache, even if your app isn’t thrashing the file cache.
- `jettisoned`: The system jettisoned the process for some other reason.

To determine the amount of memory your app is using, multiply the number of memory pages reported in the `rpages` field by the page size value from the `pageSize` field in the jetsam event report’s header. The result is the amount of memory your app is using in bytes. For example, a process with a `rpages` value of 92,802 multiplied by a `pageSize` value of 16,384 bytes is using 1,520,467,968 bytes (1.52 GB) of memory.

Each item in the `processes` array also has the following keys, which provide additional information for diagnosing the issue.

- `uuid`: The build UUID of the binary. This helps you identify the version of your app by comparing this value to the available dSYM files for builds distributed to customers. To learn more about the build UUID, see [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md).
- `states`: Describes the app’s current memory use state, such as using memory as the `frontmost` app, or `suspended` and not actively using memory.
- `lifetimeMax`: The highest number of memory pages allocated during the lifetime of the process.
- `coalition`: If your app’s process is part of a coalition that involves other system processes doing work on behalf of your app, use this information to identify related processes and their memory use, as your app can influence the memory use of other coalition processes.
- `name`: The process name. See if this name matches a binary from your app, or belongs to another app or system process.

##### Make Changes to Your Apps Memory Use

Once you confirm that your app is crashing due to high-memory use, by analyzing the jetsam event report, see [`Gathering information about memory use`](gathering-information-about-memory-use.md) to understand your app’s memory use patterns, and [`Making changes to reduce memory use`](making-changes-to-reduce-memory-use.md) for techniques to lower your memory use.

In addition to lowering your app’s memory use, ensure you are receiving the low-memory warnings sent by the system and acting on these warnings to cooperate with the needs of the operating system and lower your appʼs memory use—see [`Responding to low-memory warnings`](responding-to-low-memory-warnings.md) for the specific ways the system notifies your app.

## See Also

- [Reducing your app’s memory use](reducing-your-app-s-memory-use.md)
  Improve your app’s performance by analyzing memory-use metrics and making changes to maximize memory efficiency.
- [Logging](../os/logging.md)
  Capture telemetry from your app for debugging and performance analysis using the unified logging system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/identifying-high-memory-use-with-jetsam-event-reports)*