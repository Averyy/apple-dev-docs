# label

**Framework**: Virtualization  
**Kind**: property

An optional label for the virtual machine.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

The framework uses this string as part of the name of the virtual machine in some system services. The label must be non-empty, less than or equal to 64 characters in length, and contain at least one non-whitespace character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/label)*