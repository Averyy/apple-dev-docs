# Running macOS in a virtual machine on Apple silicon

**Framework**: Virtualization

Install and run macOS in a virtual machine using the Virtualization framework.

**Availability**:
- macOS 27.0+
- Xcode 27.0+

#### Overview

> ❗ **Important**: Starting with macOS 27, this sample project includes an additional Swift scheme and app build target: `sharedBaseImageSampleApp`. This new app demonstrates Swift-only features, such as `DiskImageKit`. While the other versions of the sample `macOSVirtualMachineSampleApp-Objective-C` and `macOSVirtualMachineSampleApp-Swift` compile and run correctly, to take advantage of stacked disk images and other DiskImageKit features, use `sharedBaseImageSampleApp`.

This sample code project demonstrates how to install and run macOS virtual machines (VMs) on Apple silicon. The Xcode project includes three separate apps:

- `InstallationTool`, a command line utility that installs macOS from a restore image, which is a file with a `.ipsw` file extension, onto a VM. You can use this tool to download the restore image of the most current macOS release from the network, or with your own restore image. The utility creates a VM bundle and stores the resulting VM images in your Home directory.
- `macOSVirtualMachineSampleApp` is a Mac app that runs the macOS VM that `InstallationTool` installs. You use `macOSVirtualMachineSampleApp` to launch and control the macOS VM that loads and runs macOS from the VM bundle. This app includes entitlements to enable it to use Virtualization and access the VM’s audio input, such as the microphone.
- `sharedBaseImageSampleApp` is a Mac app that demonstrates how to create two VMs that use a common base disk image using the capabilities of DiskImageKit. In this version, the `InstallationTool` creates two disk images from the macOS restore image that `sharedBaseImageSampleApp` configures and that run simultaneously. As with `macOSVirtualMachineSampleApp`, this app includes entitlements to enable it to use Virtualization and access the VM’s audio input, such as the microphone.

There are five build targets in this project that represent the `InstallationTool` and the `macOSVirtualMachineSampleApp`, one set of targets each for Swift and Objective-C versions of the apps, and another target for the `sharedBaseImageSampleApp`.

> **Note**: The default deployment target is macOS 27, and the sample uses APIs present in that release. To build for an earlier version of macOS, change the deployment target as appropriate and adapt the code as necessary to either remove or conditionally compile support for macOS 27 API features.

##### Configure the Sample Code Project

You need to install the virtual machine, and `VM.bundle` needs exist before launching the sample app.

1. Set up code signing for each of the project’s targets by navigating to the Signing & Capabilities settings and selecting your team from the drop-down menu.
2. Run `InstallationTool` from within Xcode or in Terminal to download the latest available macOS restore image from the network and create a macOS VM image on disk. `InstallationTool` creates a `VM.bundle` package in your Home directory, containing: - `Disk.img` — The main disk image of the installed OS.
- `AuxiliaryStorage` — The auxiliary storage for macOS.
- `MachineIdentifier` — The data representation of the `VZMacMachineIdentifier` object.
- `HardwareModel` — The data representation of the `VZMacHardwareModel` object.
- `RestoreImage.ipsw` — The restore image downloaded from the network (this file exists only if the tool runs without arguments).
3. Select one of the versions of the app to launch, either `macOSVirtualMachineSampleApp` (Objective-C or Swift) or `sharedBaseImageSampleApp`, to run the macOS guest operating system. The sample app starts the VM and configures a graphical view that you interact with. The virtual Mac continues running until you shut it down from inside the guest OS, or quit the app. To reinstall the virtual machine, delete the `VM.bundle` package and run `InstallationTool` again.

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

The `macOSVirtualMachineSampleApp` versions operate identically, using a single VM image to launch a single macOS VM; the `sharedBaseImageSampleApp` uses different initial setup and configuration methods to enable the app to support two VMs using a common, shared base image that both VMs run.

