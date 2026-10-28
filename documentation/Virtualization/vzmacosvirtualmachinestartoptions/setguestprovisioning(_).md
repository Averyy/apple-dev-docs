# setGuestProvisioning(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Sets guest provisioning options with validation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func setGuestProvisioning(_ guestProvisioningOptions: VZMacGuestProvisioningOptions?) throws
```

```objc
- (BOOL) setGuestProvisioningOptions:(VZMacGuestProvisioningOptions *) guestProvisioningOptions error:(NSError **) error;
```

## Discussion

This method validates the provisioning options before setting them. If validation fails, the current options remain unchanged.

## Parameters

- `guestProvisioningOptions`: The guest provisioning options to set, or `nil` to remove.

## See Also

### Related Documentation
- [class VZMacGuestProvisioningOptions](../vzmacguestprovisioningoptions.md)
  The configuration for guest setup during macOS virtual machine startup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosvirtualmachinestartoptions/setguestprovisioning(_:))*