# attachment

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The attachment object that provides the underlying storage for the device.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var attachment: VZStorageDeviceAttachment { get }
```

```objc
@property (strong, readonly) VZStorageDeviceAttachment * attachment;
```

#### Discussion

The attachment object defines which local resource on the host computer appears as a disk in the virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzstoragedeviceconfiguration/attachment)*