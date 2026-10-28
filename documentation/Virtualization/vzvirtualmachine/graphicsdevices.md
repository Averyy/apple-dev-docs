# graphicsDevices

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The list of configured graphics devices on the virtual machine.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var graphicsDevices: [VZGraphicsDevice] { get }
```

```objc
@property (copy, readonly) NSArray<VZGraphicsDevice *> * graphicsDevices;
```

## Discussion

Returns an empty array if there are no graphics devices configured.

## See Also

### Related Documentation
- [class VZGraphicsDeviceConfiguration](../vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.
- [class VZVirtualMachineConfiguration](../vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
### Getting the state of the VM
- [var state: VZVirtualMachine.State](./state-swift.property.md)
  The current execution state of the VM.
- [VZVirtualMachine.State](./state-swift.enum.md)
  The execution states of the VM.
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
- [var queue: dispatch_queue_t](./queue.md)
  The queue associated with this virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/graphicsdevices)*