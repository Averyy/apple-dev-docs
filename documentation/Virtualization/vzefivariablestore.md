# VZEFIVariableStore

**Framework**: Virtualization  
**Kind**: class

An object that represents the Extensible Firmware Interface (EFI) variable store that contains NVRAM variables the EFI exposes.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZEFIVariableStore
```

## Topics

### Creating the variable store
- [init(creatingVariableStoreAt: URL, options: VZEFIVariableStore.InitializationOptions) throws](vzefivariablestore/init(creatingvariablestoreat:options:).md)
  Creates a new EFI variable store at specified the URL on the filesystem, initialization options, and error-return variable.
- [init(url: URL)](vzefivariablestore/init(url:)-83pcn.md)
  Initialize the variable store from the URL of an existing file.
- [VZEFIVariableStore.InitializationOptions](vzefivariablestore/initializationoptions.md)
  Constants that describe the options available when creating a new Extensible Firmware Interface (EFI) variable store.
### Instance properties
- [var url: URL](vzefivariablestore/url.md)
  The URL of the variable store on the local file system.
### Initializers
- [init(URL: URL)](vzefivariablestore/init(url:)-8ewtl.md)
- [init(creatingVariableStoreAtURL: URL, options: VZEFIVariableStore.InitializationOptions) throws](vzefivariablestore/init(creatingvariablestoreaturl:options:).md)
### Instance Properties
- [var enrolledSecureBootSignatures: VZEFISignatureDatabaseConfiguration](vzefivariablestore/enrolledsecurebootsignatures.md)
  The currently enrolled Key Exchange Key (KEK), allowed signature database (db), and forbidden signature database (dbx) signatures.
- [var isSecureBootEnabled: Bool](vzefivariablestore/issecurebootenabled.md)
  A Boolean value that indicates whether Secure Boot is in an enabled state in the variable store.
### Instance Methods
- [func disableSecureBoot() throws](vzefivariablestore/disablesecureboot.md)
  Disables Secure Boot while preserving the existing configuration.
- [func enableSecureBoot(platformKey: SecCertificate) throws](vzefivariablestore/enablesecureboot(platformkey:).md)
  Enables Secure Boot with a custom Platform Key.
- [func enableSecureBootUsingDefaultPlatformKey() throws](vzefivariablestore/enablesecurebootusingdefaultplatformkey.md)
  Enables Secure Boot with an Apple-managed Platform Key.
- [func enrollDefaultSecureBootSignatures() throws](vzefivariablestore/enrolldefaultsecurebootsignatures.md)
  Enrolls the default signatures to Secure Boot databases.
- [func enrollSecureBootSignatures(VZEFISignatureDatabaseConfiguration) throws](vzefivariablestore/enrollsecurebootsignatures(_:).md)
  Enrolls the given signatures to Secure Boot databases.
- [func resetSecureBoot() throws](vzefivariablestore/resetsecureboot.md)
  Clears any previously applied Secure Boot configuration and disables Secure Boot.

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

- [class VZBootLoader](vzbootloader.md)
  The base class that defines the management of the initial process of the guest system.
- [class VZLinuxBootLoader](vzlinuxbootloader.md)
  An object that loads and configures a Linux kernel as the guest system of your VM.
- [class VZEFIBootLoader](vzefibootloader.md)
  The boot loader configuration the system uses to boot guest-operating systems that expect an Extensible Firmware Interface (EFI) ROM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore)*