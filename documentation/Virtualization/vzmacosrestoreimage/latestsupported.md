# latestSupported

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

Fetches the latest restore image supported by this host from the network.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class var latestSupported: VZMacOSRestoreImage { get async throws }
```

```objc
+ (void) fetchLatestSupportedWithCompletionHandler:(void (^)(VZMacOSRestoreImage *, NSError *)) completionHandler;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

## Discussion

Construct a [`VZMacOSInstaller`](../vzmacosinstaller.md) object with a `VZMacOSRestoreImage` loaded from a file on the local file system. A `VZMacOSRestoreImage` fetched with the [`latestSupported`](./latestsupported.md) method has a URL property that refers to a restore image on the network.

To use a network restore image, download the file to disk (using [`URLSession`](../../Foundation/urlsession.md) or similar API). After downloading the restore image, you can initialize a [`VZMacOSInstaller`](../vzmacosinstaller.md) using a URL referring to the local file.

## See Also

### Controlling the Restoration Process
- [class func fetchLatestSupported(completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](./fetchlatestsupported%28completionhandler%29.md)
  Fetches the latest restore image supported by this host from the network.
- [class func load(from: URL, completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](./load%28from,completionhandler%29.md)
  Load a restore image from a file on the local file system.
- [class func image(from: URL) async throws -> VZMacOSRestoreImage](./image%28from%29.md)
  Load a restore image from a file on the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/latestsupported)*