# VZVirtualMachine.State

**Framework**: Virtualization  
**Kind**: enum  
**Role**: Enumeration

The execution states of the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum State
```

```c
enum VZVirtualMachineState : NSInteger;
```

## Topics

### States
- [VZVirtualMachine.State.stopped](./state-swift.enum/stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](./state-swift.enum/running.md)
  The VM is running.
- [VZVirtualMachine.State.paused](./state-swift.enum/paused.md)
  The framework has paused a started VM.
- [VZVirtualMachine.State.error](./state-swift.enum/error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](./state-swift.enum/starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.pausing](./state-swift.enum/pausing.md)
  The VM is pausing.
- [VZVirtualMachine.State.stopping](./state-swift.enum/stopping.md)
  The VM is stopping.
- [VZVirtualMachine.State.resuming](./state-swift.enum/resuming.md)
  The VM is resuming from a paused state.
- [VZVirtualMachine.State.restoring](./state-swift.enum/restoring.md)
  The VM is restoring from a saved state.
- [VZVirtualMachine.State.saving](./state-swift.enum/saving.md)
  The VM is saving its state.
- [VZVirtualMachine.State.stopped](./state-swift.enum/stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](./state-swift.enum/running.md)
  The VM is running.
- [VZVirtualMachine.State.paused](./state-swift.enum/paused.md)
  The framework has paused a started VM.
- [VZVirtualMachine.State.error](./state-swift.enum/error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](./state-swift.enum/starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.pausing](./state-swift.enum/pausing.md)
  The VM is pausing.
- [VZVirtualMachine.State.stopping](./state-swift.enum/stopping.md)
  The VM is stopping.
- [VZVirtualMachine.State.resuming](./state-swift.enum/resuming.md)
  The VM is resuming from a paused state.
- [VZVirtualMachine.State.restoring](./state-swift.enum/restoring.md)
  The VM is restoring from a saved state.
- [VZVirtualMachine.State.saving](./state-swift.enum/saving.md)
  The VM is saving its state.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the state of the VM
- [var state: VZVirtualMachine.State](./state-swift.property.md)
  The current execution state of the VM.
- [var graphicsDevices: [VZGraphicsDevice]](./graphicsdevices.md)
  The list of configured graphics devices on the virtual machine.
- [var canStart: Bool](./canstart.md)
  A Boolean value that indicates whether you can start the VM.
- [var canPause: Bool](./canpause.md)
  A Boolean value that indicates whether you can pause the VM.
- [var canResume: Bool](./canresume.md)
  A Boolean value that indicates whether you can resume the VM.
- [var canStop: Bool](./canstop.md)
  A Boolean value that indicates whether you can stop the VM.
- [var canRequestStop: Bool](./canrequeststop.md)
  A Boolean value that indicates whether you can ask the guest operating system to stop running.
- [var queue: dispatch_queue_t](./queue.md)
  The queue associated with this virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.enum)*