As with the `macOSVirtualMachineSampleApp`, the installation tool downloads a macOS `.ipsw` restore image, creates an empty image (`Disk.img`), and then installs the OS there. This `Disk.img` becomes the base image that `sharedBaseImageSampleApp` uses to create the base image of a stack that its VMs use.

The following examples show the configuration and initialization methods for this multi-VM, Swift-only version; these methods create per-VM unique platform configurations and per-VM unique network devices the system needs to differentiate between the VMs. This example uses an index to distinguish each VM.

```swift
// Creates a per-VM platform object that includes a unique machine identifier and auxiliary storage.
private static func createMacPlatform(vmIndex: Int) -> VZMacPlatformConfiguration {
    let macPlatform = VZMacPlatformConfiguration()

    if !FileManager.default.fileExists(atPath: vmBundlePath) {
        fatalError("Missing Virtual Machine Bundle at \(vmBundlePath). Run InstallationTool first to create it.")
    }

    // The installation tool creates and describes the virtual hardware, and all VMs share the same hardware model.
    macPlatform.hardwareModel = MacOSVirtualMachineConfigurationHelper.readHardwareModel(hardwareModelURL: hardwareModelURL)

    // Each VM needs its own machine identifier and auxiliary storage.
    // Copy the auxiliary storage from the original VM (created during installation)
    // so it contains the boot configuration and NVRAM.
    let vmDir = vmDirectoryURL(forVM: vmIndex)
    let machineIdentifierURL = machineIdentifierURL(forVM: vmIndex)
    let auxiliaryStorageURL = auxiliaryStorageURL(forVM: vmIndex)

    if FileManager.default.fileExists(atPath: machineIdentifierURL.path) {
        guard let data = try? Data(contentsOf: machineIdentifierURL),
              let machineIdentifier = VZMacMachineIdentifier(dataRepresentation: data) else {
            fatalError("Failed to retrieve machine identifier for VM \(vmIndex).")
        }
        macPlatform.machineIdentifier = machineIdentifier
        macPlatform.auxiliaryStorage = VZMacAuxiliaryStorage(contentsOf: auxiliaryStorageURL)
    } else {
        try! FileManager.default.createDirectory(at: vmDir, withIntermediateDirectories: true)

        let machineIdentifier = VZMacMachineIdentifier()
        try! machineIdentifier.dataRepresentation.write(to: machineIdentifierURL)
        macPlatform.machineIdentifier = machineIdentifier

        let originalAuxStorage = vmBundleURL.appendingPathComponent("AuxiliaryStorage")
        try! FileManager.default.copyItem(at: originalAuxStorage, to: auxiliaryStorageURL)
        macPlatform.auxiliaryStorage = VZMacAuxiliaryStorage(contentsOf: auxiliaryStorageURL)
    }

    return macPlatform
}

 // Create a unique, per-VM block device configuration.
 static func createBlockDeviceConfiguration(vmIndex: Int) throws -> VZVirtioBlockDeviceConfiguration {
     let baseImage = try DiskImage(opening: .open(url: diskImageURL, mode: .readOnly))

    let stackedImage: StackedImage
    let overlay = overlayURL(forVM: vmIndex)
    if FileManager.default.fileExists(atPath: overlay.path) {
        let overlayImage = try DiskImage(opening: .open(url: overlay))
        stackedImage = try baseImage.appending(overlayImage)
    } else {
        stackedImage = try baseImage.appending(.asifLayer(url: overlay, type: .overlay))
    }

    let attachment = try VZDiskImageStorageDeviceAttachment(diskImage: stackedImage)
    return VZVirtioBlockDeviceConfiguration(attachment: attachment)
}

// Create a unique, per-VM network configuration; the last octet of the network MAC address is the index of the VM.
private static func createNetworkDeviceConfiguration(vmIndex: Int) -> VZVirtioNetworkDeviceConfiguration {
    let networkDevice = VZVirtioNetworkDeviceConfiguration()
    networkDevice.macAddress = VZMACAddress(string: String(format: "d6:a7:58:8e:78:%02x", vmIndex))!
    networkDevice.attachment = VZNATNetworkDeviceAttachment()
    return networkDevice
}

```

