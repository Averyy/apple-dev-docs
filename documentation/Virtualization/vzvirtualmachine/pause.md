# pause()

**Framework**: Virtualization  
**Kind**: method

Pauses a running VM and notifies the specified completion handler of the results.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func pause() async throws
```

#### Discussion

Call this method to pause a VM that’s in the [`VZVirtualMachine.State.running`](vzvirtualmachine/state-swift.enum/running.md) state. To determine if a VM is in a state that allows you to pause it, check the VM’s [`canPause`](vzvirtualmachine/canpause.md) property.

If the VM stops before the attempt to pause it finishes, this method calls the completion handler with an error.

## See Also

- [func start(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/start(completionhandler:).md)
  Starts the VM and notifies the specified completion handler if startup is successful.
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
- [func resume() async throws](vzvirtualmachine/resume.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/pause())*