# Requesting access to capabilities for your app playground

**Framework**: Swift Playgrounds  
**Role**: Article

Request access for your app to protected resources, services, or device hardware such as sensors.

## Overview

Your app can access many of the powerful hardware features and system services — capabilities — that are available on a device. For example, you could use the microphone together with speech recognition services to provide a voice interface, or you could access geolocation services for navigation.

Think of these capabilities as belonging to the person on whose device your app is running. Before using a capability, you ask their permission for access. For instance, if your app uses the camera to recognize landmarks, your app must explicitly ask permission to use the camera for that purpose. This is done with an alert from which the person can grant or deny your app access to that capability by tapping or clicking a button.

For more information about capabilities, see [Adding Capabilities to Your App](../Xcode/adding-capabilities-to-your-app.md).

### Import the framework

To use a capability, your code needs access to the relevant code module — usually a system framework. Start off by importing the framework at the top of your source file. For example, to access the user’s contacts, import the [Contacts](../Contacts/Contacts.md) framework.

```swift
import Contacts
```

### Request permission from the user

Many capabilities involve access to sensitive data, or use particular hardware features — such as finding a contact, or taking a photo. Before using one of these capabilities, you must explicitly request permission from the user. Do this when the person first tries to use the capability, so that the request makes most sense at the time.

Depending on the specific framework, your code for the request may look like this:

```swift
do {
    let store = CNContactStore()
    if try await store.requestAccess(for: .contacts) {
        // Do something with Contacts.
    } else {
        // Handle if Contacts access is denied.
    }
} catch {
    // Handle any error.
}
```

The preceding code shows an alert asking the user to grant your app permission to access their contacts. The alert displays a message — or purpose string — that explains why your app is requesting access to the capability, so the person can feel confident granting permission. People only need to grant access to the capability once. You should also consider what to do if they deny your app access to the capability. Your app may need to restrict available features, and provide appropriate messaging.

The following table provides a list of the capabilities supported in Swift Playgrounds. Each of these capabilities has a default purpose string, so you can use them by importing the framework and making the necessary access request.

| Capability | Framework or Class | Description |
| --- | --- | --- |
| App Tracking Transparency | [App Tracking Transparency](../AppTrackingTransparency/AppTrackingTransparency.md) | Required if your app uses the AppTrackingTransparency framework to collect data about end users and shares it with other companies for purposes of tracking across apps and websites. |
| [App Transport Security](../BundleResources/information-property-list/nsapptransportsecurity.md) | N/A | Required if your app needs to adjust default security settings for HTTP connections. |
| Bluetooth | [Core Bluetooth](https://developer.apple.com/bluetooth/) | Required if your app uses Bluetooth. |
| Calendars | [EventKit](../EventKit/EventKit.md) | Required if your app accesses Calendar. |
| Camera | [AVFoundation](../AVFoundation/capture-setup.md) | Required if your app needs to use the device’s cameras. |
| Contacts | [Contacts](../Contacts/Contacts.md) | Required if your app accesses Contacts. |
| Core Location Always | [Core Location](../CoreLocation/CoreLocation.md), [MapKit](../MapKit/MapKit.md) | Required if your app needs access to the user’s location at all times. |
| Core Location When in Use | [Core Location](../CoreLocation/CoreLocation.md), [MapKit](../MapKit/MapKit.md) | Required if your app accesses the user’s location when the app is in use. |
| Core Motion | [Core Motion](../CoreMotion/CoreMotion.md) | Required if your app accesses the motion data. |
| Face ID | [Local Authentication](../LocalAuthentication/LocalAuthentication.md) | Required if your app uses Face ID for authentication. |
| File Access (macOS) | [FileManager](../Foundation/filemanager.md) in [Foundation](../Foundation/Foundation.md) | Required if your app needs to access files on the disk. |
| Local Network | [Multipeer Connectivity](../MultipeerConnectivity/MultipeerConnectivity.md), [Network](../Network/Network.md) | Any app that uses the local network, directly or indirectly, should include this description. This includes apps that use Bonjour and services implemented with Bonjour, as well as direct unicast or multicast connections to local hosts. |
| Media Library | [Media Player](../MediaPlayer/MediaPlayer.md) | Required if your app needs access to the user’s iCloud Music library or Apple Music catalog. |
| Microphone | [AVFoundation](../AVFoundation/capture-setup.md) | Required if your app accesses the device’s microphone. |
| Nearby Interaction | [Nearby Interaction](../NearbyInteraction/NearbyInteraction.md) | Required if your app uses the Nearby Interaction framework. Applies only to devices with a U1 chip. |
| Network Connections (macOS) | [URLSession](../Foundation/urlsession.md) in [Foundation](../Foundation/Foundation.md) | Required if your app needs to receive incoming or perform outgoing network connections. |
| Photo Library | [PhotoKit](../PhotoKit/PhotoKit.md) | Required if your app needs access to the user’s photo library. |
| Photo Library (Add Only) | [PhotoKit](../PhotoKit/PhotoKit.md) | Required if your app only needs access to the user’s photo library to add photos. |
| Reminders | [EventKit](../EventKit/EventKit.md) | Required if your app accesses Reminders. |
| Speech Recognition | [Speech](../Speech/Speech.md) | Required to perform speech recognition using Apple’s servers. |

### Add a custom purpose string

You can supply your own custom purpose string to explain why your app requires a particular capability. Be specific and use straightforward language in your purpose string, so anyone using your app can clearly understand why they are being asked to grant permission for that capability. Here’s an example:

```
MyApp uses the camera to identify landmarks as you explore new places.
```

In Swift Playgrounds you can add custom purpose strings by selecting App Settings in the sidebar, and then Capabilities. Tap or click the Add button (＋) to add the capabilities you need.

### Prepare your app for distribution

If you want to submit your app to TestFlight or to the App Store, you must add your own custom purpose string for each of the capabilities you use in your app before submitting your app to App Store Connect. You can do this in Swift Playgrounds by selecting App Settings in the sidebar, and then Capabilities.

## See Also

### App playgrounds
- [Adding a Swift package to your app playground](./add-a-swift-package.md)
  Extend the functionality of your app playground by finding and adding a publicly available Swift package.
- [Debugging an App Playground using the Console](./console-print-debugging.md)
  Learn different methods to debug your code using console output.
- [Previewing SwiftUI views in Swift Playgrounds](./live-preview.md)
  Use the canvas in Swift Playgrounds to see a live preview of the SwiftUI views in your app.
- [Importing sample content into user app playgrounds](./using-content-in-user-projects.md)
  Learn how to bring sample code into your app playground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/project-capabilities)*