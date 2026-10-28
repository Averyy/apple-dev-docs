# install()

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Start installing macOS.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func install() async throws
```

```objc
- (void) installWithCompletionHandler:(void (^)(NSError *)) completionHandler;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

## Discussion

This method starts the installation process. The VM must be in a stopped state. During the installation operation, pausing or stopping the VM results in an undefined behavior.

If you start the installation on the same [`VZMacOSInstaller`](../vzmacosinstaller.md) object more than once, the framework raises an exception.

Call this method only on the VM’s queue.

## See Also

### Installing macOS
- [func install(completionHandler: (Result<Void, any Error>) -> Void)](./install%28completionhandler%29.md)
  Start installing macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosinstaller/install())*