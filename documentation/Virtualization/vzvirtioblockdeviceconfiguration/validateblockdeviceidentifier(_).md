# validateBlockDeviceIdentifier(_:)

**Framework**: Virtualization  
**Kind**: method

Checks the validity of a block device identifier.

**Availability**:
- macOS 12.3+

## Declaration

```swift
class func validateBlockDeviceIdentifier(_ blockDeviceIdentifier: String) throws
```

#### Discussion

Use [`validateBlockDeviceIdentifier(_:)`](vzvirtioblockdeviceconfiguration/validateblockdeviceidentifier(_:).md) to validate an identifier string before trying to set the [`blockDeviceIdentifier`](vzvirtioblockdeviceconfiguration/blockdeviceidentifier.md) property. The identifier must be an ASCII encodable string of 20 bytes or less.

## Parameters

- `blockDeviceIdentifier`: The device identifier to validate. In the case of an invalid identifier string, the method throws an error that describes why the device identifier isn’t valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioblockdeviceconfiguration/validateblockdeviceidentifier(_:))*