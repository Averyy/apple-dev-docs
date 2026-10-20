# requestStop()

**Framework**: Virtualization  
**Kind**: method

Asks the guest operating system to stop running.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func requestStop() throws
```

#### Discussion

> **Note**:  In Objective-C, this function returns a value that indicates if the VM was in a stoppable state when you made the request. It doesn’t reflect whether the VM will exit or has exited.

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
- [func resume(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/resume(completionhandler:).md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [func pause() async throws](vzvirtualmachine/pause.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func resume() async throws](vzvirtualmachine/resume.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/requeststop())*