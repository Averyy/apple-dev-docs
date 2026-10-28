# OSSynchronizeIO

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

The OSSynchronizeIO routine ensures orderly load and store operations to noncached memory mapped I/O devices.

**Availability**:
- macOS 10.0+

## Declaration

```c
void OSSynchronizeIO(void);
```

## Discussion

The OSSynchronizeIO routine ensures orderly load and store operations to noncached memory mapped I/O devices. It executes the eieio instruction on PowerPC processors.

## See Also

### Utilities
- [IOServiceOrdering](./api-1532621-ioserviceordering.md)
- [IOFixedDivide](./api-1575297-iofixeddivide.md)
- [IOFixedMultiply](./api-1575302-iofixedmultiply.md)
- [IOAlignmentToSize](./api-1575292-ioalignmenttosize.md)
- [IOSizeToAlignment](./api-1575319-iosizetoalignment.md)
- [DriverDescription](./driverdescription.md)
- [DriverOSRuntime](./driverosruntime.md)
- [DriverOSService](./driverosservice.md)
- [DriverServiceInfo](./driverserviceinfo.md)
- [DriverType](./drivertype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576454-ossynchronizeio)*