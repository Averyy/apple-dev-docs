# minimumAllowedCPUCount

**Framework**: Virtualization  
**Kind**: property

The minimum number of CPUs you may configure for the VM.

**Availability**:
- macOS ?+

## Declaration

```swift
class var minimumAllowedCPUCount: Int { get }
```

#### Discussion

The value in the [`cpuCount`](vzvirtualmachineconfiguration/cpucount.md) property must be greater than or equal to the value in this property.

## See Also

- [var cpuCount: Int](vzvirtualmachineconfiguration/cpucount.md)
  The number of CPUs you make available to the guest operating system.
- [class var maximumAllowedCPUCount: Int](vzvirtualmachineconfiguration/maximumallowedcpucount.md)
  The maximum number of CPUs you may configure for the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/minimumallowedcpucount)*