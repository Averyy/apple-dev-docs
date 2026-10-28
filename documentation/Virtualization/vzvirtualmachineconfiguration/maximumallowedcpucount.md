# maximumAllowedCPUCount

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

The maximum number of CPUs you may configure for the VM.

**Availability**:
- macOS

## Declaration

```swift
class var maximumAllowedCPUCount: Int { get }
```

```objc
@property (class, readonly) NSUInteger maximumAllowedCPUCount;
```

## Discussion

The value in the [`cpuCount`](./cpucount.md) property must be less than or equal to the value in this property.

## See Also

### Setting the number of CPUs
- [var cpuCount: Int](./cpucount.md)
  The number of CPUs you make available to the guest operating system.
- [class var minimumAllowedCPUCount: Int](./minimumallowedcpucount.md)
  The minimum number of CPUs you may configure for the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/maximumallowedcpucount)*