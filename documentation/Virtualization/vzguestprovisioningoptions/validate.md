# validate()

**Framework**: Virtualization  
**Kind**: method

Validates the provisioning options.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func validate() throws
```

#### Discussion

If validation fails, the error parameter contains a [`VZError`](vzerror.md) with a guest provisioning error code.

## See Also

- [VZError.Code](vzerror/code.md)
  Errors you might encounter when configuring or using a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzguestprovisioningoptions/validate())*