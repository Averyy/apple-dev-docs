# install(completionHandler:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Start installing macOS.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@preconcurrency
func install(completionHandler: @escaping @Sendable (Result<Void, any Error>) -> Void)
```

## Discussion

This method starts the installation process. The VM must be in a stopped state. During the installation operation, pausing or stopping the VM results in an undefined behavior.

If you start the installation on the same [`VZMacOSInstaller`](../vzmacosinstaller.md) object more than once, the framework raises an exception.

Call this method only on the VM’s queue.

## Parameters

- `completionHandler`: A block the framework calls after installation has completed successfully or has failed.

  The `error` parameter passed to the block is `nil` if installation was successful. The framework invokes the block on the VM’s queue. The completion handler returns an `error` parameter that describes the reason for the failure; the `error` is `nil` if installation was successful.

## See Also

### Installing macOS
- [func install() async throws](./install%28%29.md)
  Start installing macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosinstaller/install(completionhandler:))*