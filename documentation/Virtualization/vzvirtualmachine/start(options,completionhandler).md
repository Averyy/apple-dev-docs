# start(options:completionHandler:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Starts the VM with the options and a completion handler you provide.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func start(options: VZVirtualMachineStartOptions, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
func start(options: VZVirtualMachineStartOptions) async throws
```

```objc
- (void) startWithOptions:(VZVirtualMachineStartOptions *) options completionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

## Parameters

- `options`: A [`VZVirtualMachineStartOptions`](../vzvirtualmachinestartoptions.md) object that describes controlling startup behavior of a VM using [`VZMacOSBootLoader`](../vzmacosbootloader.md).
- `completionHandler`: The block to call with the results of the startup attempt. This block has no return value and has one [`NSError`](../../Foundation/nserror.md) object as its parameter:

  - **error**: A result type that contains an error object when the VM fails to start.

## See Also

### Related Documentation
- [class VZMacOSVirtualMachineStartOptions](../vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
### Starting and stopping the VM
- [func start(completionHandler: (Result<Void, any Error>) -> Void)](./start%28completionhandler%29.md)
  Starts the VM and notifies the specified completion handler if startup is successful.
- [func start() async throws](./start%28%29.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
- [func stop(completionHandler: ((any Error)?) -> Void)](./stop%28completionhandler%29.md)
  Stops a VM that’s in either a running or paused state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/start(options:completionhandler:))*