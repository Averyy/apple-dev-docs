# stop(completionHandler:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Stops a VM that’s in either a running or paused state.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func stop(completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
func stop() async throws
```

```objc
- (void) stopWithCompletionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

#### Discussion

> ⚠️ **Warning**:  This is a destructive operation. It stops the VM without giving the guest a chance to stop cleanly.

To determine if a VM is in a state that allows you to stop it, check the VM’s [`canStop`](./canstop.md) or [`canRequestStop`](./canrequeststop.md) properties.

## Parameters

- `completionHandler`: A block called after the VM stopped successfully, or on error. The error parameter passed to the block is `nil` if the stop was successful.

## See Also

### Starting and stopping the VM
- [func start(completionHandler: (Result<Void, any Error>) -> Void)](./start%28completionhandler%29.md)
  Starts the VM and notifies the specified completion handler if startup is successful.
- [func start() async throws](./start%28%29.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
- [func start(options: VZVirtualMachineStartOptions, completionHandler: ((any Error)?) -> Void)](./start%28options,completionhandler%29.md)
  Starts the VM with the options and a completion handler you provide.
- [func pause(completionHandler: (Result<Void, any Error>) -> Void)](./pause%28completionhandler%29.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func requestStop() throws](./requeststop%28%29.md)
  Asks the guest operating system to stop running.
- [func resume(completionHandler: (Result<Void, any Error>) -> Void)](./resume%28completionhandler%29.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [func pause() async throws](./pause%28%29.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func resume() async throws](./resume%28%29.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [class VZVirtualMachineStartOptions](../vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/stop(completionhandler:))*