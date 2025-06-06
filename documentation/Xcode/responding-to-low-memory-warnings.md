# Responding to low-memory warnings

**Framework**: Xcode

Detect when your app is using excessive memory, and bring memory use under control.

#### Overview

iOS sends your app a warning when its memory use approaches the limit of available device memory. The amount of memory use that triggers a memory warning corresponds to the yellow region in Xcode’s memory gauge. Your app can receive a memory warning in any of these ways:

- UIKit calls the [`applicationDidReceiveMemoryWarning(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidReceiveMemoryWarning(_:)) method of your app delegate.
- UIKit calls the [`didReceiveMemoryWarning()`](https://developer.apple.com/documentation/UIKit/UIViewController/didReceiveMemoryWarning()) method of active [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) objects.
- iOS posts [`didReceiveMemoryWarningNotification`](https://developer.apple.com/documentation/UIKit/UIApplication/didReceiveMemoryWarningNotification) to the default notification center.
- Dispatch queues receive an event with source type [`DISPATCH_SOURCE_TYPE_MEMORYPRESSURE`](https://developer.apple.com/documentation/Dispatch/DISPATCH_SOURCE_TYPE_MEMORYPRESSURE).

The operating system sends low-memory warnings using a best-effort approach, and your app needs to respond to them as quickly as possible. If memory demand on the system increases faster than the warnings relieve memory pressure, the system may not have time to send the low-memory warnings and wait for apps to respond. When this occurs, the system resorts to jettisoning apps to reclaim their memory and recording the reason in a log file, as described in [`Identifying high-memory use with jetsam event reports`](identifying-high-memory-use-with-jetsam-event-reports.md).

Make sure your app changes its approach for allocating memory when it receives a memory warning—adopting a conservative policy of looking for opportunities to release objects or reduce their size as it uses them. If your app allocates large amounts of memory at once and crashes before it receives the low-memory warning during the large allocation, modify your code to slowly allocate the necessary memory, so the system has adequate time to free memory from across the system.

If your app loads data it can easily recreate, consider using [`NSPurgeableData`](https://developer.apple.com/documentation/Foundation/NSPurgeableData). When the contents of [`NSPurgeableData`](https://developer.apple.com/documentation/Foundation/NSPurgeableData) aren’t marked as in-use through [`beginContentAccess()`](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/1412187-begincontentaccess), the system automatically discards the contents in low-memory situations. This automatic discard process helps your app react to a low-memory warnings more quickly, because the kernel handles discarding the data, rather than your app, which is waiting to receive the low-memory notification before discarding the data.

> ❗ **Important**: Don’t traverse your app’s whole object graph looking for memory to release when your app receives a memory warning, and avoid using [`NSCache`](https://developer.apple.com/documentation/Foundation/NSCache) in connection with [`NSPurgeableData`](https://developer.apple.com/documentation/Foundation/NSPurgeableData). iOS compresses memory pages that apps haven’t accessed recently. Searching for memory to purge brings these pages out of the compressor, and increases memory demands on the system.

Don’t traverse your app’s whole object graph looking for memory to release when your app receives a memory warning, and avoid using [`NSCache`](https://developer.apple.com/documentation/Foundation/NSCache) in connection with [`NSPurgeableData`](https://developer.apple.com/documentation/Foundation/NSPurgeableData). iOS compresses memory pages that apps haven’t accessed recently. Searching for memory to purge brings these pages out of the compressor, and increases memory demands on the system.

## See Also

- [Identifying high-memory use with jetsam event reports](identifying-high-memory-use-with-jetsam-event-reports.md)
  Discover why the operating system terminated your app when available memory was low.
- [Gathering information about memory use](gathering-information-about-memory-use.md)
  Identify memory-use inefficiencies by measuring and profiling your app.
- [Making changes to reduce memory use](making-changes-to-reduce-memory-use.md)
  Decrease your app’s use of memory by addressing common causes of excessive use.
- [Preventing memory-use regressions](preventing-memory-use-regressions.md)
  Measure the memory that your app’s features use, and detect increases by using XCTest performance tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/responding-to-low-memory-warnings)*