# Reducing your app’s disk usage

**Framework**: Xcode

Measure and minimize the space your app uses to store its files.

#### Overview

People use multiple apps on a device, to create and access important content. Minimize your app’s disk usage to make more space for a person’s content, and to allow someone to install more apps on their device. Store recoverable data in purgeable locations, so that the system can free up space when it needs to.

##### Review Your Apps Disk Usage

To see the storage used by each app on your device, open Settings and choose General > Storage.

![A screenshot of Settings on iPhone, showing the storage used by each app on the device.](https://docs-assets.developer.apple.com/published/13e4beea418ff8835b18f3bd2f09178b/iphone-storage-settings%402x.png)

Tap on your app to see a breakdown of how the app’s bundle, documents, and data contribute to the overall disk usage.

##### Gather Metrics on Disk Usage

Use [`MXDiskSpaceUsageMetric`](https://developer.apple.com/documentation/MetricKit/MXDiskSpaceUsageMetric) to gather metrics on the number of files in your app’s container, and the disk space they occupy including space in the [`cachesDirectory`](https://developer.apple.com/documentation/Foundation/URL/cachesDirectory):

```swift
import MetricKit

class MetricService: NSObject, MXMetricManagerSubscriber {
    let metricManager: MXMetricManager = MXMetricManager.shared
    
    override init() {
        super.init()
        metricManager.add(self)
    }
    
    func didReceive(_ payloads: [MXMetricPayload]) {
        payloads.forEach({ payload in
            if let diskUsage = payload.diskSpaceUsageMetrics {
                // Analyze your app's disk usage.
            }
        })
    }
}
```

##### Use Purgeable Folders for Recoverable Content

When you download or otherwise generate content that your app can recover if it needs to, store that content in the [`cachesDirectory`](https://developer.apple.com/documentation/Foundation/URL/cachesDirectory) or the [`temporaryDirectory`](https://developer.apple.com/documentation/Foundation/FileManager/temporaryDirectory). The system automatically deletes content in the `cachesDirectory` and `temporaryDirectory` — an operation known as  — when it detects that disk space is low.

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

##### Manage Local Copies of Icloud Files

When a person isn’t using the local copy of a file that’s stored in iCloud, call [`evictUbiquitousItem(at:)`](https://developer.apple.com/documentation/Foundation/FileManager/evictUbiquitousItem(at:)) to remove the local copy while keeping the original on iCloud:

```swift
func removeLocalDocument(at localURL: URL) throws {
    let resources = try localURL.resourceValues(forKeys: [.ubiquitousItemIsUploadedKey])
    guard resources.ubiquitousItemIsUploaded == true else { return }
    FileManager.default.evictUbiquitousItem(at: localURL)
}
```

You can subsequently retrieve the file from iCloud by calling [`startDownloadingUbiquitousItem(at:)`](https://developer.apple.com/documentation/Foundation/FileManager/startDownloadingUbiquitousItem(at:)):

```swift
func fetchRemoteDocument(for localURL: URL) throws {
    let resources = try localURL.resourceValues(forKeys: [.ubiquitousItemIsUploadedKey])
    guard resources.ubiquitousItemIsUploaded != true else { return }
    FileManager.default.startDownloadingUbiquitousItem(at: localURL)
}
```

> ⚠️ **Warning**:  If you delete a file from iCloud by calling [`removeItem(at:)`](https://developer.apple.com/documentation/Foundation/FileManager/removeItem(at:)), the system deletes both the local and iCloud copy, and you can’t recover the file.

##### Copy Files By Creating Clones

When you use [`copyItem(at:to:)`](https://developer.apple.com/documentation/Foundation/FileManager/copyItem(at:to:)) to copy a file on an APFS volume, the system creates a  of the file. The clone refers to the original file’s content, so it uses less space on disk than if you duplicate the file through other methods. [`MXDiskSpaceUsageMetric`](https://developer.apple.com/documentation/MetricKit/MXDiskSpaceUsageMetric) accounts for clones in its calculations of the disk space used by your app.

For more information, see [`About Apple File System`](https://developer.apple.com/documentation/Foundation/about-apple-file-system#Clones-Reduce-the-Cost-of-Copying).

## See Also

- [Reducing disk writes](reducing-disk-writes.md)
  Improve your app’s responsiveness by optimizing how it writes data to permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-your-app-s-disk-usage)*