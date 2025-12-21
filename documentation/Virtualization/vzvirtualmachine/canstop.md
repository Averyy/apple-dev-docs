# canStop

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether you can stop the VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var canStop: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the VM is in a state that allows you to stop it. Call the [`stop(completionHandler:)`](vzvirtualmachine/stop(completionhandler:).md) to stop the VM.

## See Also

- [var state: VZVirtualMachine.State](vzvirtualmachine/state-swift.property.md)
  The current execution state of the VM.
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
- [var canRequestStop: Bool](vzvirtualmachine/canrequeststop.md)
  A Boolean value that indicates whether you can ask the guest operating system to stop running.
- [var queue: dispatch_queue_t](vzvirtualmachine/queue.md)
  The queue associated with this virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/canstop)*