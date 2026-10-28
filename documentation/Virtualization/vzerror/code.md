# VZError.Code

**Framework**: Virtualization  
**Kind**: enum  
**Role**: Enumeration

Errors you might encounter when configuring or using a virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum Code
```

```c
enum VZErrorCode : NSInteger;
```

## Overview

The domain for these errors is [`VZErrorDomain`](../vzerrordomain.md). When an error originates in a different component, the [`NSError`](../../Foundation/nserror.md) object contains the domain of that component.

## Topics

### Error codes
- [VZError.Code.internalError](./code/internalerror.md)
  An internal error, such as the VM unexpectedly stopping.
- [VZError.Code.invalidVirtualMachineConfiguration](./code/invalidvirtualmachineconfiguration.md)
  An invalid configuration error.
- [VZError.Code.invalidVirtualMachineState](./code/invalidvirtualmachinestate.md)
  An invalid state error.
- [VZError.Code.invalidVirtualMachineStateTransition](./code/invalidvirtualmachinestatetransition.md)
  An invalid state transition error.
- [VZError.Code.invalidDiskImage](./code/invaliddiskimage.md)
  An invalid disk-image error.
- [VZError.Code.virtualMachineLimitExceeded](./code/virtualmachinelimitexceeded.md)
  Unable to create an additional VM.
- [VZError.Code.networkError](./code/networkerror.md)
  A network error, such as a failed connection error, occurred.
- [VZError.Code.notSupported](./code/notsupported.md)
  The host computer or operating system isn’t supported.
- [VZError.Code.outOfDiskSpace](./code/outofdiskspace.md)
  The host is out of disk space.
- [VZError.Code.operationCancelled](./code/operationcancelled.md)
  The code that indicates user canceled the installation of Rosetta or the app canceled the installation of a guest OS.
- [VZError.Code.installationFailed](./code/installationfailed.md)
  An error occurred during installation.
- [VZError.Code.installationRequiresUpdate](./code/installationrequiresupdate.md)
  The VM requires a software update in order to complete the installation.
- [VZError.Code.invalidRestoreImage](./code/invalidrestoreimage.md)
  The restore image is invalid.
- [VZError.Code.invalidRestoreImageCatalog](./code/invalidrestoreimagecatalog.md)
  The restore image catalog is invalid.
- [VZError.Code.noSupportedRestoreImagesInCatalog](./code/nosupportedrestoreimagesincatalog.md)
  The restore image catalog has no supported restore images.
- [VZError.Code.restoreImageCatalogLoadFailed](./code/restoreimagecatalogloadfailed.md)
  The restore image catalog failed to load.
- [VZError.Code.restoreImageLoadFailed](./code/restoreimageloadfailed.md)
  The restore image failed to load.
- [VZError.Code.networkBlockDeviceNegotiationFailed](./code/networkblockdevicenegotiationfailed.md)
  The connection or the negotiation with the network block device server failed.
- [VZError.Code.networkBlockDeviceDisconnected](./code/networkblockdevicedisconnected.md)
  The network block device client disconnected from the server.
- [VZError.Code.restore](./code/restore.md)
  The VM failed to restore from save file.
- [VZError.Code.save](./code/save.md)
  The VM failed to save to the save file.
- [VZError.Code.deviceAlreadyAttached](./code/devicealreadyattached.md)
  The device already has an attachment to the VM.
- [VZError.Code.deviceInitializationFailure](./code/deviceinitializationfailure.md)
  A device initialization failure.
- [VZError.Code.deviceNotFound](./code/devicenotfound.md)
  The framework can’t find the device.
- [VZError.Code.usbControllerNotFound](./code/usbcontrollernotfound.md)
  The framework can’t find the controller.
- [VZError.Code.internalError](./code/internalerror.md)
  An internal error, such as the VM unexpectedly stopping.
- [VZError.Code.invalidVirtualMachineConfiguration](./code/invalidvirtualmachineconfiguration.md)
  An invalid configuration error.
- [VZError.Code.invalidVirtualMachineState](./code/invalidvirtualmachinestate.md)
  An invalid state error.
- [VZError.Code.invalidVirtualMachineStateTransition](./code/invalidvirtualmachinestatetransition.md)
  An invalid state transition error.
- [VZError.Code.invalidDiskImage](./code/invaliddiskimage.md)
  An invalid disk-image error.
- [VZError.Code.virtualMachineLimitExceeded](./code/virtualmachinelimitexceeded.md)
  Unable to create an additional VM.
- [VZError.Code.networkError](./code/networkerror.md)
  A network error, such as a failed connection error, occurred.
- [VZError.Code.notSupported](./code/notsupported.md)
  The host computer or operating system isn’t supported.
- [VZError.Code.outOfDiskSpace](./code/outofdiskspace.md)
  The host is out of disk space.
- [VZError.Code.operationCancelled](./code/operationcancelled.md)
  The code that indicates user canceled the installation of Rosetta or the app canceled the installation of a guest OS.
- [VZError.Code.installationFailed](./code/installationfailed.md)
  An error occurred during installation.
- [VZError.Code.installationRequiresUpdate](./code/installationrequiresupdate.md)
  The VM requires a software update in order to complete the installation.
- [VZError.Code.invalidRestoreImage](./code/invalidrestoreimage.md)
  The restore image is invalid.
- [VZError.Code.invalidRestoreImageCatalog](./code/invalidrestoreimagecatalog.md)
  The restore image catalog is invalid.
- [VZError.Code.noSupportedRestoreImagesInCatalog](./code/nosupportedrestoreimagesincatalog.md)
  The restore image catalog has no supported restore images.
- [VZError.Code.restoreImageCatalogLoadFailed](./code/restoreimagecatalogloadfailed.md)
  The restore image catalog failed to load.
- [VZError.Code.restoreImageLoadFailed](./code/restoreimageloadfailed.md)
  The restore image failed to load.
- [VZError.Code.networkBlockDeviceNegotiationFailed](./code/networkblockdevicenegotiationfailed.md)
  The connection or the negotiation with the network block device server failed.
- [VZError.Code.networkBlockDeviceDisconnected](./code/networkblockdevicedisconnected.md)
  The network block device client disconnected from the server.
- [VZError.Code.restore](./code/restore.md)
  The VM failed to restore from save file.
- [VZError.Code.save](./code/save.md)
  The VM failed to save to the save file.
- [VZError.Code.deviceAlreadyAttached](./code/devicealreadyattached.md)
  The device already has an attachment to the VM.
- [VZError.Code.deviceInitializationFailure](./code/deviceinitializationfailure.md)
  A device initialization failure.
- [VZError.Code.deviceNotFound](./code/devicenotfound.md)
  The framework can’t find the device.
- [VZError.Code.usbControllerNotFound](./code/usbcontrollernotfound.md)
  The framework can’t find the controller.
### Enumeration Cases
- [VZError.Code.efiSecureBootEnrollmentFailed](./code/efisecurebootenrollmentfailed.md)
  An error that indicates the Secure Boot signatures failed to enroll.
- [VZError.Code.efiVariableInaccessible](./code/efivariableinaccessible.md)
  An error that indicates the framework can’t access the EFI variable store.
- [VZError.Code.guestProvisioningInvalidFullName](./code/guestprovisioninginvalidfullname.md)
  An error that indicates the full name for guest provisioning is invalid.
- [VZError.Code.guestProvisioningInvalidPassword](./code/guestprovisioninginvalidpassword.md)
  An error that indicates the password for guest provisioning is invalid.
- [VZError.Code.guestProvisioningInvalidUsername](./code/guestprovisioninginvalidusername.md)
  An error that indicates the username for guest provisioning is invalid.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the error codes
- [static var internalError: VZError.Code](./internalerror.md)
  An internal error occurred.
- [static var invalidVirtualMachineConfiguration: VZError.Code](./invalidvirtualmachineconfiguration.md)
  An invalid configuration error.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzerror/code)*