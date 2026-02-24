# Running macOS in a virtual machine on Apple silicon

**Framework**: Virtualization

Install and run macOS in a virtual machine using the Virtualization framework.

**Availability**:
- macOS 14.0+
- Xcode 26.0+

#### Overview

This sample code project demonstrates how to install and run macOS virtual machines (VMs) on Apple silicon. The Xcode project includes two separate apps:

- `InstallationTool`, a command line utility that installs macOS from a restore image, which is a file with a `.ipsw` file extension, onto a VM. You can use this tool to download the restore image of the most current macOS release from the network, or with your own restore image. The utility creates a VM bundle and stores the resulting VM images in your Home directory.
- `macOSVirtualMachineSampleApp` is a Mac app that runs the macOS VM that `InstallationTool` installs. You use `macOSVirtualMachineSampleApp` to launch and control the macOS VM that loads and runs macOS from the VM bundle. This app includes entitlements to enable it to use Virtualization and access the VM’s’ audio input, such as the microphone.

There are four build targets in this project that represent the `InstallationTool` and the `macOSVirtualMachineSampleApp`, one set of targets each for Swift and Objective-C versions of the apps. You can use either version, they’re functionally identical.

> **Note**: The default deployment target is macOS 14. If you need to build for an earlier version of macOS, you need to change the deployment target as appropriate.

##### Configure the Sample Code Project

You need to install the virtual machine, and `VM.bundle` needs exist before launching the sample app.

1. Set up code signing for each of the project’s targets by navigating to the Signing & Capabilities settings and selecting your team from the drop-down menu.
2. Run `InstallationTool` from within Xcode or in Terminal to download the latest available macOS restore image from the network and create a macOS VM image on disk. `InstallationTool` creates a `VM.bundle` package in your Home directory, containing: - `Disk.img` — The main disk image of the installed OS.
- `AuxiliaryStorage` — The auxiliary storage for macOS.
- `MachineIdentifier` — The data representation of the `VZMacMachineIdentifier` object.
- `HardwareModel` — The data representation of the `VZMacHardwareModel` object.
- `RestoreImage.ipsw` — The restore image downloaded from the network (this file exists only if the tool runs without arguments).
3. Launch `macOSVirtualMachineSampleApp` to run the macOS guest operating system. The sample app starts the VM and configures a graphical view that you interact with. The virtual Mac continues running until you shut it down from inside the guest OS, or quit the app. To reinstall the virtual machine, delete the `VM.bundle` package and run `InstallationTool` again.

##### Install Macos From a Restore Image

After downloading a restore image, you can install macOS from that restore image.

**Swift**:

```swift
let installer = VZMacOSInstaller(virtualMachine: virtualMachine, restoringFromImageAt: restoreImageURL)

NSLog("Starting installation.")
installer.install(completionHandler: { (result: Result<Void, Error>) in
    if case let .failure(error) = result {
        fatalError(error.localizedDescription)
    } else {
        NSLog("Installation succeeded.")
    }
})

// Observe installation progress.
installationObserver = installer.progress.observe(\.fractionCompleted, options: [.initial, .new]) { (progress, change) in
    NSLog("Installation progress: \(change.newValue! * 100).")
}
```

**Objective-C**:

```objective-c
VZMacOSInstaller *installer = [[VZMacOSInstaller alloc] initWithVirtualMachine:self->_virtualMachine restoreImageURL:restoreImageFileURL];

NSLog(@"Starting installation.");
[installer installWithCompletionHandler:^(NSError *error) {
    if (error) {
        abortWithErrorMessage([NSString stringWithFormat:@"%@", error.localizedDescription]);
    } else {
        NSLog(@"Installation succeeded.");
    }
}];

[installer.progress addObserver:self forKeyPath:@"fractionCompleted" options:NSKeyValueObservingOptionInitial | NSKeyValueObservingOptionNew context:nil];
```

##### Set Up the Virtual Machine

The sample app uses a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object to configure the basic characteristics of the guest, such as the CPU count, memory size, various device configurations, and a [`VZMacOSBootLoader`](vzmacosbootloader.md) object to load the operating system from the disk image, as the following example shows:

**Swift**:

