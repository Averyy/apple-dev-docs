# Reducing your app’s disk usage

**Framework**: Xcode  
**Role**: Article

Measure and minimize the space your app uses to store its files.

#### Overview

People use multiple apps on a device, to create and access important content. Minimize your app’s disk usage to make more space for a person’s content, and to allow someone to install more apps on their device. Store recoverable data in purgeable locations, so that the system can free up space when it needs to.

##### Review your app’s disk usage

To see the storage used by each app on your device, open Settings and choose General > Storage.

![A screenshot of Settings on iPhone, showing the storage used by each app on the device.](https://developer.apple.com/tutorials/images/com.apple.Xcode/iphone-storage-settings@2x.png)

Tap on your app to see a breakdown of how the app’s bundle, documents, and data contribute to the overall disk usage.

##### Gather metrics on disk usage

Use [MetricKit](../MetricKit/MetricKit.md) to gather metrics on the number of files in your app’s container and the disk space they occupy. Observe the `metricReports` asynchronous sequence and read the file count and size values from the daily report:

```swift
import MetricKit

let manager = MetricManager()

for await report in manager.metricReports {
    let entry = report.intervalEntries.fullDayEntry
    for value in entry.values {
        switch value {
        case let .totalFileSize(metric):
            // Analyze your app's disk usage.
            break
        case let .totalFileCount(metric):
            // Track the number of files in your app's container.
            break
        @unknown default:
            break
        }
    }
}
```

##### Use purgeable folders for recoverable content

When you download or otherwise generate content that your app can recover if it needs to, store that content in the [`cachesDirectory`](../Foundation/url/cachesdirectory.md) or the [`temporaryDirectory`](../Foundation/filemanager/temporarydirectory.md). The system automatically deletes content in the `cachesDirectory` and `temporaryDirectory` — an operation known as *purging* — when it detects that disk space is low.

```swift
let cacheDownloadTask = URLSession.shared.downloadTask(with: cacheURL) {
    fileURL, response, error

    // Check for download errors and handle them.

    guard let temporaryURL = fileURL else { return }
    do {
        let destinationURL = URL.cachesDirectory.appendingPathComponent(temporaryURL.lastPathComponent)
        try FileManager.default.moveItem(at: temporaryURL, to: destinationURL)
    }
    catch {
        // Handle the error.
    }
}
```

##### Manage local copies of iCloud files

When a person isn’t using the local copy of a file that’s stored in iCloud, call [`evictUbiquitousItem(at:)`](../Foundation/filemanager/evictubiquitousitem%28at%29.md) to remove the local copy while keeping the original on iCloud:

```swift
func removeLocalDocument(at localURL: URL) throws {
    let resources = try localURL.resourceValues(forKeys: [.ubiquitousItemIsUploadedKey])
    guard resources.ubiquitousItemIsUploaded == true else { return }
    FileManager.default.evictUbiquitousItem(at: localURL)
}
```

You can subsequently retrieve the file from iCloud by calling [`startDownloadingUbiquitousItem(at:)`](../Foundation/filemanager/startdownloadingubiquitousitem%28at%29.md):

```swift
func fetchRemoteDocument(for localURL: URL) throws {
    let resources = try localURL.resourceValues(forKeys: [.ubiquitousItemIsUploadedKey])
    guard resources.ubiquitousItemIsUploaded != true else { return }
    FileManager.default.startDownloadingUbiquitousItem(at: localURL)
}
```

> ⚠️ **Warning**:  If you delete a file from iCloud by calling [`removeItem(at:)`](../Foundation/filemanager/removeitem%28at%29.md), the system deletes both the local and iCloud copy, and you can’t recover the file.

##### Copy files by creating clones

When you use [`copyItem(at:to:)`](../Foundation/filemanager/copyitem%28at,to%29.md) to copy a file on an APFS volume, the system creates a *clone* of the file. The clone refers to the original file’s content, so it uses less space on disk than if you duplicate the file through other methods. MetricKit’s [`TotalFileSizeMetric`](../MetricKit/totalfilesizemetric.md) accounts for clones in its calculations of the disk space used by your app.

For more information, see [About Apple File System](../Foundation/about-apple-file-system.md).

## See Also

### Disk usage
- [Reducing disk writes](./reducing-disk-writes.md)
  Improve your app’s responsiveness by optimizing how it writes data to permanent storage.
- [Monitoring your app’s storage metrics](./monitoring-your-app-s-storage-metrics.md)
  Track your app’s storage footprint over time using Xcode Organizer to catch regressions in Documents & Data and App Size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-your-app-s-disk-usage)*