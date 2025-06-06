# OSSynchronizeIO

**Framework**: Kernel  
**Kind**: func

The OSSynchronizeIO routine ensures orderly load and store operations to noncached memory mapped I/O devices.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void OSSynchronizeIO(void);
```

#### Discussion

The OSSynchronizeIO routine ensures orderly load and store operations to noncached memory mapped I/O devices. It executes the eieio instruction on PowerPC processors.

## See Also

- [IOServiceOrdering](1532621-ioserviceordering.md)
- [IOFixedDivide](1575297-iofixeddivide.md)
- [IOFixedMultiply](1575302-iofixedmultiply.md)
- [IOAlignmentToSize](1575292-ioalignmenttosize.md)
- [IOSizeToAlignment](1575319-iosizetoalignment.md)
- [DriverDescription](driverdescription.md)
- [DriverOSRuntime](driverosruntime.md)
- [DriverOSService](driverosservice.md)
- [DriverServiceInfo](driverserviceinfo.md)
- [DriverType](drivertype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576454-ossynchronizeio)*