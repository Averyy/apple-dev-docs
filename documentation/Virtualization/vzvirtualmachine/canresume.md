# canResume

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether you can resume the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var canResume: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the VM is in a state that allows you to resume it. Call the [`resume(completionHandler:)`](vzvirtualmachine/resume(completionhandler:).md) method (Swift)  or [`resume()`](vzvirtualmachine/resume().md) method (Objective-C) to resume the VM

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
- [var canStop: Bool](vzvirtualmachine/canstop.md)
  A Boolean value that indicates whether you can stop the VM.
- [var canRequestStop: Bool](vzvirtualmachine/canrequeststop.md)
  A Boolean value that indicates whether you can ask the guest operating system to stop running.
- [var queue: dispatch_queue_t](vzvirtualmachine/queue.md)
  The queue associated with this virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/canresume)*