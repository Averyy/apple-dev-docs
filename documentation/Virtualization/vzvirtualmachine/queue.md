# queue

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The queue associated with this virtual machine.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
var queue: dispatch_queue_t { get }
```

```objc
@property (nonatomic, readonly) dispatch_queue_t queue;
```

#### Discussion

This property is a reference to the queue the framework used to create the virtual machine when initialized using [`init(configuration:queue:)`](./init%28configuration,queue%29.md). If not specified, the default is the main queue.

The property is accessible from any queue or actor.

Other properties or function calls on [`VZVirtualMachine`](../vzvirtualmachine.md) must happen on this queue. The framework also invokes any completion handlers from asynchronous functions on this queue.

The following example shows use of the `VZVirtualMachine.queue` property to check to see if it’s possible to start a VM.

**Swift**:

```swift
let canStart = virtualMachine.queue.sync {
    virtualMachine.canStart
}
```

**Objective-C**:

```objective-c
    BOOL canStart = NO;
    dispatch_sync(virtualMachine.queue, ^{
        canStart = virtualMachine.canStart;
    });
```

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
- [var canRequestStop: Bool](./canrequeststop.md)
  A Boolean value that indicates whether you can ask the guest operating system to stop running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/queue)*