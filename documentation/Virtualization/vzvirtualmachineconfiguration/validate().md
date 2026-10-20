# validate()

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Validates the current configuration settings and reports any issues that might prevent the successful initialization of the VM.

**Availability**:
- macOS

## Declaration

```swift
func validate() throws
```

```objc
- (BOOL) validateWithError:(NSError **) error;
```

## See Also

### Validating the configuration
- [func validateSaveRestoreSupport() throws](./validatesaverestoresupport%28%29.md)
  Determines whether the framework can save or restore the VM’s current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/validate())*