# queue

**Framework**: Virtualization  
**Kind**: property

The queue associated with this virtual machine.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
var queue: dispatch_queue_t { get }
```

#### Discussion

This property is a reference to the queue the framework used to create the virtual machine when initialized using [`init(configuration:queue:)`](vzvirtualmachine/init(configuration:queue:).md). If not specified, the default is the main queue.

The property is accessible from any queue or actor.

Other properties or function calls on [`VZVirtualMachine`](vzvirtualmachine.md) must happen on this queue. The framework also invokes any completion handlers from asynchronous functions on this queue.

The following example shows use of the `VZVirtualMachine.queue` property to check to see if it’s possible to start a VM.

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
- [var canStop: Bool](vzvirtualmachine/canstop.md)
  A Boolean value that indicates whether you can stop the VM.
- [var canRequestStop: Bool](vzvirtualmachine/canrequeststop.md)
  A Boolean value that indicates whether you can ask the guest operating system to stop running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/queue)*