```swift
let virtualMachineConfiguration = VZVirtualMachineConfiguration()

virtualMachineConfiguration.platform = createMacPlaform()
virtualMachineConfiguration.bootLoader = MacOSVirtualMachineConfigurationHelper.createBootLoader()
virtualMachineConfiguration.cpuCount = MacOSVirtualMachineConfigurationHelper.computeCPUCount()
virtualMachineConfiguration.memorySize = MacOSVirtualMachineConfigurationHelper.computeMemorySize()

virtualMachineConfiguration.audioDevices = [MacOSVirtualMachineConfigurationHelper.createSoundDeviceConfiguration()]
virtualMachineConfiguration.graphicsDevices = [MacOSVirtualMachineConfigurationHelper.createGraphicsDeviceConfiguration()]
virtualMachineConfiguration.networkDevices = [MacOSVirtualMachineConfigurationHelper.createNetworkDeviceConfiguration()]
virtualMachineConfiguration.storageDevices = [MacOSVirtualMachineConfigurationHelper.createBlockDeviceConfiguration()]

virtualMachineConfiguration.pointingDevices = [MacOSVirtualMachineConfigurationHelper.createPointingDeviceConfiguration()]
virtualMachineConfiguration.keyboards = [MacOSVirtualMachineConfigurationHelper.createKeyboardConfiguration()]

try! virtualMachineConfiguration.validate()

if #available(macOS 14.0, *) {
    try! virtualMachineConfiguration.validateSaveRestoreSupport()
}

virtualMachine = VZVirtualMachine(configuration: virtualMachineConfiguration)
```

**Objective-C**:

```objective-c
VZVirtualMachineConfiguration *configuration = [VZVirtualMachineConfiguration new];

configuration.platform = [self createMacPlatformConfiguration];
configuration.CPUCount = [MacOSVirtualMachineConfigurationHelper computeCPUCount];
configuration.memorySize = [MacOSVirtualMachineConfigurationHelper computeMemorySize];

configuration.bootLoader = [MacOSVirtualMachineConfigurationHelper createBootLoader];

configuration.audioDevices = @[ [MacOSVirtualMachineConfigurationHelper createSoundDeviceConfiguration] ];
configuration.graphicsDevices = @[ [MacOSVirtualMachineConfigurationHelper createGraphicsDeviceConfiguration] ];
configuration.networkDevices = @[ [MacOSVirtualMachineConfigurationHelper createNetworkDeviceConfiguration] ];
configuration.storageDevices = @[ [MacOSVirtualMachineConfigurationHelper createBlockDeviceConfiguration] ];

configuration.pointingDevices = @[ [MacOSVirtualMachineConfigurationHelper createPointingDeviceConfiguration] ];
configuration.keyboards = @[ [MacOSVirtualMachineConfigurationHelper createKeyboardConfiguration] ];

BOOL isValidConfiguration = [configuration validateWithError:nil];
if (!isValidConfiguration) {
    @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Invalid configuration" userInfo:nil];
}

if (@available(macOS 14.0, *)) {
    BOOL supportsSaveRestore = [configuration validateSaveRestoreSupportWithError:nil];
    if (!supportsSaveRestore) {
        @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Invalid configuration" userInfo:nil];
    }
}

_virtualMachine = [[VZVirtualMachine alloc] initWithConfiguration:configuration];
```

Inside the `createVirtualMachine` method, the app also creates a platform configuration for the VM. [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) configures important macOS-specific data that the macOS guest needs to run, including the specific [`hardwareModel`](vzmacosconfigurationrequirements/hardwaremodel.md) that the image supports, as well as a [`machineIdentifier`](vzmacplatformconfiguration/machineidentifier.md) that uniquely identifies the current VM instance and differentiates it from any others.

**Swift**:

