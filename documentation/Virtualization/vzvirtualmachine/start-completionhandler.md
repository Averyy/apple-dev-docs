# start(completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Starts the VM and notifies the specified completion handler if startup is successful.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func start(completionHandler: @escaping (Result<Void, any Error>) -> Void)
```

#### Discussion

Call this method to start a VM that’s in the [`VZVirtualMachine.State.stopped`](vzvirtualmachine/state-swift.enum/stopped.md) or [`VZVirtualMachine.State.error`](vzvirtualmachine/state-swift.enum/error.md) state. To determine if a VM is in a state that allows you to start it, check the VM’s [`canStart`](vzvirtualmachine/canstart.md) property.

## Parameters

- `completionHandler`: The block to call with the results of the startup attempt. This block has no return value and has one   object as its parameter:

## See Also

- [func start() async throws](vzvirtualmachine/start.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
- [func start(options: VZVirtualMachineStartOptions, completionHandler: ((any Error)?) -> Void)](vzvirtualmachine/start(options:completionhandler:).md)
  Starts the VM with the options and a completion handler you provide.
- [func stop(completionHandler: ((any Error)?) -> Void)](vzvirtualmachine/stop(completionhandler:).md)
  Stops a VM that’s in either a running or paused state.
- [func pause(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/pause(completionhandler:).md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func requestStop() throws](vzvirtualmachine/requeststop.md)
  Asks the guest operating system to stop running.
- [func resume(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/resume(completionhandler:).md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [func pause() async throws](vzvirtualmachine/pause.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func resume() async throws](vzvirtualmachine/resume.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/start(completionhandler:))*