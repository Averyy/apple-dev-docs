# VZVirtualMachine.State.stopping

**Framework**: Virtualization  
**Kind**: case  
**Role**: Case

The VM is stopping.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case stopping
```

```c
VZVirtualMachineStateStopping
```

#### Discussion

This is the intermediate state between [`VZVirtualMachine.State.running`](./running.md) and [`VZVirtualMachine.State.stopped`](./stopped.md).

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
- [VZVirtualMachine.State.pausing](./pausing.md)
  The VM is pausing.
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
- [VZVirtualMachine.State.pausing](./pausing.md)
  The VM is pausing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.enum/stopping)*