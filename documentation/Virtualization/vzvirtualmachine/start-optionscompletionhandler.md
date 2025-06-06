# start(options:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Starts the VM with the options and a completion handler you provide.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func start(options: VZVirtualMachineStartOptions) async throws
```

## Parameters

- `options`: A   object that describes controlling startup behavior of a VM using  .
- `completionHandler`: The block to call with the results of the startup attempt. This block has no return value and has one   object as its parameter:

## See Also

- [class VZMacOSVirtualMachineStartOptions](vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
- [func start(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/start(completionhandler:).md)
  Starts the VM and notifies the specified completion handler if startup is successful.
- [func start() async throws](vzvirtualmachine/start.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/start(options:completionhandler:))*