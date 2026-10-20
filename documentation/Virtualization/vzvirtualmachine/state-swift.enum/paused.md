# VZVirtualMachine.State.paused

**Framework**: Virtualization  
**Kind**: case  
**Role**: Case

The framework has paused a started VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case paused
```

```c
VZVirtualMachineStatePaused
```

#### Discussion

The virtual machine can enter this state only from the [`VZVirtualMachine.State.pausing`](./pausing.md) state.

## See Also

### States
- [VZVirtualMachine.State.stopped](./stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](./running.md)
  The VM is running.
- [VZVirtualMachine.State.error](./error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](./starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.pausing](./pausing.md)
  The VM is pausing.
- [VZVirtualMachine.State.stopping](./stopping.md)
  The VM is stopping.
- [VZVirtualMachine.State.resuming](./resuming.md)
  The VM is resuming from a paused state.
- [VZVirtualMachine.State.restoring](./restoring.md)
  The VM is restoring from a saved state.
- [VZVirtualMachine.State.saving](./saving.md)
  The VM is saving its state.
- [VZVirtualMachine.State.stopped](./stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](./running.md)
  The VM is running.
- [VZVirtualMachine.State.error](./error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](./starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.pausing](./pausing.md)
  The VM is pausing.
- [VZVirtualMachine.State.stopping](./stopping.md)
  The VM is stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.enum/paused)*