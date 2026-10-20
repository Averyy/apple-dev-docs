# VZVirtualMachine.State.pausing

**Framework**: Virtualization  
**Kind**: case  
**Role**: Case

The VM is pausing.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case pausing
```

```c
VZVirtualMachineStatePausing
```

#### Discussion

This state is an intermediate state between the [`VZVirtualMachine.State.running`](./running.md) and [`VZVirtualMachine.State.paused`](./paused.md) states.

## See Also

### States
- [VZVirtualMachine.State.stopped](./stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](./running.md)
  The VM is running.
- [VZVirtualMachine.State.paused](./paused.md)
  The framework has paused a started VM.
- [VZVirtualMachine.State.error](./error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](./starting.md)
  The VM is configuring the hardware preparing to run.
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
- [VZVirtualMachine.State.paused](./paused.md)
  The framework has paused a started VM.
- [VZVirtualMachine.State.error](./error.md)
  The VM encountered an unrecoverable error.
- [VZVirtualMachine.State.starting](./starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.stopping](./stopping.md)
  The VM is stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.enum/pausing)*