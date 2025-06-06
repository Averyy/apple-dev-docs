# restoreImageLoadFailed

**Framework**: Virtualization  
**Kind**: property

The restore image failed to load.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var restoreImageLoadFailed: VZError.Code { get }
```

## See Also

- [static var internalError: VZError.Code](vzerror/internalerror.md)
  An internal error occurred.
- [static var invalidVirtualMachineConfiguration: VZError.Code](vzerror/invalidvirtualmachineconfiguration.md)
  An invalid configuration error.
- [static var invalidVirtualMachineState: VZError.Code](vzerror/invalidvirtualmachinestate.md)
  An invalid state error.
- [static var invalidVirtualMachineStateTransition: VZError.Code](vzerror/invalidvirtualmachinestatetransition.md)
  An invalid state transition error.
- [static var invalidDiskImage: VZError.Code](vzerror/invaliddiskimage.md)
  An invalid disk-image error.
- [static var networkError: VZError.Code](vzerror/networkerror.md)
  A network error, such as a failed connection.
- [static var notSupported: VZError.Code](vzerror/notsupported.md)
  The operation isn’t supported.
- [static var outOfDiskSpace: VZError.Code](vzerror/outofdiskspace.md)
  The host is out of disk space.
- [static var operationCancelled: VZError.Code](vzerror/operationcancelled.md)
  The user canceled the installation of Rosetta or the app canceled the installation of a guest OS.
- [static var installationFailed: VZError.Code](vzerror/installationfailed.md)
  An error occurred during installation.
- [static var installationRequiresUpdate: VZError.Code](vzerror/installationrequiresupdate.md)
  The framework canceled the installation because the host requires a software update in order to complete the installation.
- [static var invalidRestoreImage: VZError.Code](vzerror/invalidrestoreimage.md)
  The restore image is invalid.
- [static var invalidRestoreImageCatalog: VZError.Code](vzerror/invalidrestoreimagecatalog.md)
  The restore image catalog is invalid.
- [static var noSupportedRestoreImagesInCatalog: VZError.Code](vzerror/nosupportedrestoreimagesincatalog.md)
  The restore image catalog has no supported restore images.
- [static var restoreImageCatalogLoadFailed: VZError.Code](vzerror/restoreimagecatalogloadfailed.md)
  The restore image catalog failed to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzerror/restoreimageloadfailed)*