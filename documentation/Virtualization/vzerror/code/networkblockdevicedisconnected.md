# VZError.Code.networkBlockDeviceDisconnected

**Framework**: Virtualization  
**Kind**: case  
**Role**: Case

The network block device client disconnected from the server.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case networkBlockDeviceDisconnected
```

```c
VZErrorNetworkBlockDeviceDisconnected
```

## See Also

### Error codes
- [VZError.Code.internalError](./internalerror.md)
  An internal error, such as the VM unexpectedly stopping.
- [VZError.Code.invalidVirtualMachineConfiguration](./invalidvirtualmachineconfiguration.md)
  An invalid configuration error.
- [VZError.Code.invalidVirtualMachineState](./invalidvirtualmachinestate.md)
  An invalid state error.
- [VZError.Code.invalidVirtualMachineStateTransition](./invalidvirtualmachinestatetransition.md)
  An invalid state transition error.
- [VZError.Code.invalidDiskImage](./invaliddiskimage.md)
  An invalid disk-image error.
- [VZError.Code.virtualMachineLimitExceeded](./virtualmachinelimitexceeded.md)
  Unable to create an additional VM.
- [VZError.Code.networkError](./networkerror.md)
  A network error, such as a failed connection error, occurred.
- [VZError.Code.notSupported](./notsupported.md)
  The host computer or operating system isn’t supported.
- [VZError.Code.outOfDiskSpace](./outofdiskspace.md)
  The host is out of disk space.
- [VZError.Code.operationCancelled](./operationcancelled.md)
  The code that indicates user canceled the installation of Rosetta or the app canceled the installation of a guest OS.
- [VZError.Code.installationFailed](./installationfailed.md)
  An error occurred during installation.
- [VZError.Code.installationRequiresUpdate](./installationrequiresupdate.md)
  The VM requires a software update in order to complete the installation.
- [VZError.Code.invalidRestoreImage](./invalidrestoreimage.md)
  The restore image is invalid.
- [VZError.Code.invalidRestoreImageCatalog](./invalidrestoreimagecatalog.md)
  The restore image catalog is invalid.
- [VZError.Code.noSupportedRestoreImagesInCatalog](./nosupportedrestoreimagesincatalog.md)
  The restore image catalog has no supported restore images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzerror/code/networkblockdevicedisconnected)*