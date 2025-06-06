# VZError.Code.outOfDiskSpace

**Framework**: Virtualization  
**Kind**: case

The host is out of disk space.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case outOfDiskSpace
```

## See Also

- [VZError.Code.internalError](vzerror/code/internalerror.md)
  An internal error, such as the VM unexpectedly stopping.
- [VZError.Code.invalidVirtualMachineConfiguration](vzerror/code/invalidvirtualmachineconfiguration.md)
  An invalid configuration error.
- [VZError.Code.invalidVirtualMachineState](vzerror/code/invalidvirtualmachinestate.md)
  An invalid state error.
- [VZError.Code.invalidVirtualMachineStateTransition](vzerror/code/invalidvirtualmachinestatetransition.md)
  An invalid state transition error.
- [VZError.Code.invalidDiskImage](vzerror/code/invaliddiskimage.md)
  An invalid disk-image error.
- [VZError.Code.virtualMachineLimitExceeded](vzerror/code/virtualmachinelimitexceeded.md)
  Unable to create an additional VM.
- [VZError.Code.networkError](vzerror/code/networkerror.md)
  A network error, such as a failed connection error, occurred.
- [VZError.Code.notSupported](vzerror/code/notsupported.md)
  The host computer or operating system isn’t supported.
- [VZError.Code.operationCancelled](vzerror/code/operationcancelled.md)
  The code that indicates user canceled the installation of Rosetta or the app canceled the installation of a guest OS.
- [VZError.Code.installationFailed](vzerror/code/installationfailed.md)
  An error occurred during installation.
- [VZError.Code.installationRequiresUpdate](vzerror/code/installationrequiresupdate.md)
  The VM requires a software update in order to complete the installation.
- [VZError.Code.invalidRestoreImage](vzerror/code/invalidrestoreimage.md)
  The restore image is invalid.
- [VZError.Code.invalidRestoreImageCatalog](vzerror/code/invalidrestoreimagecatalog.md)
  The restore image catalog is invalid.
- [VZError.Code.noSupportedRestoreImagesInCatalog](vzerror/code/nosupportedrestoreimagesincatalog.md)
  The restore image catalog has no supported restore images.
- [VZError.Code.restoreImageCatalogLoadFailed](vzerror/code/restoreimagecatalogloadfailed.md)
  The restore image catalog failed to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzerror/code/outofdiskspace)*