The app delegate starts and manages the VMs using individual machine configurations:

```swift
#if arch(arm64)
func applicationDidFinishLaunching(_ aNotification: Notification) {
    Task { @MainActor in
        let configurations = await createAllConfigurations()
        startVMs(with: configurations)
    }
}

@MainActor
private func startVMs(with configurations: [VZVirtualMachineConfiguration]) {
    for index in 1...Self.vmCount {
        let vm = VZVirtualMachine(configuration: configurations[index - 1])

        let delegate = SharedVirtualMachineDelegate(name: "VM \(index)")
        vm.delegate = delegate

        let (vmWindow, vmView): (NSWindow, VZVirtualMachineView)
        if index == 1 {
            let view = VZVirtualMachineView()
            window.title = "VM \(index) — Shared Base Image"
            window.contentView = view
            vmWindow = window
            vmView = view
        } else {
            (vmWindow, vmView) = makeVMWindow(
                title: "VM \(index) — Shared Base Image",
                frame: windowFrame(forVM: index)
            )
        }
        vmView.virtualMachine = vm
        vmView.capturesSystemKeys = true
        vmView.automaticallyReconfiguresDisplay = true

        virtualMachines.append(vm)
        delegates.append(delegate)
        windows.append(vmWindow)

        vm.start { result in
            if case let .failure(error) = result {
                fatalError("VM \(index) failed to start: \(error)")
            }
        }
    }
}

@MainActor
private func createAllConfigurations() async -> [VZVirtualMachineConfiguration] {
     do {
         return try await buildConfigurations()
     } catch is IncompatibleStackingError {
         guard promptOverlayReset() else {
             NSApplication.shared.terminate(nil)
             fatalError("Terminating due to incompatible overlays.")
         }
         await discardAllOverlays()
         do {
             return try await buildConfigurations()
         } catch {
             fatalError("Failed to create VM configurations after discarding overlays: \(error)")
         }
     } catch {
         fatalError("Failed to create VM configurations: \(error)")
     }
}

private func buildConfigurations() async throws -> [VZVirtualMachineConfiguration] {
    try await Task.detached {
        try (1...Self.vmCount).map {
            try SharedVMConfigurationHelper.createVirtualMachineConfiguration(vmIndex: $0)
        }
    }.value
}

private func discardAllOverlays() async {
    await Task.detached {
        for index in 1...Self.vmCount {
            SharedVMConfigurationHelper.discardOverlay(vmIndex: index)
        }
    }.value
}

@MainActor
private func promptOverlayReset() -> Bool {
    let alert = NSAlert()
    alert.messageText = "Overlays Incompatible"
    alert.informativeText =
        "The base disk image has been modified. " +
        "The existing overlays are no longer compatible " +
        "and must be reset.\n\n" +
        "Reset all overlays to start with a fresh state?"
    alert.alertStyle = .warning
    alert.addButton(withTitle: "Reset and Continue")
    alert.addButton(withTitle: "Quit")
    return alert.runModal() == .alertFirstButtonReturn
}
#else
func applicationDidFinishLaunching(_ aNotification: Notification) {
    fatalError("SharedBaseImageSampleApp requires an Apple Silicon Mac.")
}
#endif
```

