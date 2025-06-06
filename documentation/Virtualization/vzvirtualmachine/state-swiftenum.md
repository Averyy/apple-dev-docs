# VZVirtualMachine.State

**Framework**: Virtualization  
**Kind**: enum

The execution states of the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum State
```

## Topics

### States
- [VZVirtualMachine.State.stopped](vzvirtualmachine/state-swift.enum/stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](vzvirtualmachine/state-swift.enum/running.md)
  The VM is running.
- [VZVirtualMachine.State.paused](vzvirtualmachine/state-swift.enum/paused.md)
  The framework has paused a started VM.
- [VZVirtualMachine.State.error](vzvirtualmachine/state-swift.enum/error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](vzvirtualmachine/state-swift.enum/starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.pausing](vzvirtualmachine/state-swift.enum/pausing.md)
  The VM is pausing.
- [VZVirtualMachine.State.stopping](vzvirtualmachine/state-swift.enum/stopping.md)
  The VM is stopping.
- [VZVirtualMachine.State.resuming](vzvirtualmachine/state-swift.enum/resuming.md)
  The VM is resuming from a paused state.
- [VZVirtualMachine.State.restoring](vzvirtualmachine/state-swift.enum/restoring.md)
  The VM is restoring from a saved state.
- [VZVirtualMachine.State.saving](vzvirtualmachine/state-swift.enum/saving.md)
  The VM is saving its state.
- [VZVirtualMachine.State.stopped](vzvirtualmachine/state-swift.enum/stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](vzvirtualmachine/state-swift.enum/running.md)
  The VM is running.
- [VZVirtualMachine.State.paused](vzvirtualmachine/state-swift.enum/paused.md)
  The framework has paused a started VM.
- [VZVirtualMachine.State.error](vzvirtualmachine/state-swift.enum/error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](vzvirtualmachine/state-swift.enum/starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.pausing](vzvirtualmachine/state-swift.enum/pausing.md)
  The VM is pausing.
- [VZVirtualMachine.State.stopping](vzvirtualmachine/state-swift.enum/stopping.md)
  The VM is stopping.
- [VZVirtualMachine.State.resuming](vzvirtualmachine/state-swift.enum/resuming.md)
  The VM is resuming from a paused state.
- [VZVirtualMachine.State.restoring](vzvirtualmachine/state-swift.enum/restoring.md)
  The VM is restoring from a saved state.
- [VZVirtualMachine.State.saving](vzvirtualmachine/state-swift.enum/saving.md)
  The VM is saving its state.
### Initializers
- [init?(rawValue: Int)](vzvirtualmachine/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: VZVirtualMachine.State](vzvirtualmachine/state-swift.property.md)
  The current execution state of the VM.
- [var graphicsDevices: [VZGraphicsDevice]](vzvirtualmachine/graphicsdevices.md)
  The list of configured graphics devices on the virtual machine.
- [var canStart: Bool](vzvirtualmachine/canstart.md)
  A Boolean value that indicates whether you can start the VM.
- [var canPause: Bool](vzvirtualmachine/canpause.md)
  A Boolean value that indicates whether you can pause the VM.
- [var canResume: Bool](vzvirtualmachine/canresume.md)
  A Boolean value that indicates whether you can resume the VM.
- [var canStop: Bool](vzvirtualmachine/canstop.md)
  A Boolean value that indicates whether you can stop the VM.
- [var canRequestStop: Bool](vzvirtualmachine/canrequeststop.md)
  A Boolean value that indicates whether you can ask the guest operating system to stop running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.enum)*