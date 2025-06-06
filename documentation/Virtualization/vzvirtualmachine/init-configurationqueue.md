# init(configuration:queue:)

**Framework**: Virtualization  
**Kind**: init

Creates and configures the VM with the specified data and dispatch queue.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(configuration: VZVirtualMachineConfiguration, queue: dispatch_queue_t)
```

#### Return Value

An initialized VM object.

## Parameters

- `configuration`: The configuration of the VM. The configuration must be valid, and you can verify that it’s valid by calling its   method. The VM stores a copy of the configuration.
- `queue`: The serial dispatch queue for the VM. You must perform all VM-related operations on the specified queue, and the VM executes callbacks and delegate methods on the queue. If the queue isn’t serial, the behavior isn’t defined.

## See Also

- [convenience init(configuration: VZVirtualMachineConfiguration)](vzvirtualmachine/init(configuration:).md)
  Creates the VM and configures it with the specified data.
- [class var isSupported: Bool](vzvirtualmachine/issupported.md)
  A Boolean value that indicates whether the system supports virtualization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/init(configuration:queue:))*