# VZError.Code

**Framework**: Virtualization  
**Kind**: enum

Errors you might encounter when configuring or using a virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum Code
```

#### Overview

The domain for these errors is [`VZErrorDomain`](vzerrordomain.md). When an error originates in a different component, the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object contains the domain of that component.

## Topics

### Error codes
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
- [VZError.Code.outOfDiskSpace](vzerror/code/outofdiskspace.md)
  The host is out of disk space.
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
- [VZError.Code.restoreImageLoadFailed](vzerror/code/restoreimageloadfailed.md)
  The restore image failed to load.
- [VZError.Code.networkBlockDeviceNegotiationFailed](vzerror/code/networkblockdevicenegotiationfailed.md)
  The connection or the negotiation with the network block device server failed.
- [VZError.Code.networkBlockDeviceDisconnected](vzerror/code/networkblockdevicedisconnected.md)
  The network block device client disconnected from the server.
- [VZError.Code.restore](vzerror/code/restore.md)
  The VM failed to restore from save file.
- [VZError.Code.save](vzerror/code/save.md)
  The VM failed to save to the save file.
- [VZError.Code.deviceAlreadyAttached](vzerror/code/devicealreadyattached.md)
  The device already has an attachment to the VM.
- [VZError.Code.deviceInitializationFailure](vzerror/code/deviceinitializationfailure.md)
  A device initialization failure.
- [VZError.Code.deviceNotFound](vzerror/code/devicenotfound.md)
  The framework can’t find the device.
- [VZError.Code.usbControllerNotFound](vzerror/code/usbcontrollernotfound.md)
  The framework can’t find the controller.
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
- [VZError.Code.outOfDiskSpace](vzerror/code/outofdiskspace.md)
  The host is out of disk space.
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
- [VZError.Code.restoreImageLoadFailed](vzerror/code/restoreimageloadfailed.md)
  The restore image failed to load.
- [VZError.Code.networkBlockDeviceNegotiationFailed](vzerror/code/networkblockdevicenegotiationfailed.md)
  The connection or the negotiation with the network block device server failed.
- [VZError.Code.networkBlockDeviceDisconnected](vzerror/code/networkblockdevicedisconnected.md)
  The network block device client disconnected from the server.
- [VZError.Code.restore](vzerror/code/restore.md)
  The VM failed to restore from save file.
- [VZError.Code.save](vzerror/code/save.md)
  The VM failed to save to the save file.
- [VZError.Code.deviceAlreadyAttached](vzerror/code/devicealreadyattached.md)
  The device already has an attachment to the VM.
- [VZError.Code.deviceInitializationFailure](vzerror/code/deviceinitializationfailure.md)
  A device initialization failure.
- [VZError.Code.deviceNotFound](vzerror/code/devicenotfound.md)
  The framework can’t find the device.
- [VZError.Code.usbControllerNotFound](vzerror/code/usbcontrollernotfound.md)
  The framework can’t find the controller.
### Initializers
- [init?(rawValue: Int)](vzerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzerror/code)*