# VZVirtualMachine.State.error

**Framework**: Virtualization  
**Kind**: case  
**Role**: Case

The VM encountered an unrecoverable error.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case error
```

```c
VZVirtualMachineStateError
```

## Discussion

The VM encountered an unrecoverable error and the framework can no longer use the VM; you need to destroy the [`VZVirtualMachine`](../../vzvirtualmachine.md) object.

## See Also

### States
- [VZVirtualMachine.State.stopped](./stopped.md)
  The VM isn’t running.
- [VZVirtualMachine.State.running](./running.md)
  The VM is running.
- [VZVirtualMachine.State.paused](./paused.md)
  The framework has paused a started VM.
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
- [VZVirtualMachine.State.paused](./paused.md)
  The framework has paused a started VM.
- [VZVirtualMachine.State.starting](./starting.md)
  The VM is configuring the hardware preparing to run.
- [VZVirtualMachine.State.pausing](./pausing.md)
  The VM is pausing.
- [VZVirtualMachine.State.stopping](./stopping.md)
  The VM is stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.enum/error)*