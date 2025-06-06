# VZLinuxRosettaDirectoryShare

**Framework**: Virtualization  
**Kind**: class

The Linux directory share for Rosetta.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZLinuxRosettaDirectoryShare
```

#### Overview

This directory share exposes the Rosetta directory from the host file system to the guest. The example below shows the process of creating a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md), and then associating the Rosetta directory share with the VM configuration.

```swift
let tag = "EXAMPLE_TAG"  
let configuration = VZVirtualMachineConfiguration()
do {
    try let validationError = VZVirtioFileSystemDeviceConfiguration.validateTag(tag)
    let rosettaDirectoryShare = try VZLinuxRosettaDirectoryShare()
    let fileSystemDevice = VZVirtioFileSystemDeviceConfiguration(tag: tag)
    fileSystemDevice.share = rosettaDirectoryShare

    configuration.directorySharingDevices = [ fileSystemDevice ]
} catch VZError.invalidVirtualMachineConfiguration {
    // Rosetta is unavailable.
}
```

For complete instructions on installing Rosetta see [`Running Intel Binaries in Linux VMs with Rosetta`](running-intel-binaries-in-linux-vms-with-rosetta.md), which includes additional information about checking for Rosetta availability, mounting the directory share, and registering the Rosetta runtime binary to run Intel binaries in a guest VM.

For information on using a custom kernel to enhance Rosetta performance, see [`Accelerating the performance of Rosetta`](accelerating-the-performance-of-rosetta.md).

## Topics

### Creating a Rosetta directory share
- [init() throws](vzlinuxrosettadirectoryshare/init.md)
  Creates a new Rosetta directory share, or returns an error if Rosetta isn’t installed.
### Checking Rosetta availability
- [class var availability: VZLinuxRosettaAvailability](vzlinuxrosettadirectoryshare/availability.md)
  A value that indicates the current state of Rosetta’s availability.
- [enum VZLinuxRosettaAvailability](vzlinuxrosettaavailability.md)
  Constants that describe the availability and installation status of Rosetta.
### Installing Rosetta
- [class func installRosetta(completionHandler: ((any Error)?) -> Void)](vzlinuxrosettadirectoryshare/installrosetta(completionhandler:).md)
  Starts the installation of Rosetta.
### Setting the ahead of time (AOT) caching options
- [var cachingOptions: VZLinuxRosettaDirectoryShare.CachingOptions?](vzlinuxrosettadirectoryshare/cachingoptions-swift.property.md)
  The value that enables translation caching and configures the socket communication type for Rosetta.
- [func setCachingOptions(VZLinuxRosettaDirectoryShare.CachingOptions?) throws](vzlinuxrosettadirectoryshare/setcachingoptions(_:).md)
  Sets the Rosetta caching options using the options you specify.
- [VZLinuxRosettaDirectoryShare.CachingOptions](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum.md)
  Socket values you specify to configure Rosetta’s caching capabilities.

## Relationships

### Inherits From
- [VZDirectoryShare](vzdirectoryshare.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZDirectorySharingDeviceConfiguration](vzdirectorysharingdeviceconfiguration.md)
  The base class for a directory sharing device configuration.
- [class VZSharedDirectory](vzshareddirectory.md)
  A directory on the host that you can expose to a guest.
- [class VZSingleDirectoryShare](vzsingledirectoryshare.md)
  An object that defines the directory share for a single directory.
- [class VZMultipleDirectoryShare](vzmultipledirectoryshare.md)
  An object that describes a directory share for multiple directories.
- [class VZVirtualMachine](vzvirtualmachine.md)
  An object that manages the overall state and configuration of your VM.
- [class VZVirtualMachineView](vzvirtualmachineview.md)
  A view that allows user interaction with a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare)*