The following examples (for both Swift and Objective-C) show how the `macOSVirtualMachineSampleApp` sample app version uses a single [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object to configure the basic characteristics of the guest, such as the CPU count, memory size, creation of disk images, various device configurations, and a [`VZMacOSBootLoader`](vzmacosbootloader.md) object to load the operating system from the disk image:

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
try! virtualMachineConfiguration.validateSaveRestoreSupport()

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

BOOL supportsSaveRestore = [configuration validateSaveRestoreSupportWithError:nil];
if (!supportsSaveRestore) {
    @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Invalid configuration" userInfo:nil];
}

self->_virtualMachine = [[VZVirtualMachine alloc] initWithConfiguration:configuration];
self->_delegate = [MacOSVirtualMachineDelegate new];
self->_virtualMachine.delegate = self->_delegate;
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
let hardwareModel = MacOSVirtualMachineConfigurationHelper.readHardwareModel(hardwareModelURL: hardwareModelURL)
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

virtualMachineConfiguration.usbControllers = [MacOSVirtualMachineConfigurationHelper.createUSBControllerConfiguration()]

try! virtualMachineConfiguration.validate()

try! virtualMachineConfiguration.validateSaveRestoreSupport()

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

    configuration.usbControllers = @[ [MacOSVirtualMachineConfigurationHelper createUSBControllerConfiguration] ];
    _usbDevicesByRegistryID = [[NSMutableDictionary alloc] init];

    BOOL isValidConfiguration = [configuration validateWithError:nil];
    if (!isValidConfiguration) {
        @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Invalid configuration" userInfo:nil];
    }
    
    BOOL supportsSaveRestore = [configuration validateSaveRestoreSupportWithError:nil];
    if (!supportsSaveRestore) {
        @throw [NSException exceptionWithName:NSInternalInconsistencyException reason:@"Invalid configuration" userInfo:nil];
    }

_virtualMachine = [[VZVirtualMachine alloc] initWithConfiguration:configuration];
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

// Configure the app to automatically respond to changes in the display size.
virtualMachineView.automaticallyReconfiguresDisplay = true

let fileManager = FileManager.default
if fileManager.fileExists(atPath: saveFileURL.path) {
    restoreVirtualMachine()
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

    // Configure the app to automatically respond to changes in the display size.
    self->_virtualMachineView.automaticallyReconfiguresDisplay = YES;

    NSFileManager *fileManager = [NSFileManager defaultManager];
    if ([fileManager fileExistsAtPath:getSaveFileURL().path]) {
        [self restoreVirtualMachine];
    } else {
        [self startVirtualMachine];
    }
});
```

Additionally, as part of the VM creation, the app also specifies macOS startup options that create a default user, including a default full name, password, whether this initial account automatically logs in, and whether the account is accessible remotely over the network using the Secure Shell protocol (SSH).

**Swift**:

```swift
let guestOptions = VZMacGuestProvisioningOptions()
guestOptions.fullName = "Admin User"
guestOptions.username = "admin"
guestOptions.password = "password123!"
guestOptions.logsInAutomatically = true
guestOptions.enablesRemoteLogin = true

let startOptions = VZMacOSVirtualMachineStartOptions()
try! startOptions.setGuestProvisioning(guestOptions)
```

**Objective-C**:

```objective-c
VZMacGuestProvisioningOptions *guestOptions = [[VZMacGuestProvisioningOptions alloc] init];
guestOptions.fullName = @"Admin User";
guestOptions.username = @"admin";
guestOptions.password = @"password123!";
guestOptions.logsInAutomatically = YES;
guestOptions.enablesRemoteLogin = YES;

VZMacOSVirtualMachineStartOptions *startOptions = [[VZMacOSVirtualMachineStartOptions alloc] init];
NSError *error = nil;
if (![startOptions setGuestProvisioningOptions:guestOptions error:&error]) {
    abortWithErrorMessage([NSString stringWithFormat:@"Failed to set guest provisioning options: %@", error.localizedDescription]);
}
```

##### Listen for Accessories and Respond to Connection Changes

After successfully starting the VM, the app starts listening for USB accessories with the [`Accessory Access`](https://developer.apple.com/documentation/accessoryaccess) framework. As devices connect to or disconnect from the VM, the framework calls the [`usbAccessoryDidConnect(_:)`](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener/usbaccessorydidconnect(_:)) and [`usbAccessoryDidDisconnect(_:)`](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener/usbaccessorydiddisconnect(_:)) protocol methods to inform the app about these transitions.

**Swift**:

```swift
func startListeningForUSBAccessories() {
    Task {
        do {
            let connectedAccessories = try await AAUSBAccessoryManager.shared.registerListener(self, matchingCriteria: [])
            for accessory in connectedAccessories {
                usbAccessoryDidConnect(accessory)
            }
        } catch {
            fatalError("Failed to register USB accessory listener. \(error)")
        }
    }
}

