# VZMacOSInstaller

**Framework**: Virtualization  
**Kind**: class

An object you use to install macOS on the specified virtual machine.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacOSInstaller
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Overview

Initialize a [`VZMacOSInstaller`](vzmacosinstaller.md) object with a [`VZVirtualMachine`](vzvirtualmachine.md) and a file URL that refers to a macOS restore image.

The following code example shows how to use a `VZMacOSInstaller:`

```swift
// Call VZMacOSInstaller with a URL that corresponds to a local file. 
// This is the storage location for the restore image the app downloads.
let localRestoreImageURL = ...

// Load the latest restore image.
guard let restoreImage = try? await VZMacOSRestoreImage.latestSupported else {
    // Handle the error.
    abort()
}

// Call VZMacOSInstaller with a URL that corresponds to a local file. 
// Because restoreImage came from latestSupported, its URL property refers to a 
// restore image on the network. Download the restore image to the local file system.
guard let (location, _) = try? await URLSession.shared.download(from: restoreImage.url, delegate: nil) 
    else {
        // Handle the error.
        abort()
}

guard ((try? FileManager.default.moveItem(at: location, to: localRestoreImageURL)) != nil) else {
    // Handle the error.
    abort()
}

DispatchQueue.main.async {
    // Becuase this restore image came from VZMacOSRestoreImage.
    // latestSupported, mostFeaturefulSupportedConfiguration should not be nil.
    let configurationRequirements = restoreImage.mostFeaturefulSupportedConfiguration!

    // Construct a VZVirtualMachineConfiguration that satisfies the configuration requirements.
    let configuration = VZVirtualMachineConfiguration()
    configuration.bootLoader = VZMacOSBootLoader()
    configuration.platform = VZMacPlatformConfiguration()

    // The following are minimum values; you can use larger values if desired.
    configuration.cpuCount = configurationRequirements.minimumSupportedCPUCount
    configuration.memorySize = configurationRequirements.minimumSupportedMemorySize

    // Set other configuration properties as necessary.
    // ...

guard ((try? configuration.validate()) != nil) else {
    // Handle the error.
    abort()
}

let virtualMachine = VZVirtualMachine(configuration: configuration)
let installer = VZMacOSInstaller(virtualMachine: virtualMachine, restoringFromImageAt: localRestoreImageURL)
installer.install(completionHandler: { (result: Result) in
    if case let .failure(error) = result {
        // Handle the error.
        abort()
    } else {
        // Installation was successful.
    }
})

// Observe progress using installer.progress object.
}
```

## Topics

### Creating a macOS Installer
- [init(virtualMachine: VZVirtualMachine, restoringFromImageAt: URL)](vzmacosinstaller/init(virtualmachine:restoringfromimageat:).md)
  Creates a macOS installer object.
### Getting Information About an Installation
- [var progress: Progress](vzmacosinstaller/progress.md)
  A progress object that you can use to observe or cancel an installation.
- [var restoreImageURL: URL](vzmacosinstaller/restoreimageurl.md)
  The restore image URL used to initialize this installer.
- [var virtualMachine: VZVirtualMachine](vzmacosinstaller/virtualmachine.md)
  The virtual machine used to initialize this installer.
### Installing macOS
- [func install(completionHandler: (Result<Void, any Error>) -> Void)](vzmacosinstaller/install(completionhandler:).md)
  Start installing macOS.
- [func install() async throws](vzmacosinstaller/install.md)
  Start installing macOS.

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

- [class VZVirtualMachine](vzvirtualmachine.md)
  An object that manages the overall state and configuration of your VM.
- [class VZMacOSRestoreImage](vzmacosrestoreimage.md)
  An object that describes a version of macOS to install on to a virtual machine.
- [class VZMacOSConfigurationRequirements](vzmacosconfigurationrequirements.md)
  An object that describes the parameter constraints required by a specific configuration of macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosinstaller)*