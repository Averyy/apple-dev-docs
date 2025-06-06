# validateSaveRestoreSupport()

**Framework**: Virtualization  
**Kind**: method

Determines whether the framework can save or restore the VM’s current configuration.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func validateSaveRestoreSupport() throws
```

#### Discussion

Use this method to verify that a virtual machine with this configuration is savable.

- Not all configuration options can be safely saved and restored from the configuration file on disk.
- If this method returns `false`, the caller should expect future calls to [`saveMachineStateTo(url:completionHandler:)`](vzvirtualmachine/savemachinestateto(url:completionhandler:).md) to fail.

## See Also

- [func validate() throws](vzvirtualmachineconfiguration/validate.md)
  Validates the current configuration settings and reports any issues that might prevent the successful initialization of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/validatesaverestoresupport())*