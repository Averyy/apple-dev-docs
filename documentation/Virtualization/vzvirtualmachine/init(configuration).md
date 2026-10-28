# init(configuration:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates the VM and configures it with the specified data.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init(configuration: VZVirtualMachineConfiguration)
```

```objc
- (instancetype) initWithConfiguration:(VZVirtualMachineConfiguration *) configuration;
```

## Return Value

An initialized VM object.

## Discussion

This VM uses your app’s main queue for all operations. You must perform all VM-related operations on the main queue, and the VM executes all callbacks and delegate methods on the main queue.

## Parameters

- `configuration`: The configuration of the VM. The configuration must be valid, and you can verify that it’s valid by calling its [`validate()`](../vzvirtualmachineconfiguration/validate%28%29.md) method. The VM stores a copy of the configuration.

## See Also

### Creating the VM
- [init(configuration: VZVirtualMachineConfiguration, queue: dispatch_queue_t)](./init%28configuration,queue%29.md)
  Creates and configures the VM with the specified data and dispatch queue.
- [class var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the system supports virtualization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/init(configuration:))*