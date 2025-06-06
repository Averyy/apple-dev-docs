# bootLoader

**Framework**: Virtualization  
**Kind**: property

The guest system to boot when the VM starts.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var bootLoader: VZBootLoader? { get set }
```

#### Discussion

Assign the boot loader object that contains information about how to load your guest operating system. For example, to configure your VM with a Linux operating system, assign a [`VZLinuxBootLoader`](vzlinuxbootloader.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/bootloader)*