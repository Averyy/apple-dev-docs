# VZError

**Framework**: Virtualization  
**Kind**: struct

Errors that you might encounter when configuring or using a VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct VZError
```

#### Overview

The domain for these errors is [`VZErrorDomain`](vzerrordomain.md). When an error originates in a different component, the [`NSError`](https://developer.apple.com/documentation/foundation/nserror) object contains the domain of that component.

## Topics

### Getting the error codes
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
- [static var restoreImageLoadFailed: VZError.Code](vzerror/restoreimageloadfailed.md)
  The restore image failed to load.
- [static var restore: VZError.Code](vzerror/restore.md)
  The VM failed to restore from the save file.
- [static var save: VZError.Code](vzerror/save.md)
  The VM failed to save to the save file.
- [static var deviceAlreadyAttached: VZError.Code](vzerror/devicealreadyattached.md)
  The device already has an attachment to the VM.
- [static var deviceInitializationFailure: VZError.Code](vzerror/deviceinitializationfailure.md)
  A device initialization failure.
- [static var deviceNotFound: VZError.Code](vzerror/devicenotfound.md)
  The framework can’t find the device.
- [static var usbControllerNotFound: VZError.Code](vzerror/usbcontrollernotfound.md)
  The framework can’t find the controller.
- [static var efiSecureBootEnrollmentFailed: VZError.Code](vzerror/efisecurebootenrollmentfailed.md)
- [static var efiVariableInaccessible: VZError.Code](vzerror/efivariableinaccessible.md)
- [static var guestProvisioningInvalidFullName: VZError.Code](vzerror/guestprovisioninginvalidfullname.md)
- [static var guestProvisioningInvalidPassword: VZError.Code](vzerror/guestprovisioninginvalidpassword.md)
- [static var guestProvisioningInvalidUsername: VZError.Code](vzerror/guestprovisioninginvalidusername.md)
- [VZError.Code](vzerror/code.md)
  Errors you might encounter when configuring or using a virtual machine.
- [static var errorDomain: String](vzerror/errordomain.md)
### Accessing the error information
- [static var virtualMachineLimitExceeded: VZError.Code](vzerror/virtualmachinelimitexceeded.md)
  Returns an error code that indicates whether the system exceeded the limit on the number of running virtual machines.
### Type properties
- [static var networkBlockDeviceDisconnected: VZError.Code](vzerror/networkblockdevicedisconnected.md)
  Returns a value that indicates the connection state of the network block device.
- [static var networkBlockDeviceNegotiationFailed: VZError.Code](vzerror/networkblockdevicenegotiationfailed.md)
  Returns a value that indicates whether the network block device negotiation failed.

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let VZErrorDomain: String](vzerrordomain.md)
  The error domain for the Virtualization framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzerror)*