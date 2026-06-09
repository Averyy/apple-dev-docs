# setGuestProvisioning(_:)

**Framework**: Virtualization  
**Kind**: method

Sets guest provisioning options with validation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func setGuestProvisioning(_ guestProvisioningOptions: VZMacGuestProvisioningOptions?) throws
```

#### Discussion

This method validates the provisioning options before setting them. If validation fails, the current options remain unchanged.

## Parameters

- `guestProvisioningOptions`: The guest provisioning options to set, or `nil` to remove.

## See Also

- [class VZMacGuestProvisioningOptions](vzmacguestprovisioningoptions.md)
  The configuration for guest setup during macOS virtual machine startup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosvirtualmachinestartoptions/setguestprovisioning(_:))*