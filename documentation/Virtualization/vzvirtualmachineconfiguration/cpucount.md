# cpuCount

**Framework**: Virtualization  
**Kind**: property

The number of CPUs you make available to the guest operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var cpuCount: Int { get set }
```

#### Discussion

The value of this property must be greater than or equal to the value in [`minimumAllowedCPUCount`](vzvirtualmachineconfiguration/minimumallowedcpucount.md), and less than or equal to the value in [`maximumAllowedCPUCount`](vzvirtualmachineconfiguration/maximumallowedcpucount.md). The system uses the number of physical CPUs on the current system to determine a default value.

## See Also

- [class var minimumAllowedCPUCount: Int](vzvirtualmachineconfiguration/minimumallowedcpucount.md)
  The minimum number of CPUs you may configure for the VM.
- [class var maximumAllowedCPUCount: Int](vzvirtualmachineconfiguration/maximumallowedcpucount.md)
  The maximum number of CPUs you may configure for the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/cpucount)*