```swift
let macPlatform = VZMacPlatformConfiguration()

let auxiliaryStorage = VZMacAuxiliaryStorage(contentsOf: auxiliaryStorageURL)
macPlatform.auxiliaryStorage = auxiliaryStorage

if !FileManager.default.fileExists(atPath: vmBundlePath) {
    fatalError("Missing Virtual Machine Bundle at \(vmBundlePath). Run InstallationTool first to create it.")
}

// Retrieve the hardware model and save this value to disk
// during installation.
guard let hardwareModelData = try? Data(contentsOf: hardwareModelURL) else {
    fatalError("Failed to retrieve hardware model data.")
}

guard let hardwareModel = VZMacHardwareModel(dataRepresentation: hardwareModelData) else {
    fatalError("Failed to create hardware model.")
}

if !hardwareModel.isSupported {
    fatalError("The hardware model isn't supported on the current host")
}
macPlatform.hardwareModel = hardwareModel

// Retrieve the machine identifier and save this value to disk
// during installation.
guard let machineIdentifierData = try? Data(contentsOf: machineIdentifierURL) else {
    fatalError("Failed to retrieve machine identifier data.")
}

guard let machineIdentifier = VZMacMachineIdentifier(dataRepresentation: machineIdentifierData) else {
    fatalError("Failed to create machine identifier.")
}
macPlatform.machineIdentifier = machineIdentifier
```

**Objective-C**:

```objective-c
VZMacPlatformConfiguration *macPlatformConfiguration = [[VZMacPlatformConfiguration alloc] init];
VZMacAuxiliaryStorage *auxiliaryStorage = [[VZMacAuxiliaryStorage alloc] initWithContentsOfURL:getAuxiliaryStorageURL()];
macPlatformConfiguration.auxiliaryStorage = auxiliaryStorage;

if (![[NSFileManager defaultManager] fileExistsAtPath:getVMBundlePath()]) {
    abortWithErrorMessage([NSString stringWithFormat:@"Missing Virtual Machine Bundle at %@. Run InstallationTool first to create it.", getVMBundlePath()]);
}

// Retrieve the hardware model and save this value to disk during installation.
NSData *hardwareModelData = [[NSData alloc] initWithContentsOfURL:getHardwareModelURL()];
if (!hardwareModelData) {
    abortWithErrorMessage(@"Failed to retrieve hardware model data.");
}

VZMacHardwareModel *hardwareModel = [[VZMacHardwareModel alloc] initWithDataRepresentation:hardwareModelData];
if (!hardwareModel) {
    abortWithErrorMessage(@"Failed to create hardware model.");
}

if (!hardwareModel.supported) {
    abortWithErrorMessage(@"The hardware model isn't supported on the current host");
}
macPlatformConfiguration.hardwareModel = hardwareModel;

// Retrieve the machine identifier and save this value to disk
// during installation.
NSData *machineIdentifierData = [[NSData alloc] initWithContentsOfURL:getMachineIdentifierURL()];
if (!machineIdentifierData) {
    abortWithErrorMessage(@"Failed to retrieve machine identifier data.");
}

VZMacMachineIdentifier *machineIdentifier = [[VZMacMachineIdentifier alloc] initWithDataRepresentation:machineIdentifierData];
if (!machineIdentifier) {
    abortWithErrorMessage(@"Failed to create machine identifier.");
}
macPlatformConfiguration.machineIdentifier = machineIdentifier;
```

After creating the platform configuration, the app creates an instance of  [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) and adds video, virtual drives, and other devices to the system.

**Swift**:

