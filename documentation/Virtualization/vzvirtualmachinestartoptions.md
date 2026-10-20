# VZVirtualMachineStartOptions

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The abstract class for VM start options.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtualMachineStartOptions
```

```objc
@interface VZVirtualMachineStartOptions : NSObject
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZMacOSVirtualMachineStartOptions](./vzmacosvirtualmachinestartoptions.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZMacOSVirtualMachineStartOptions](./vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
### Starting and stopping the VM
- [func start(completionHandler: (Result<Void, any Error>) -> Void)](./vzvirtualmachine/start%28completionhandler%29.md)
  Starts the VM and notifies the specified completion handler if startup is successful.
- [func start() async throws](./vzvirtualmachine/start%28%29.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
- [func start(options: VZVirtualMachineStartOptions, completionHandler: ((any Error)?) -> Void)](./vzvirtualmachine/start%28options,completionhandler%29.md)
  Starts the VM with the options and a completion handler you provide.
- [func stop(completionHandler: ((any Error)?) -> Void)](./vzvirtualmachine/stop%28completionhandler%29.md)
  Stops a VM that’s in either a running or paused state.
- [func pause(completionHandler: (Result<Void, any Error>) -> Void)](./vzvirtualmachine/pause%28completionhandler%29.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func requestStop() throws](./vzvirtualmachine/requeststop%28%29.md)
  Asks the guest operating system to stop running.
- [func resume(completionHandler: (Result<Void, any Error>) -> Void)](./vzvirtualmachine/resume%28completionhandler%29.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [func pause() async throws](./vzvirtualmachine/pause%28%29.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func resume() async throws](./vzvirtualmachine/resume%28%29.md)
  Resumes a paused VM and notifies the specified completion handler of the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachinestartoptions)*