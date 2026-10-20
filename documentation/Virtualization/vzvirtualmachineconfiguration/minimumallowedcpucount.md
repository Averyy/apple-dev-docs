# minimumAllowedCPUCount

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

The minimum number of CPUs you may configure for the VM.

**Availability**:
- macOS

## Declaration

```swift
class var minimumAllowedCPUCount: Int { get }
```

```objc
@property (class, readonly) NSUInteger minimumAllowedCPUCount;
```

#### Discussion

The value in the [`cpuCount`](./cpucount.md) property must be greater than or equal to the value in this property.

## See Also

### Setting the number of CPUs
- [var cpuCount: Int](./cpucount.md)
  The number of CPUs you make available to the guest operating system.
- [class var maximumAllowedCPUCount: Int](./maximumallowedcpucount.md)
  The maximum number of CPUs you may configure for the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/minimumallowedcpucount)*