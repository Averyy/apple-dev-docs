# Virtualization enumerations

**Framework**: Virtualization

Control the caching modes, disk synchronization, and macOS auxiliary storage options of VMs.

#### Overview

These are values you use to control aspects of the operation of the virtual drives for guest VMs and the auxiliary storage of macOS guest VMs.

## Topics

### Virtual disk image caching modes
- [enum VZDiskImageCachingMode](vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
### Virtual disk synchronization modes
- [enum VZDiskImageSynchronizationMode](vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.
- [enum VZDiskSynchronizationMode](vzdisksynchronizationmode.md)
  Values that describe the synchronization modes available to the guest OS.
### Mac-specific auxiliary storage options
- [VZMacAuxiliaryStorage.InitializationOptions](vzmacauxiliarystorage/initializationoptions.md)
  Options you can set when creating new auxiliary storage.
### Rosetta availability states
- [enum VZLinuxRosettaAvailability](vzlinuxrosettaavailability.md)
  Constants that describe the availability and installation status of Rosetta.
### Virtualization error codes
- [VZError.Code](vzerror/code.md)
  Errors you might encounter when configuring or using a virtual machine.
### VM states
- [VZVirtualMachine.State](vzvirtualmachine/state-swift.enum.md)
  The execution states of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/virtualization-enumerations)*