# IOServiceOrdering

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
SInt32 IOServiceOrdering(const OSMetaClassBase *inObj1, const OSMetaClassBase *inObj2, void *ref);
```

## See Also

### Utilities
- [IOFixedDivide](./api-1575297-iofixeddivide.md)
- [IOFixedMultiply](./api-1575302-iofixedmultiply.md)
- [IOAlignmentToSize](./api-1575292-ioalignmenttosize.md)
- [IOSizeToAlignment](./api-1575319-iosizetoalignment.md)
- [OSSynchronizeIO](./api-1576454-ossynchronizeio.md)
  The OSSynchronizeIO routine ensures orderly load and store operations to noncached memory mapped I/O devices.
- [DriverDescription](./driverdescription.md)
- [DriverOSRuntime](./driverosruntime.md)
- [DriverOSService](./driverosservice.md)
- [DriverServiceInfo](./driverserviceinfo.md)
- [DriverType](./drivertype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532621-ioserviceordering)*