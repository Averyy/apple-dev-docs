# XCUIApplication

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

A proxy that can launch, monitor, and terminate a test application.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIApplication
```

```objc
@interface XCUIApplication : XCUIElement
```

## Mentions

- [Recording UI automation for testing](./recording-ui-automation-for-testing.md)

## Overview

Use this class to launch, monitor, and terminate your app in a UI test. Use [`wait(for:timeout:)`](./xcuiapplication/wait%28for,timeout%29.md) to launch your app and wait for it to reach an expected state before you check test conditions.

## Topics

### Creating an application proxy
- [init()](./xcuiapplication/init%28%29.md)
  Creates a proxy for the application that’s configured as the Target Application in Xcode’s target settings.
- [init(bundleIdentifier: String)](./xcuiapplication/init%28bundleidentifier%29.md)
  Creates a proxy for an application for the specified bundle identifier.
- [init(url: URL)](./xcuiapplication/init%28url%29-90e7z.md)
  Creates a proxy for the application at the specified file system URL.
- [+ new](./xcuiapplication/new.md)
  Creates a proxy for the application specified as the Target Application in Xcode’s target settings.
### Launching the application
- [func launch()](./xcuiapplication/launch%28%29.md)
  Launches the application.
- [var launchArguments: [String]](./xcuiapplication/launcharguments.md)
  The arguments that pass to the application on launch.
- [var launchEnvironment: [String : String]](./xcuiapplication/launchenvironment.md)
  The environment variables that pass to the application on launch.
- [func open(URL)](./xcuiapplication/open%28_%29.md)
  Launches the application by URL.
### Activating the application
- [func activate()](./xcuiapplication/activate%28%29.md)
  Activates the application.
### Terminating the application
- [func terminate()](./xcuiapplication/terminate%28%29.md)
  Terminates any running instance of the application.
### Determining application state
- [var state: XCUIApplication.State](./xcuiapplication/state-swift.property.md)
  The most recent state of the application.
- [XCUIApplication.State](./xcuiapplication/state-swift.enum.md)
  The possible states of an application during UI testing.
### Waiting for an application state
- [func wait(for: XCUIApplication.State, timeout: TimeInterval) -> Bool](./xcuiapplication/wait%28for,timeout%29.md)
  Waits for the application to reach the specified state or timeout.
### Resetting authorization status
- [func resetAuthorizationStatus(for: XCUIProtectedResource)](./xcuiapplication/resetauthorizationstatus%28for%29.md)
  Resets the authorization status for a protected resource.
- [enum XCUIProtectedResource](./xcuiprotectedresource.md)
  A system resource that requires user authorization to access.
### Performing an accessibility audit
- [func performAccessibilityAudit(for: XCUIAccessibilityAuditType, ((XCUIAccessibilityAuditIssue) throws -> Bool)?) throws](./xcuiapplication/performaccessibilityaudit%28for,_%29.md)
- [struct XCUIAccessibilityAuditType](./xcuiaccessibilityaudittype.md)
- [class XCUIAccessibilityAuditIssue](./xcuiaccessibilityauditissue.md)
- [- performAccessibilityAuditWithAuditTypes:issueHandler:error:](./xcuiapplication/performaccessibilityauditwithaudittypes_issuehandler_error_.md)
### Initializers
- [init(URL: URL)](./xcuiapplication/init%28url%29-6ga10.md)

## Relationships

### Inherits From
- [XCUIElement](./xcuielement.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [XCUIElementAttributes](./xcuielementattributes.md)
- [XCUIElementSnapshotProviding](./xcuielementsnapshotproviding.md)
- [XCUIElementTypeQueryProvider](./xcuielementtypequeryprovider.md)
- [XCUIScreenshotProviding](./xcuiscreenshotproviding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication)*