```swift
let virtualMachineConfiguration = VZVirtualMachineConfiguration()

virtualMachineConfiguration.platform = createMacPlatformConfiguration(macOSConfiguration: macOSConfiguration)
virtualMachineConfiguration.cpuCount = MacOSVirtualMachineConfigurationHelper.computeCPUCount()
if virtualMachineConfiguration.cpuCount < macOSConfiguration.minimumSupportedCPUCount {
    fatalError("CPUCount isn't supported by the macOS configuration.")
}

virtualMachineConfiguration.memorySize = MacOSVirtualMachineConfigurationHelper.computeMemorySize()
if virtualMachineConfiguration.memorySize < macOSConfiguration.minimumSupportedMemorySize {
    fatalError("memorySize isn't supported by the macOS configuration.")
}

// Create a 128 GB disk image.
createDiskImage()

virtualMachineConfiguration.bootLoader = MacOSVirtualMachineConfigurationHelper.createBootLoader()

virtualMachineConfiguration.audioDevices = [MacOSVirtualMachineConfigurationHelper.createSoundDeviceConfiguration()]
virtualMachineConfiguration.graphicsDevices = [MacOSVirtualMachineConfigurationHelper.createGraphicsDeviceConfiguration()]
virtualMachineConfiguration.networkDevices = [MacOSVirtualMachineConfigurationHelper.createNetworkDeviceConfiguration()]
virtualMachineConfiguration.storageDevices = [MacOSVirtualMachineConfigurationHelper.createBlockDeviceConfiguration()]

virtualMachineConfiguration.pointingDevices = [MacOSVirtualMachineConfigurationHelper.createPointingDeviceConfiguration()]
virtualMachineConfiguration.keyboards = [MacOSVirtualMachineConfigurationHelper.createKeyboardConfiguration()]

try! virtualMachineConfiguration.validate()

if #available(macOS 14.0, *) {
    try! virtualMachineConfiguration.validateSaveRestoreSupport()
}

virtualMachine = VZVirtualMachine(configuration: virtualMachineConfiguration)
virtualMachineResponder = MacOSVirtualMachineDelegate()
virtualMachine.delegate = virtualMachineResponder
```

**Objective-C**:

```objective-c
VZVirtualMachineConfiguration *configuration = [VZVirtualMachineConfiguration new];

configuration.platform = [self createMacPlatformConfiguration:macOSConfiguration];
assert(configuration.platform);

configuration.CPUCount = [MacOSVirtualMachineConfigurationHelper computeCPUCount];
if (configuration.CPUCount < macOSConfiguration.minimumSupportedCPUCount) {
   abortWithErrorMessage(@"CPUCount is not supported by the macOS configuration.");
}

configuration.memorySize = [MacOSVirtualMachineConfigurationHelper computeMemorySize];
if (configuration.memorySize < macOSConfiguration.minimumSupportedMemorySize) {
   abortWithErrorMessage(@"memorySize is not supported by the macOS configuration.");
}

// Create a 128 GB disk image.
createDiskImage();

configuration.bootLoader = [MacOSVirtualMachineConfigurationHelper createBootLoader];

configuration.audioDevices = @[ [MacOSVirtualMachineConfigurationHelper createSoundDeviceConfiguration] ];
configuration.graphicsDevices = @[ [MacOSVirtualMachineConfigurationHelper createGraphicsDeviceConfiguration] ];
configuration.networkDevices = @[ [MacOSVirtualMachineConfigurationHelper createNetworkDeviceConfiguration] ];
configuration.storageDevices = @[ [MacOSVirtualMachineConfigurationHelper createBlockDeviceConfiguration] ];

configuration.pointingDevices = @[ [MacOSVirtualMachineConfigurationHelper createPointingDeviceConfiguration] ];
configuration.keyboards = @[ [MacOSVirtualMachineConfigurationHelper createKeyboardConfiguration] ];

BOOL isValidConfiguration = [configuration validateWithError:nil];
if (!isValidConfiguration) {
   @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Invalid configuration" userInfo:nil];
}

if (@available(macOS 14.0, *)) {
   BOOL supportsSaveRestore = [configuration validateSaveRestoreSupportWithError:nil];
   if (!supportsSaveRestore) {
       @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Invalid configuration" userInfo:nil];
   }
}

self->_virtualMachine = [[VZVirtualMachine alloc] initWithConfiguration:configuration];
self->_delegate = [MacOSVirtualMachineDelegate new];
self->_virtualMachine.delegate = self->_delegate;
```

The Virtualization framework checks the configuration to make sure it supports saving and restoring.

##### Start the Vm

After building the configuration data for the VM, the sample app uses the [`VZVirtualMachine`](vzvirtualmachine.md) object to start the execution of the macOS guest operating system.

Before calling the [`start(completionHandler:)`](vzvirtualmachine/start(completionhandler:).md) or [`restoreMachineStateFrom(url:completionHandler:)`](vzvirtualmachine/restoremachinestatefrom(url:completionhandler:).md) methods, the sample app configures a delegate object to receive messages about the state of the virtual machine. When the macOS guest operating system shuts down, the virtual machine calls the delegate’s [`guestDidStop(_:)`](vzvirtualmachinedelegate/guestdidstop(_:).md) method. In response, the delegate method prints a message and exits the app. If the macOS guest stops for any reason other than a normal shutdown, the delegate prints an error message and the app exits.

