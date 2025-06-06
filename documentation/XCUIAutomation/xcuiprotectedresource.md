# XCUIProtectedResource

**Framework**: Xcuiautomation  
**Kind**: enum

A system resource that requires user authorization to access.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+
- watchOS 6.2+
- Xcode 16.3+

## Declaration

```swift
enum XCUIProtectedResource
```

## Topics

### Protected resources
- [XCUIProtectedResource.location](xcuiprotectedresource/location.md)
  The protected resource case for Location Services.
- [XCUIProtectedResource.userTracking](xcuiprotectedresource/usertracking.md)
  The protected resource case for access to tracking data.
- [XCUIProtectedResource.contacts](xcuiprotectedresource/contacts.md)
  The protected resource case for access to Contacts.
- [XCUIProtectedResource.calendar](xcuiprotectedresource/calendar.md)
  The protected resource case for acces to Calendar data.
- [XCUIProtectedResource.reminders](xcuiprotectedresource/reminders.md)
  The protected resource case for access to Reminders data.
- [XCUIProtectedResource.photos](xcuiprotectedresource/photos.md)
  The protected resource case for access to Photos.
- [XCUIProtectedResource.bluetooth](xcuiprotectedresource/bluetooth.md)
  The protected resource case for Bluetooth utilization.
- [XCUIProtectedResource.localNetwork](xcuiprotectedresource/localnetwork.md)
  The protected resource case for finding and communicating with devices on the local network.
- [XCUIProtectedResource.microphone](xcuiprotectedresource/microphone.md)
  The protected resource case for access to the microphone.
- [XCUIProtectedResource.camera](xcuiprotectedresource/camera.md)
  The protected resource case for access to the camera.
- [XCUIProtectedResource.health](xcuiprotectedresource/health.md)
  The protected resource case for access to Health data.
- [XCUIProtectedResource.homeKit](xcuiprotectedresource/homekit.md)
  The protected resource case for access to Home data.
- [XCUIProtectedResource.mediaLibrary](xcuiprotectedresource/medialibrary.md)
  The protected resource case for access to the media library.
- [XCUIProtectedResource.keyboardNetwork](xcuiprotectedresource/keyboardnetwork.md)
  The protected resource case for access to the keyboard network.
- [XCUIProtectedResource.systemRootDirectory](xcuiprotectedresource/systemrootdirectory.md)
  The protected resource case for access to the system root directory.
- [XCUIProtectedResource.userDesktopDirectory](xcuiprotectedresource/userdesktopdirectory.md)
  The protected resource case for access to the Desktop directory.
- [XCUIProtectedResource.userDocumentsDirectory](xcuiprotectedresource/userdocumentsdirectory.md)
  The protected resource case for access to the Documents directory.
- [XCUIProtectedResource.userDownloadsDirectory](xcuiprotectedresource/userdownloadsdirectory.md)
  The protected resource case for access to the Downloads directory.
- [XCUIProtectedResource.focus](xcuiprotectedresource/focus.md)
  The protected resource case to see and share Focus status.
- [XCUIProtectedResource.removableVolumes](xcuiprotectedresource/removablevolumes.md)
  The protected resource case for access to removable volumes.
- [XCUIProtectedResource.networkVolumes](xcuiprotectedresource/networkvolumes.md)
  The protected resource case for access to network volumes.
- [XCUIProtectedResource.appleEvents](xcuiprotectedresource/appleevents.md)
  The protected resource case for the use of Apple Events.
### Initializers
- [init?(rawValue: Int)](xcuiprotectedresource/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](xcuiprotectedresource/equatable-implementations.md)
- [RawRepresentable Implementations](xcuiprotectedresource/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func resetAuthorizationStatus(for: XCUIProtectedResource)](xcuiapplication/resetauthorizationstatus(for:).md)
  Resets the authorization status for a protected resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiprotectedresource)*