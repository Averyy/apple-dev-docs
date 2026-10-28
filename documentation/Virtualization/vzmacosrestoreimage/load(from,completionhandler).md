# load(from:completionHandler:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Type Method

Load a restore image from a file on the local file system.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@preconcurrency
class func load(from fileURL: URL, completionHandler: @escaping @Sendable (Result<VZMacOSRestoreImage, any Error>) -> Void)
```

## Discussion

`VZMacOSRestoreImage` can load macOS installation media from a local file. If the `fileURL` parameter doesn’t refer to a local file, the system raises an exception.

## Parameters

- `fileURL`: A file URL that indicates the macOS restore image to load.
- `completionHandler`: A block called after the restore image successfully loaded or has failed to load. The `error` parameter passed to the block is `nil` if the restore image loads successfully.

  The system invokes the completion handler on an arbitrary thread.

## See Also

### Controlling the Restoration Process
- [class func fetchLatestSupported(completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](./fetchlatestsupported%28completionhandler%29.md)
  Fetches the latest restore image supported by this host from the network.
- [class var latestSupported: VZMacOSRestoreImage](./latestsupported.md)
  Fetches the latest restore image supported by this host from the network.
- [class func image(from: URL) async throws -> VZMacOSRestoreImage](./image%28from%29.md)
  Load a restore image from a file on the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/load(from:completionhandler:))*