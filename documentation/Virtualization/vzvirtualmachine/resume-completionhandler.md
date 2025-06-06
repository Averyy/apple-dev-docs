# resume(completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Resumes a paused VM and notifies the specified completion handler of the results.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func resume(completionHandler: @escaping (Result<Void, any Error>) -> Void)
```

#### Discussion

Call this method to resume a VM that’s in the [`VZVirtualMachine.State.paused`](vzvirtualmachine/state-swift.enum/paused.md) state.

## Parameters

- `completionHandler`: The block to call with the results of the resume attempt. This block has no return value and has one   object as its parameter. The completion handler returns an error object when the VM fails to resume.

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
- [func pause() async throws](vzvirtualmachine/pause.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func resume() async throws](vzvirtualmachine/resume.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/resume(completionhandler:))*