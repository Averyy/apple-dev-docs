# graphicsDevices

**Framework**: Virtualization  
**Kind**: property

The list of configured graphics devices on the virtual machine.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var graphicsDevices: [VZGraphicsDevice] { get }
```

#### Discussion

Returns an empty array if there are no graphics devices configured.

## See Also

- [class VZGraphicsDeviceConfiguration](vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.
- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [var state: VZVirtualMachine.State](vzvirtualmachine/state-swift.property.md)
  The current execution state of the VM.
- [VZVirtualMachine.State](vzvirtualmachine/state-swift.enum.md)
  The execution states of the VM.
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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/graphicsdevices)*