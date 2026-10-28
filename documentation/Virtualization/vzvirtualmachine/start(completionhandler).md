# start(completionHandler:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Starts the VM and notifies the specified completion handler if startup is successful.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func start(completionHandler: @escaping (Result<Void, any Error>) -> Void)
```

## Discussion

Call this method to start a VM that’s in the [`VZVirtualMachine.State.stopped`](./state-swift.enum/stopped.md) or [`VZVirtualMachine.State.error`](./state-swift.enum/error.md) state. To determine if a VM is in a state that allows you to start it, check the VM’s [`canStart`](./canstart.md) property.

## Parameters

- `completionHandler`: The block to call with the results of the startup attempt. This block has no return value and has one [`NSError`](../../Foundation/nserror.md) object as its parameter:

  - **result**: A result type that contains an error object when the VM fails to start.

## See Also

### Starting and stopping the VM
- [func start() async throws](./start%28%29.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
- [func start(options: VZVirtualMachineStartOptions, completionHandler: ((any Error)?) -> Void)](./start%28options,completionhandler%29.md)
  Starts the VM with the options and a completion handler you provide.
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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/start(completionhandler:))*