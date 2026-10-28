# validateBlockDeviceIdentifier(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Type Method

Checks the validity of a block device identifier.

**Availability**:
- macOS 12.3+

## Declaration

```swift
class func validateBlockDeviceIdentifier(_ blockDeviceIdentifier: String) throws
```

```objc
+ (BOOL) validateBlockDeviceIdentifier:(NSString *) blockDeviceIdentifier error:(NSError **) error;
```

## Discussion

Use [`validateBlockDeviceIdentifier(_:)`](./validateblockdeviceidentifier%28_%29.md) to validate an identifier string before trying to set the [`blockDeviceIdentifier`](./blockdeviceidentifier.md) property. The identifier must be an ASCII encodable string of 20 bytes or less.

## Parameters

- `blockDeviceIdentifier`: The device identifier to validate. In the case of an invalid identifier string, the method throws an error that describes why the device identifier isn’t valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioblockdeviceconfiguration/validateblockdeviceidentifier(_:))*