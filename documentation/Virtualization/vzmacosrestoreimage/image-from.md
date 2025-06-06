# image(from:)

**Framework**: Virtualization  
**Kind**: method

Load a restore image from a file on the local file system.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func image(from fileURL: URL) async throws -> VZMacOSRestoreImage
```

#### Discussion

`VZMacOSRestoreImage` can load macOS installation media from a local file. If the `fileURL` parameter doesn’t refer to a local file, the system raises an exception.

## Parameters

- `fileURL`: A file URL that indicates the macOS restore image to load.

## See Also

- [class func fetchLatestSupported(completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](vzmacosrestoreimage/fetchlatestsupported(completionhandler:).md)
  Fetches the latest restore image supported by this host from the network.
- [class func load(from: URL, completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](vzmacosrestoreimage/load(from:completionhandler:).md)
  Load a restore image from a file on the local file system.
- [class var latestSupported: VZMacOSRestoreImage](vzmacosrestoreimage/latestsupported.md)
  Fetches the latest restore image supported by this host from the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/image(from:))*