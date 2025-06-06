# VZVirtualMachine

**Framework**: Virtualization  
**Kind**: class

An object that manages the overall state and configuration of your VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtualMachine
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)
- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)

#### Overview

A [`VZVirtualMachine`](vzvirtualmachine.md) object emulates a complete hardware machine of the same architecture as the underlying Mac computer. Use the VM to execute a guest operating system and any other apps you install. The VM manages the resources that the guest operating system uses, providing access to some hardware resources while emulating others.

Create and configure a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object with details about how you want to configure your VM, and use that object to create the [`VZVirtualMachine`](vzvirtualmachine.md) object. After creating the VM, call the [`start(completionHandler:)`](vzvirtualmachine/start(completionhandler:).md) method (Swift)  or the [`start()`](vzvirtualmachine/start().md) method (Objective-C) to start the VM and boot the guest operating system.

> ❗ **Important**:  The creation of a virtual machine requires your app to have the [`com.apple.security.virtualization`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.virtualization) entitlement.

 The creation of a virtual machine requires your app to have the [`com.apple.security.virtualization`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.virtualization) entitlement.

## Topics

### Creating the VM
- [convenience init(configuration: VZVirtualMachineConfiguration)](vzvirtualmachine/init(configuration:).md)
  Creates the VM and configures it with the specified data.
- [init(configuration: VZVirtualMachineConfiguration, queue: dispatch_queue_t)](vzvirtualmachine/init(configuration:queue:).md)
  Creates and configures the VM with the specified data and dispatch queue.
- [class var isSupported: Bool](vzvirtualmachine/issupported.md)
  A Boolean value that indicates whether the system supports virtualization.
### Responding to a stopped VM
- [var delegate: (any VZVirtualMachineDelegate)?](vzvirtualmachine/delegate.md)
  A custom object you use to determine when the VM stops.
- [protocol VZVirtualMachineDelegate](vzvirtualmachinedelegate.md)
  The methods you use to respond to changes in the state of the VM.
### Starting and stopping the VM
- [func start(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/start(completionhandler:).md)
  Starts the VM and notifies the specified completion handler if startup is successful.
- [func start() async throws](vzvirtualmachine/start.md)
  Starts the VM and notifies the specified completion handler if startup was successful.
- [func start(options: VZVirtualMachineStartOptions, completionHandler: ((any Error)?) -> Void)](vzvirtualmachine/start(options:completionhandler:).md)
  Starts the VM with the options and a completion handler you provide.
- [func stop(completionHandler: ((any Error)?) -> Void)](vzvirtualmachine/stop(completionhandler:).md)
  Stops a VM that’s in either a running or paused state.
- [func pause(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/pause(completionhandler:).md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func requestStop() throws](vzvirtualmachine/requeststop.md)
  Asks the guest operating system to stop running.
- [func resume(completionHandler: (Result<Void, any Error>) -> Void)](vzvirtualmachine/resume(completionhandler:).md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [func pause() async throws](vzvirtualmachine/pause.md)
  Pauses a running VM and notifies the specified completion handler of the results.
- [func resume() async throws](vzvirtualmachine/resume.md)
  Resumes a paused VM and notifies the specified completion handler of the results.
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.
### Configuring VM attributes at runtime
- [var consoleDevices: [VZConsoleDevice]](vzvirtualmachine/consoledevices.md)
  The list of configured console devices on the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDevice]](vzvirtualmachine/memoryballoondevices.md)
  The array of devices that you use to adjust the amount of memory available to the guest system.
- [var networkDevices: [VZNetworkDevice]](vzvirtualmachine/networkdevices.md)
  The list of configured network devices on the VM.
- [var socketDevices: [VZSocketDevice]](vzvirtualmachine/socketdevices.md)
  The array of socket devices that the VM configures for use ports in the guest VM.
- [var directorySharingDevices: [VZDirectorySharingDevice]](vzvirtualmachine/directorysharingdevices.md)
  The list of configured directory-sharing devices on the VM.
- [var usbControllers: [VZUSBController]](vzvirtualmachine/usbcontrollers.md)
  The list of runtime USB controller objects.
### Getting the state of the VM
- [var state: VZVirtualMachine.State](vzvirtualmachine/state-swift.property.md)
  The current execution state of the VM.
- [VZVirtualMachine.State](vzvirtualmachine/state-swift.enum.md)
  The execution states of the VM.
- [var graphicsDevices: [VZGraphicsDevice]](vzvirtualmachine/graphicsdevices.md)
  The list of configured graphics devices on the virtual machine.
- [var canStart: Bool](vzvirtualmachine/canstart.md)
  A Boolean value that indicates whether you can start the VM.
- [var canPause: Bool](vzvirtualmachine/canpause.md)
  A Boolean value that indicates whether you can pause the VM.
- [var canResume: Bool](vzvirtualmachine/canresume.md)
  A Boolean value that indicates whether you can resume the VM.
- [var canStop: Bool](vzvirtualmachine/canstop.md)
  A Boolean value that indicates whether you can stop the VM.
- [var canRequestStop: Bool](vzvirtualmachine/canrequeststop.md)
  A Boolean value that indicates whether you can ask the guest operating system to stop running.
### Saving and restoring the VM state
- [func saveMachineStateTo(url: URL, completionHandler: ((any Error)?) -> Void)](vzvirtualmachine/savemachinestateto(url:completionhandler:).md)
  Saves the state of a VM.
- [func restoreMachineStateFrom(url: URL, completionHandler: ((any Error)?) -> Void)](vzvirtualmachine/restoremachinestatefrom(url:completionhandler:).md)
  Restores a VM from a previously saved state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtualMachineView](vzvirtualmachineview.md)
  A view that allows user interaction with a VM.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine)*