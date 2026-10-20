# pause(completionHandler:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Pauses a running VM and notifies the specified completion handler of the results.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func pause(completionHandler: @escaping (Result<Void, any Error>) -> Void)
```

#### Discussion

Call this method to pause a Vm that’s in the [`VZVirtualMachine.State.running`](./state-swift.enum/running.md) state. To determine if a virtual machine is in a state that allows you to pause it, check the VM’s [`canPause`](./canpause.md) property.

## Parameters

- `completionHandler`: The block to call with the results of the pause attempt. This block has no return value and has one [`NSError`](../../Foundation/nserror.md) object as its parameter:

  - **result**: A result type that contains an error object when the VM fails to pause.

## See Also

### Starting and stopping the VM
- [func start(completionHandler: (Result<Void, any Error>) -> Void)](./start%28completionhandler%29.md)
  Starts the VM and notifies the specified completion handler if startup is successful.
- [func start() async throws](./start%28%29.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
- [func start(options: VZVirtualMachineStartOptions, completionHandler: ((any Error)?) -> Void)](./start%28options,completionhandler%29.md)
  Starts the VM with the options and a completion handler you provide.
- [func stop(completionHandler: ((any Error)?) -> Void)](./stop%28completionhandler%29.md)
  Stops a VM that’s in either a running or paused state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/pause(completionhandler:))*