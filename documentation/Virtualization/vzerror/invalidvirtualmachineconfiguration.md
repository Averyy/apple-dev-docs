# invalidVirtualMachineConfiguration

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

An invalid configuration error.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static var invalidVirtualMachineConfiguration: VZError.Code { get }
```

#### Discussion

This error indicates that your [`VZVirtualMachineConfiguration`](../vzvirtualmachineconfiguration.md) object contains invalid data.

## See Also

### Getting the error codes
- [static var internalError: VZError.Code](./internalerror.md)
  An internal error occurred.
- [static var invalidVirtualMachineState: VZError.Code](./invalidvirtualmachinestate.md)
  An invalid state error.
- [static var invalidVirtualMachineStateTransition: VZError.Code](./invalidvirtualmachinestatetransition.md)
  An invalid state transition error.
- [static var invalidDiskImage: VZError.Code](./invaliddiskimage.md)
  An invalid disk-image error.
- [static var networkError: VZError.Code](./networkerror.md)
  A network error, such as a failed connection.
- [static var notSupported: VZError.Code](./notsupported.md)
  The operation isn’t supported.
- [static var outOfDiskSpace: VZError.Code](./outofdiskspace.md)
  The host is out of disk space.
- [static var operationCancelled: VZError.Code](./operationcancelled.md)
  The user canceled the installation of Rosetta or the app canceled the installation of a guest OS.
- [static var installationFailed: VZError.Code](./installationfailed.md)
  An error occurred during installation.
- [static var installationRequiresUpdate: VZError.Code](./installationrequiresupdate.md)
  The framework canceled the installation because the host requires a software update in order to complete the installation.
- [static var invalidRestoreImage: VZError.Code](./invalidrestoreimage.md)
  The restore image is invalid.
- [static var invalidRestoreImageCatalog: VZError.Code](./invalidrestoreimagecatalog.md)
  The restore image catalog is invalid.
- [static var noSupportedRestoreImagesInCatalog: VZError.Code](./nosupportedrestoreimagesincatalog.md)
  The restore image catalog has no supported restore images.
- [static var restoreImageCatalogLoadFailed: VZError.Code](./restoreimagecatalogloadfailed.md)
  The restore image catalog failed to load.
- [static var restoreImageLoadFailed: VZError.Code](./restoreimageloadfailed.md)
  The restore image failed to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzerror/invalidvirtualmachineconfiguration)*