nonisolated func usbAccessoryDidDisconnect(_ usbAccessory: AAUSBAccessory) {
    virtualMachine.queue.async { [weak self] in
        guard let self else {
            return
        }

        let usbDevice = self.accessories[usbAccessory.registryID]!
        self.virtualMachine.usbControllers.first!.detach(device: usbDevice) { [weak self] error in
            guard let self else {
                return
            }
            self.accessories.removeValue(forKey: usbAccessory.registryID)
        }
    }
}

nonisolated func usbAccessoryDidConnect(_ usbAccessory: AAUSBAccessory) {
    virtualMachine.queue.async { [weak self] in
        guard let self else {
            return
        }

        if self.virtualMachine.state != .running && self.virtualMachine.state != .paused {
            return
        }

        let configuration = VZUSBPassthroughDeviceConfiguration(device: usbAccessory)
        do {
            let usbDevice = try VZUSBPassthroughDevice(configuration: configuration)
            self.virtualMachine.usbControllers.first!.attach(device: usbDevice) { [weak self] error in
                guard let self else {
                    return
                }
                self.accessories[usbAccessory.registryID] = usbDevice
            }
        } catch {
            return
        }
    }
}        
```

**Objective-C**:

```objective-c
- (void)startListeningForUSBAccessories
{
    [AAUSBAccessoryManager.sharedManager registerListener:self withMatchingCriteria:@[] completionHandler:^(NSArray<AAUSBAccessory *> *accessories, NSError *error) {
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Failed to register accessory listener with ", error.localizedDescription]);
        }

        for (AAUSBAccessory *accessory in accessories) {
            [self usbAccessoryDidConnect:accessory];
        }
    }];
}

- (void)usbAccessoryDidConnect:(AAUSBAccessory *)usbAccessory
{
    __weak AppDelegate *weak_self = self;
    dispatch_async(_virtualMachine.queue, ^{
        AppDelegate *strong_self = weak_self;
        if (!strong_self) {
            return;
        }
        if (strong_self->_virtualMachine.state != VZVirtualMachineStateRunning && strong_self->_virtualMachine.state != VZVirtualMachineStatePaused) {
            return;
        }
        VZUSBPassthroughDeviceConfiguration *usbDeviceConfiguration = [[VZUSBPassthroughDeviceConfiguration alloc] initWithDevice:usbAccessory];
        NSError *error;
        VZUSBPassthroughDevice *usbDevice = [[VZUSBPassthroughDevice alloc] initWithConfiguration:usbDeviceConfiguration error:&error];
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Failed to create USB device with ", error.localizedDescription]);
        }

        strong_self->_usbDevicesByRegistryID[@(usbAccessory.registryID)] = usbDevice;

        [strong_self->_virtualMachine.usbControllers.firstObject attachDevice:usbDevice completionHandler:^(NSError *error) {
            if (error) {
                abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Failed to attach USB device to virtual machine with ", error.localizedDescription]);
            }
        }];
    });
}

