# XCUIApplication

**Framework**: XCUIAutomation  
**Kind**: class

A proxy that can launch, monitor, and terminate a test application.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIApplication
```

## Mentions

- [Recording UI automation for testing](recording-ui-automation-for-testing.md)

#### Overview

Use this class to launch, monitor, and terminate your app in a UI test. Use [`wait(for:timeout:)`](xcuiapplication/wait(for:timeout:).md) to launch your app and wait for it to reach an expected state before you check test conditions.

## Topics

### Creating an application proxy
- [init()](xcuiapplication/init.md)
  Creates a proxy for the application that’s configured as the Target Application in Xcode’s target settings.
- [init(bundleIdentifier: String)](xcuiapplication/init(bundleidentifier:).md)
  Creates a proxy for an application for the specified bundle identifier.
- [init(url: URL)](xcuiapplication/init(url:).md)
  Creates a proxy for the application at the specified file system URL.
### Launching the application
- [func launch()](xcuiapplication/launch.md)
  Launches the application.
- [var launchArguments: [String]](xcuiapplication/launcharguments.md)
  The arguments that pass to the application on launch.
- [var launchEnvironment: [String : String]](xcuiapplication/launchenvironment.md)
  The environment variables that pass to the application on launch.
- [func open(URL)](xcuiapplication/open(_:).md)
  Launches the application by URL.
### Activating the application
- [func activate()](xcuiapplication/activate.md)
  Activates the application.
### Terminating the application
- [func terminate()](xcuiapplication/terminate.md)
  Terminates any running instance of the application.
### Determining application state
- [var state: XCUIApplication.State](xcuiapplication/state-swift.property.md)
  The most recent state of the application.
- [XCUIApplication.State](xcuiapplication/state-swift.enum.md)
  The possible states of an application during UI testing.
### Waiting for an application state
- [func wait(for: XCUIApplication.State, timeout: TimeInterval) -> Bool](xcuiapplication/wait(for:timeout:).md)
  Waits for the application to reach the specified state or timeout.
### Resetting authorization status
- [func resetAuthorizationStatus(for: XCUIProtectedResource)](xcuiapplication/resetauthorizationstatus(for:).md)
  Resets the authorization status for a protected resource.
- [enum XCUIProtectedResource](xcuiprotectedresource.md)
  A system resource that requires user authorization to access.
### Performing an accessibility audit
- [func performAccessibilityAudit(for: XCUIAccessibilityAuditType, ((XCUIAccessibilityAuditIssue) throws -> Bool)?) throws](xcuiapplication/performaccessibilityaudit(for:_:).md)
- [struct XCUIAccessibilityAuditType](xcuiaccessibilityaudittype.md)
- [class XCUIAccessibilityAuditIssue](xcuiaccessibilityauditissue.md)

## Relationships

### Inherits From
- [XCUIElement](xcuielement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [XCUIElementAttributes](xcuielementattributes.md)
- [XCUIElementSnapshotProviding](xcuielementsnapshotproviding.md)
- [XCUIElementTypeQueryProvider](xcuielementtypequeryprovider.md)
- [XCUIScreenshotProviding](xcuiscreenshotproviding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication)*