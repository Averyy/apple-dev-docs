# state

**Framework**: Virtualization  
**Kind**: property

The current execution state of the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var state: VZVirtualMachine.State { get }
```

## See Also

- [VZVirtualMachine.State](vzvirtualmachine/state-swift.enum.md)
  The execution states of the VM.
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
- [var queue: dispatch_queue_t](vzvirtualmachine/queue.md)
  The queue associated with this virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/state-swift.property)*