**Swift**:

```swift
DispatchQueue.main.async { [self] in
    createVirtualMachine()
    virtualMachineResponder = MacOSVirtualMachineDelegate()
    virtualMachine.delegate = virtualMachineResponder
    virtualMachineView.virtualMachine = virtualMachine
    virtualMachineView.capturesSystemKeys = true

    if #available(macOS 14.0, *) {
        // Configure the app to automatically respond to changes in the display size.
        virtualMachineView.automaticallyReconfiguresDisplay = true
    }

    if #available(macOS 14.0, *) {
        let fileManager = FileManager.default
        if fileManager.fileExists(atPath: saveFileURL.path) {
            restoreVirtualMachine()
        } else {
            startVirtualMachine()
        }
    } else {
        startVirtualMachine()
    }
}
```

**Objective-C**:

```objective-c
dispatch_async(dispatch_get_main_queue(), ^{
    [self createVirtualMachine];

    self->_delegate = [MacOSVirtualMachineDelegate new];
    self->_virtualMachine.delegate = self->_delegate;
    self->_virtualMachineView.virtualMachine = self->_virtualMachine;
    self->_virtualMachineView.capturesSystemKeys = YES;

    if (@available(macOS 14.0, *)) {
        // Configure the app to automatically respond to changes in the display size.
        self->_virtualMachineView.automaticallyReconfiguresDisplay = YES;
    }

    if (@available(macOS 14.0, *)) {
        NSFileManager *fileManager = [NSFileManager defaultManager];
        if ([fileManager fileExistsAtPath:getSaveFileURL().path]) {
            [self restoreVirtualMachine];
        } else {
            [self startVirtualMachine];
        }
    } else {
        [self startVirtualMachine];
    }
});
```

If the virtual machine was running when the sample app last exited, the app calls `restoreVirtualMachine` to restore the state. If the virtual machine was in a shutdown state, the app calls `startVirtualMachine` to reboot the machine. Both methods start the VM asynchronously in the background. The VM loads the system image and boots macOS. After macOS starts, the user interacts with a [`VZVirtualMachineView`](vzvirtualmachineview.md) window that displays the macOS UI and handles keyboard and mouse input through a [`VZMacGraphicsDeviceConfiguration`](vzmacgraphicsdeviceconfiguration.md) as though the user is interacting directly with the Mac hardware. The `VZVirtualMachineView` automatically resizes the virtual machine display when window size changes, and to capture system keys such, as the Globe key on a Mac keyboard.

The `startVirtualMachine` method calls the VM’s [`start(completionHandler:)`](vzvirtualmachine/start(completionhandler:).md) method.

**Swift**:

```swift
func startVirtualMachine() {
    virtualMachine.start(completionHandler: { (result) in
        if case let .failure(error) = result {
            fatalError("Virtual machine failed to start with \(error)")
        }
    })
}
```

**Objective-C**:

```objective-c
- (void)startVirtualMachine
{
    [_virtualMachine startWithCompletionHandler:^(NSError * _Nullable error) {
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Virtual machine failed to start with ", error.localizedDescription]);
        }
    }];
}
```

Or, if the app previously had the VM save its state to `SaveFile.vzvmsave`, `restoreVirtualMachine` calls the VM’s [`restoreMachineStateFrom(url:completionHandler:)`](vzvirtualmachine/restoremachinestatefrom(url:completionhandler:).md) and [`resume(completionHandler:)`](vzvirtualmachine/resume(completionhandler:).md) methods.

**Swift**:

```swift
func resumeVirtualMachine() {
    virtualMachine.resume(completionHandler: { (result) in
        if case let .failure(error) = result {
            fatalError("Virtual machine failed to resume with \(error)")
        }
    })
}

@available(macOS 14.0, *)
func restoreVirtualMachine() {
    virtualMachine.restoreMachineStateFrom(url: saveFileURL, completionHandler: { [self] (error) in
        // Remove the saved file. Whether success or failure, the state no longer matches the VM's disk.
        let fileManager = FileManager.default
        try! fileManager.removeItem(at: saveFileURL)

        if error == nil {
            self.resumeVirtualMachine()
        } else {
            self.startVirtualMachine()
        }
    })
}
```

