# VZVirtualMachine.State.pausing

**Framework**: Virtualization  
**Kind**: case

The VM is pausing.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case pausing
```

#### Discussion

This state is an intermediate state between the [`VZVirtualMachine.State.running`](vzvirtualmachine/state-swift.enum/running.md) and [`VZVirtualMachine.State.paused`](vzvirtualmachine/state-swift.enum/paused.md) states.

## See Also

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
- [VZVirtualMachine.State.stopping](vzvirtualmachine/state-swift.enum/stopping.md)
  The VM is stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.enum/pausing)*