- (void)usbAccessoryDidDisconnect:(AAUSBAccessory *)usbAccessory
{
    __weak AppDelegate *weak_self = self;
    dispatch_async(_virtualMachine.queue, ^{
        AppDelegate *strong_self = weak_self;
        if (!strong_self) {
            return;
        }
        VZUSBPassthroughDevice *usbDevice = strong_self->_usbDevicesByRegistryID[@(usbAccessory.registryID)];
        [strong_self->_virtualMachine.usbControllers.firstObject detachDevice:usbDevice completionHandler:^(NSError *error) {
            [strong_self->_usbDevicesByRegistryID removeObjectForKey:@(usbAccessory.registryID)];
        }];
    });
}
```

If the virtual machine was running when the sample app last exited, the app calls `restoreVirtualMachine` to restore the state. If the virtual machine was in a shutdown state, the app calls `startVirtualMachine` to reboot the machine. Both methods start the VM asynchronously in the background. The VM loads the system image and boots macOS. After macOS starts, the user interacts with a [`VZVirtualMachineView`](vzvirtualmachineview.md) window that displays the macOS UI and handles keyboard and mouse input through a [`VZMacGraphicsDeviceConfiguration`](vzmacgraphicsdeviceconfiguration.md) as though the user is interacting directly with the Mac hardware. The [`VZVirtualMachineView`](vzvirtualmachineview.md) automatically resizes the virtual machine display when the window size changes, and captures system keys such as the Globe key on a Mac keyboard.

The `startVirtualMachine` method calls the VM’s [`start(completionHandler:)`](vzvirtualmachine/start(completionhandler:).md) method.

For a sendable wrapper that connects a [`VZVirtualMachineView`](vzvirtualmachineview.md) to a virtual machine, see [`VZVirtualMachineViewAdaptor`](vzvirtualmachineviewadaptor.md).

**Swift**:

```swift
func startVirtualMachine() {
    let startOptions = MacOSVirtualMachineConfigurationHelper.createMacOSStartOptions()
    virtualMachine.start(options: startOptions, completionHandler: { error in
        if let error {
            fatalError("Virtual machine failed to start with \(error)")
        }
        self.startListeningForUSBAccessories()
    })
}
```

**Objective-C**:

```objective-c
- (void)startVirtualMachine
{
    VZMacOSVirtualMachineStartOptions *startOptions = [MacOSVirtualMachineConfigurationHelper createMacOSStartOptions];
    [_virtualMachine startWithOptions:startOptions completionHandler:^(NSError * _Nullable error) {
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Virtual machine failed to start with ", error.localizedDescription]);
        }

        [self startListeningForUSBAccessories];
    }];
}
```

If the app previously had the VM save its state to `SaveFile.vzvmsave`, `restoreVirtualMachine` calls the VM’s [`restoreMachineStateFrom(url:completionHandler:)`](vzvirtualmachine/restoremachinestatefrom(url:completionhandler:).md) and [`resume(completionHandler:)`](vzvirtualmachine/resume(completionhandler:).md) methods.

**Swift**:

```swift
func resumeVirtualMachine() {
    virtualMachine.resume(completionHandler: { (result) in
        if case let .failure(error) = result {
            fatalError("Virtual machine failed to resume with \(error)")
        }
        self.startListeningForUSBAccessories()
    })
}


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

        [self startListeningForUSBAccessories];
    }];
}

- (void)restoreVirtualMachine
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
func saveVirtualMachine(completionHandler: @escaping () -> Void) {
    virtualMachine.saveMachineStateTo(url: saveFileURL, completionHandler: { (error) in
        guard error == nil else {
            fatalError("Virtual machine failed to save with \(error!)")
        }

        completionHandler()
    })
}

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
- (void)saveVirtualMachine:(void (^)(void))completionHandler
{
    [_virtualMachine saveMachineStateToURL:getSaveFileURL() completionHandler:^(NSError * _Nullable error) {
        if (error) {
            abortWithErrorMessage([NSString stringWithFormat:@"%@%@", @"Virtual machine failed to save with ", error.localizedDescription]);
        }
                    
        completionHandler();
    }];
}

- (void)pauseAndSaveVirtualMachine:(void (^)(void))completionHandler
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
- [Running Intel Binaries in Linux VMs](running-intel-binaries-in-linux-vms.md)
  Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/running-macos-in-a-virtual-machine-on-apple-silicon)*