**Objective-C**:

```objective-c
- (void)resumeVirtualMachine
{
    [_virtualMachine resumeWithCompletionHandler:^(NSError * _Nullable error) {
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Virtual machine failed to resume with ", error.localizedDescription]);
        }
    }];
}

- (void)restoreVirtualMachine API_AVAILABLE(macosx(14.0));
{
    [_virtualMachine restoreMachineStateFromURL:getSaveFileURL() completionHandler:^(NSError * _Nullable error) {
        // Remove the saved file. Whether success or failure, the state no longer matches the VM's disk.
        NSFileManager *fileManager = [NSFileManager defaultManager];
        [fileManager removeItemAtURL:getSaveFileURL() error:nil];

        if (!error) {
            [self resumeVirtualMachine];
        } else {
            [self startVirtualMachine];
        }
    }];
}
```

If the restore fails, the framework causes the virtual machine to reboot. In either case, the framework deletes `SaveFile.vzvmsave`  after restore completes because the VM disk no longer matches the state in the file.

##### Save the Vm

When you close the sample app, it calls the VM’s [`pause(completionHandler:)`](vzvirtualmachine/pause(completionhandler:).md) and [`saveMachineStateTo(url:completionHandler:)`](vzvirtualmachine/savemachinestateto(url:completionhandler:).md) methods. This captures the runtime state of the VM to `SaveFile.vzvmsave`, which the app uses when calling `startOrRestoreVirtualMachine` to resume running the VM at the same point when you relaunch the sample app.

**Swift**:

```swift
@available(macOS 14.0, *)
func saveVirtualMachine(completionHandler: @escaping () -> Void) {
    virtualMachine.saveMachineStateTo(url: saveFileURL, completionHandler: { (error) in
        guard error == nil else {
            fatalError("Virtual machine failed to save with \(error!)")
        }

        completionHandler()
    })
}

@available(macOS 14.0, *)
func pauseAndSaveVirtualMachine(completionHandler: @escaping () -> Void) {
    virtualMachine.pause(completionHandler: { (result) in
        if case let .failure(error) = result {
            fatalError("Virtual machine failed to pause with \(error)")
        }

        self.saveVirtualMachine(completionHandler: completionHandler)
    })
}
```

**Objective-C**:

```objective-c
- (void)saveVirtualMachine:(void (^)(void))completionHandler API_AVAILABLE(macosx(14.0));
{
    [_virtualMachine saveMachineStateToURL:getSaveFileURL() completionHandler:^(NSError * _Nullable error) {
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Virtual machine failed to save with ", error.localizedDescription]);
        }
        
        completionHandler();
    }];
}

- (void)pauseAndSaveVirtualMachine:(void (^)(void))completionHandler API_AVAILABLE(macosx(14.0));
{
    [_virtualMachine pauseWithCompletionHandler:^(NSError * _Nullable error) {
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Virtual machine failed to pause with ", error.localizedDescription]);
        }

        [self saveVirtualMachine:completionHandler];
    }];
}
```

The system defers app termination until the [`saveMachineStateTo(url:completionHandler:)`](vzvirtualmachine/savemachinestateto(url:completionhandler:).md) method completes.

## See Also

- [Running Linux in a Virtual Machine](running-linux-in-a-virtual-machine.md)
  Run a Linux operating system on your Mac using the Virtualization framework.
- [Running GUI Linux in a virtual machine on a Mac](running-gui-linux-in-a-virtual-machine-on-a-mac.md)
  Install and run GUI Linux in a virtual machine using the Virtualization framework.
- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)
  Download a macOS restore image and install it in a new VM.
- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)
  Design and run custom Linux guests on Apple silicon or Intel-based Mac Computers.
- [Virtualize macOS on a Mac](virtualize-macos-on-a-mac.md)
  Configure and run macOS guests on Apple silicon.
- [Virtualize Linux on a Mac](virtualize-linux-on-a-mac.md)
  Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)
  Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/running-macos-in-a-virtual-machine-on-apple-silicon)*