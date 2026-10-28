# canRequestStop

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can ask the guest operating system to stop running.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var canRequestStop: Bool { get }
```

```objc
@property (readonly) BOOL canRequestStop;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the VM is in a state that allows it to stop running. Call the [`requestStop()`](./requeststop%28%29.md) method to ask the guest operating system to stop running.

## See Also

### Getting the state of the VM
- [var state: VZVirtualMachine.State](./state-swift.property.md)
  The current execution state of the VM.
- [VZVirtualMachine.State](./state-swift.enum.md)
  The execution states of the VM.
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
- [var queue: dispatch_queue_t](./queue.md)
  The queue associated with this virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/canrequeststop)*