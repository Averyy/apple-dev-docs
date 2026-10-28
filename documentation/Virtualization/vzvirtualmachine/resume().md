# resume()

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Resumes a paused VM and notifies the specified completion handler of the results.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func resume() async throws
```

```objc
- (void) resumeWithCompletionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

## Discussion

Call this method to resume a VM that’s in the [`VZVirtualMachine.State.paused`](./state-swift.enum/paused.md) state. To determine if a VM is in a state that allows you to resume it, check the VM’s [`canResume`](./canresume.md) property.

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
- [func pause(completionHandler: (Result<Void, any Error>) -> Void)](./pause%28completionhandler%29.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func requestStop() throws](./requeststop%28%29.md)
  Asks the guest operating system to stop running.
- [func resume(completionHandler: (Result<Void, any Error>) -> Void)](./resume%28completionhandler%29.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [func pause() async throws](./pause%28%29.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [class VZVirtualMachineStartOptions](../vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/resume())*