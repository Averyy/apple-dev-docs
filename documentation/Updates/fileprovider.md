# File Provider updates

**Framework**: Updates

Learn about important changes to File Provider.

#### Overview

Browse notable changes in [`File Provider`](https://developer.apple.com/documentation/FileProvider).

#### June 2024

- Offer people the ability to sync their Desktop and Documents folders with your File Provider app. Check whether a person opts in to sync these folders using [`replicatedKnownFolders`](https://developer.apple.com/documentation/FileProvider/NSFileProviderDomain/replicatedKnownFolders). Sync the folders using [`claimKnownFolders(_:localizedReason:completionHandler:)`](https://developer.apple.com/documentation/FileProvider/NSFileProviderManager/claimKnownFolders(_:localizedReason:completionHandler:)), or stop syncing using [`releaseKnownFolders(_:localizedReason:completionHandler:)`](https://developer.apple.com/documentation/FileProvider/NSFileProviderManager/releaseKnownFolders(_:localizedReason:completionHandler:)) if the person opts out. Provide the system with information about which folders you support syncing through [`supportedKnownFolders`](https://developer.apple.com/documentation/FileProvider/NSFileProviderDomain/supportedKnownFolders), and share the locations of the folders by adopting [`NSFileProviderKnownFolderSupporting`](https://developer.apple.com/documentation/FileProvider/NSFileProviderKnownFolderSupporting).
- Cache files on external disks. Confirm whether a volume is eligible for storing a domain using [`checkDomainsCanBeStoredOnVolume(at:)`](https://developer.apple.com/documentation/FileProvider/NSFileProviderManager/checkDomainsCanBeStoredOnVolume(at:)), and create a domain on that volume using the new [`init(displayName:userInfo:volumeURL:)`](https://developer.apple.com/documentation/FileProvider/NSFileProviderDomain/init(displayName:userInfo:volumeURL:)) initializer. Store data about the current sync state using [`stateDirectoryURL()`](https://developer.apple.com/documentation/FileProvider/NSFileProviderManager/stateDirectoryURL()), and determine whether to connect to a domain created on another device using [`shouldConnectExternalDomain(completionHandler:)`](https://developer.apple.com/documentation/FileProvider/NSFileProviderExternalVolumeHandling/shouldConnectExternalDomain(completionHandler:)).
- Install the File Provider logging profile to log helpful information for debugging and troubleshooting. Download the `.mobileconfig` file at [`Profiles and Logs`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/).

#### March 2024

- Improve error handling with new underlying error codes for [`NSFileProviderError.Code.providerNotFound`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/Code/providerNotFound). [`NSFileProviderError.Code.providerDomainTemporarilyUnavailable`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/Code/providerDomainTemporarilyUnavailable) indicates that the system is unable to service requests for this domain temporarily, and you can try again later. [`NSFileProviderError.Code.providerDomainNotFound`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/Code/providerDomainNotFound) indicates that there isn’t a registered domain for the corresponding identifier. [`NSFileProviderError.Code.applicationExtensionNotFound`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/Code/applicationExtensionNotFound) indicates that there isn’t an app extension within the app bundle.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/fileprovider)*