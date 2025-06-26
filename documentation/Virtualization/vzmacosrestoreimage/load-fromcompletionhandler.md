# load(from:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Load a restore image from a file on the local file system.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@preconcurrency
class func load(from fileURL: URL, completionHandler: @escaping (Result<VZMacOSRestoreImage, any Error>) -> Void)
```

#### Discussion

`VZMacOSRestoreImage` can load macOS installation media from a local file. If the `fileURL` parameter doesn’t refer to a local file, the system raises an exception.

## Parameters

- `fileURL`: A file URL that indicates the macOS restore image to load.
- `completionHandler`: The system invokes the completion handler on an arbitrary thread.

## See Also

- [class func fetchLatestSupported(completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](vzmacosrestoreimage/fetchlatestsupported(completionhandler:).md)
  Fetches the latest restore image supported by this host from the network.
- [class var latestSupported: VZMacOSRestoreImage](vzmacosrestoreimage/latestsupported.md)
  Fetches the latest restore image supported by this host from the network.
- [class func image(from: URL) async throws -> VZMacOSRestoreImage](vzmacosrestoreimage/image(from:).md)
  Load a restore image from a file on the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/load(from:completionhandler:))*