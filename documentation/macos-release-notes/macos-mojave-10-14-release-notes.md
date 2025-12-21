# macOS Mojave 10.14 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 10.14 SDK provides support for developing apps for Macs running macOS Mojave. The SDK comes bundled with Xcode 10 available from the Mac App Store. For information about Xcode 10, see [`Xcode 10 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-10-release-notes).

##### General

###### Known Issues

- Mac Pro (mid 2010 and mid 2012 models) must first be updated to macOS High Sierra 10.13.6 before updating to macOS Mojave. (41798700)

###### Deprecations

- Ink APIs in `Ink.framework` and associated ink events in Carbon are deprecated. (29008562)
- Using Carbon File Manager APIs and other APIs based on the [`FSRef`](https://developer.apple.com/documentation/coreservices/fsref) structure might slow system performance when using APFS-formatted volumes. File Manager is deprecated in macOS 10.8 and later. For improved performance, switch to URL-based replacements such as [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) and [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL).

##### 32 Bit Deprecation

###### New Features

- 32-bit processes now trigger an alert on launch.
- You can review 32-bit apps in System Information. The Software > Legacy Software report in System Information provides an overview of impacted software.

###### Deprecations

- 32-bit system services such as `mdworker32`, `quicklookd32`, `inkserver`, `QTKitserver` remain for compatibility purposes and will be deprecated in a future release of macOS. If your app is using one of these services, migrate to the equivalent 64-bit framework.
- `QTKit` and `QTMovieModernizer` depend on the deprecated 32-bit QuickTime framework which remains present in macOS Mojave for compatibility purposes. When future versions of macOS no longer support 32-bit processes, these APIs will become unavailable.
- Administrators are encouraged to review root-owned daemons and processes on behalf of non-administrator users, as these users might lack permissions required to resolve previously-installed 32-bit dependencies.

##### Apple File System Apfs

###### Known Issues

- After enabling or disabling FileVault on a volume, the volume will become invisible to pre-macOS Mojave systems until the encryption or decryption process completes.

##### Applescript

###### New Features

- Sending Apple events from an app—including script applets—now requires user approval. The list of currently approved apps can be viewed and edited in the Automation category in the Privacy tab in System Preferences > Security & Privacy. If an event is blocked because the user didn’t approve that app, the event will fail with the error code: `-1743 ("``: Not authorized to send Apple events to ``")`. An event can be preflighted using [`AEDeterminePermissionToAutomateTarget(_:_:_:_:)`](https://developer.apple.com/documentation/coreservices/3025784-aedeterminepermissiontoautomatet).
- Scripting additions can no longer be globally installed. The `/Library/ScriptingAdditions`, `/Network/Library/ScriptingAdditions`, and `~/Library/ScriptingAdditions` directories are effectively ignored.Distribute scripting additions as part of a specific app by embedding the scripting addition in the app’s `Contents/Resources/Scripting Additions` directory and signing both the addition and the app with the same team identifier.

##### Appkit

See [`AppKit Release Notes for macOS 10.14`](appkit-release-notes-for-macos-10_14.md).

##### Core Ml

###### New Features

- Support for quantized models (≤ 8-bit linear and/or lookup table)
- Support for flexible image sizes and multi-array shapes
- Batch prediction API
- Support for custom models
- Support for Create ML models (Vision Feature Print, Text Classifier, Word Tagger)

##### Disk Utility

###### Known Issues

-  Don’t use Disk Utility while booted from Internet Recovery to erase an APFS Fusion container. (40565698)  Use Disk Utility while booted into macOS 10.13.6 or newer.

##### Egpu

###### New Features

- You can now request to use an external GPU (eGPU) when an app’s window is located on a display connected directly to your Mac, including the built-in display on iMac or MacBook Pro. To enable this option in an app, choose File > Get Info and check the ’Prefer External GPU’ checkbox. (39888124)

##### Facetime and Messages

###### Known Issues

- Group FaceTime has been removed from the initial release of macOS Mojave and will ship in a future software update later this fall.

##### Foundation

See [`Foundation Release Notes`](foundation-release-notes.md).

##### Grab

###### Deprecations

- Grab is superseded by the Screenshot app.

##### Homekit

###### Known Issues

- Inviting iOS 11 users who have multiple email addresses associated with their Apple ID to a home might not succeed. (41033550)  Send the invitation to a different email address or phone number associated with the Apple ID of the iOS 11 user.

##### Localization

###### New Features

- British English, Australian English, Canadian French, and Hong Kong Chinese (Traditional) localization is new in macOS Mojave.

###### Resolved Issues

- You might experience difficulty logging into your account because the keyboard layout may change unexpectedly at the Login window. (40821875)  Log in to your account, launch Terminal, and execute the following command: ```bash
sudo rm -rf /var/db/securityagent/Library/Preferences/com.apple.HIToolbox.plist
```

##### Mail

###### Deprecations

- The Stationery feature has been removed. (38725777)

##### Maps

###### New Features

- [`MKMapView`](https://developer.apple.com/documentation/MapKit/MKMapView) and [`MKMapSnapshotter`](https://developer.apple.com/documentation/MapKit/MKMapSnapshotter) are updated to support the new Dark Map style. MapKit  automatically switches to the Dark Map appearance when Dark Mode is enabled, the user hasn’t disabled the Dark Map in the Maps app, and your app has been compiled for macOS 10.14 Mojave. As a result, most apps using MapKit don’t require code changes to adopt the correct behavior. Both [`MKMapView`](https://developer.apple.com/documentation/MapKit/MKMapView) and [`MKMapSnapshotter`](https://developer.apple.com/documentation/MapKit/MKMapSnapshotter) support overriding this behavior through their respective appearance property. If your app overlays custom controls on top of the map view or the snapshot, you might want to react to changes of the map appearance using [`NSAppearance`](https://developer.apple.com/documentation/AppKit/NSAppearance). (39003102)

##### Networking

###### New Features

- The [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) HTTP/2 implementation is updated to support HTTP/2 connection reuse per RFC 7540 Section 9.1.1. This requires an HTTP/2 server to present a certificate which covers more than one server hostname. The certificate may use the Subject Alternative Name extension or wildcarded domain names. In addition, [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) requires name resolution to resolve the different hostnames to the same IP address. [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) may reuse HTTP/2 connections across different domain names when these conditions are satisfied. (37507838)

###### Deprecations

- The `ftp://` and `file://` URL schemes for Proxy Automatic Configuration (PAC) are deprecated. HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including, but not limited to, configurations set via Settings, System Preferences, profiles, and [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/connectionProxyDictionary), and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/CFNetwork/CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)). (37811761)

##### Open Gl and Open Cl

###### Deprecations

- The APIs in the OpenGL and OpenCL frameworks are deprecated and remain present for compatibility purposes. Transition to Metal if your app is using OpenGL or OpenCL.

##### Privacy

###### New Features

- Apps that call the [`scanForNetworks(withName:)`](https://developer.apple.com/documentation/CoreWLAN/CWInterface/scanForNetworks(withName:)) method can no longer obtain the MAC address (BSSID) of nearby Wi-Fi access points when Location Services is disabled. If broadcasted, the network name (SSID) remains included in the scan results. (37427543)
- Apps can’t access protected storage unless they’re added to the Application Data category located in the Privacy tab of System Preferences > Security & Privacy. (39798760)

##### Safari and Webkit

###### Deprecations

- The Safari Extension [`canLoad`](https://developer.apple.com/documentation/safariextensions/safaricontentbrowsertabproxy/1635506-canload) API is deprecated. Safari deactivates these extensions and notifies users upon first launch. You can reenable affected extensions using the Extensions pane in Safari preferences. Extensions using [`canLoad`](https://developer.apple.com/documentation/safariextensions/safaricontentbrowsertabproxy/1635506-canload) should switch to the Content Blocker model. (33726891)
- Legacy NPAPI browser plug-ins are no longer supported in Safari, with the exception of Adobe Flash. These plug-ins won’t load and can’t be reenabled. (34213078)
- Safari no longer supports developer-signed `.safariextz` packaged legacy Safari Extensions. When you first launch Safari on macOS Mojave, if you have any legacy developer-signed extensions installed, you’ll see a notification that such extensions are no longer supported. These extensions can’t be reenabled. Safari Extension Gallery extensions remain supported; however, this support will be removed in an upcoming macOS release. Adopt the [`Safari app extensions`](https://developer.apple.com/documentation/SafariServices/safari-app-extensions) programming model instead. (39007695)

##### Social Network Integrations

###### Deprecations

- macOS no longer includes built-in integrations with social networking and media sites. Use share extensions if this functionality is desired. For design guidance, see [`Human Interface Guidelines > Share Extensions`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/extensions/share-extensions/).

##### Terminal

###### Resolved Issues

- The shell command `link` takes two arguments, neither of which is permitted to be the name of a directory. Prior to macOS Mojave, the command `link F D`, where `F` is a file and `D` is a directory, created the hard link `D/F`. In macOS Mojave this behavior now conforms to the documented behavior. The error message `link: D is a directory` is displayed and the command exits with a failure status (`1`).  (42901913)

## See Also

- [macOS Mojave 10.14.6 Release Notes](macos-mojave-10_14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.5 Release Notes](macos-mojave-10_14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.4 Release Notes](macos-mojave_10_14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.3 Release Notes](macos-mojave-10_14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.2 Release Notes](macos-mojave-10_14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-mojave-10_14-release-notes)*