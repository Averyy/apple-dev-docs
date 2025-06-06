# isSupported

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the system supports virtualization.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class var isSupported: Bool { get }
```

#### Discussion

If virtualization is unavailable on the current device, no configuration is valid. If you want to know more about why virtualization is unavailable, call the [`validate()`](vzvirtualmachineconfiguration/validate().md) method of [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) and examine the returned error object.

## See Also

- [convenience init(configuration: VZVirtualMachineConfiguration)](vzvirtualmachine/init(configuration:).md)
  Creates the VM and configures it with the specified data.
- [init(configuration: VZVirtualMachineConfiguration, queue: dispatch_queue_t)](vzvirtualmachine/init(configuration:queue:).md)
  Creates and configures the VM with the specified data and dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/issupported)*