# XCUIAutomation

**Framework**: XCUIAutomation  
**Kind**: module

Replicate sequences of interactions and make sure that your app’s user interface behaves as intended.

**Availability**:
- Xcode 16.3+

#### Overview

UI testing lets you verify that when you change parts of your app’s data model, your app’s view controllers, views, and controls respond appropriately. You can also create test cases to manipulate your app’s views and controls, as if a person is interacting with your interface. Use the XCUIAutomation framework to control your app’s user interface and inspect its state. Use [`XCTest`](https://developer.apple.com/documentation/XCTest) to write tests that control your app using XCUIAutomation, and check if your app’s state matches your expectations.

> **Note**:  UI testing isn’t available to apps you build using the visionOS SDK. You can still use it to test compatible iPad and iPhone apps that you build using the iOS SDK but run in visionOS.

## Topics

### Essentials
- [Recording UI automation for testing](recording-ui-automation-for-testing.md)
  Capture and replay interaction sequences to verify your app’s behavior.
### UI element queries
- [class XCUIElementQuery](xcuielementquery.md)
  An object that defines the search criteria a test uses to identify UI elements.
- [protocol XCUIElementTypeQueryProvider](xcuielementtypequeryprovider.md)
  A type that provides ready-made queries for locating descendant UI elements.
### UI elements
- [class XCUIElement](xcuielement.md)
  A UI element in an application.
- [protocol XCUIElementAttributes](xcuielementattributes.md)
  Attributes exposed by UI elements.
- [protocol XCUIElementSnapshot](xcuielementsnapshot.md)
  A set of attributes to express a snapshot of an element’s attributes and descendant user interface hierarchy.
- [protocol XCUIElementSnapshotProviding](xcuielementsnapshotproviding.md)
  A method to capture a snapshot of an element’s attributes and descendant user interface hierarchy.
- [class XCUICoordinate](xcuicoordinate.md)
  A location on screen relative to a UI element.
### Application lifecycle
- [class XCUIApplication](xcuiapplication.md)
  A proxy that can launch, monitor, and terminate a test application.
### Screenshots
- [class XCUIScreen](xcuiscreen.md)
  A physical screen attached to a device.
- [class XCUIScreenshot](xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.
- [protocol XCUIScreenshotProviding](xcuiscreenshotproviding.md)
  A type that can provide a screenshot of its current UI state.
### Device simulation
- [class XCUIDevice](xcuidevice.md)
  A proxy that can simulate physical buttons, device orientation, and Siri interaction for an iOS, watchOS, or tvOS device.
- [class XCUISystem](xcuisystem.md)
  A proxy that provides an interface to OS-specific properties and actions.
- [class XCUISiriService](xcuisiriservice.md)
  A proxy that simulates a device’s Siri interface.
### Remote control simulation
- [class XCUIRemote](xcuiremote.md)
  A class that simulates interaction with a physical remote control.
### UI testing availability
- [var XCUI_UI_TESTING_AVAILABLE: Int32](xcui_ui_testing_available.md)
  Indicates whether the current environment supports UI testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/XCUIAutomation)*