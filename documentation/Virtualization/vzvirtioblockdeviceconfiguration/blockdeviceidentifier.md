# blockDeviceIdentifier

**Framework**: Virtualization  
**Kind**: property

The string that identifies the VIRTIO block device.

**Availability**:
- macOS 12.3+

## Declaration

```swift
var blockDeviceIdentifier: String { get set }
```

#### Discussion

Use `blockDeviceIdentifier` to name devices so they’re more discoverable in the Linux guest. The identifier must be an ASCII encodable string of 20 bytes or less.

Validate the identifier string using [`validateBlockDeviceIdentifier(_:)`](vzvirtioblockdeviceconfiguration/validateblockdeviceidentifier(_:).md) before attempting to set this property, for example:

```swift
let idString = "ProjectData"
do {
    try VZVirtioBlockDeviceConfiguration.validateBlockDeviceIdentifier(idString)
    blockDeviceIdentifier = idString
} catch {
    // Handle error as appropriate.
    throw error
}
```

> ⚠️ **Warning**:  Setting the identifier to an invalid string results in a fatal error that terminates the app.

In a Linux guest, device identifiers are visible in the `/dev/disk/by-id/` directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioblockdeviceconfiguration/blockdeviceidentifier)*