# UIScreen

**Framework**: UIKit  
**Kind**: class

An object that defines the properties associated with a hardware-based display.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class UIScreen
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)
- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

A [`UIScreen`](uiscreen.md) object provides information about the screens attached to an iOS, iPadOS, or tvOS device. A screen object for an iOS or iPadOS device has information about the integrated display or an attached display. A screen object for a tvOS device represents the television connected to the device. In a compatible iPad or iPhone app running in visionOS, don’t rely on screen-related properties to configure your app.

You don’t create any of these screen objects directly. Instead, fetch the screen object for one of your app’s windows from the [`UIWindowScene`](uiwindowscene.md) object that manages the window.

Avoid using screen objects to make decisions about your app’s interface. Use a screen object only as needed to retrieve screen-related information, such as the screen’s bounds rectangle, brightness, and overscan settings. Apps that rely on the screen dimensions can use the object in the [`fixedCoordinateSpace`](uiscreen/fixedcoordinatespace.md) property as a fixed point of reference for any calculations they must make.

## Topics

### Getting the coordinate space
- [var coordinateSpace: any UICoordinateSpace](uiscreen/coordinatespace.md)
  The current coordinate space of the screen.
- [var fixedCoordinateSpace: any UICoordinateSpace](uiscreen/fixedcoordinatespace.md)
  The fixed coordinate space of the screen.
### Getting the size and scale
- [var bounds: CGRect](uiscreen/bounds.md)
  The bounding rectangle of the screen, measured in points.
- [var nativeBounds: CGRect](uiscreen/nativebounds.md)
  The bounding rectangle of the physical screen, measured in pixels.
- [var nativeScale: CGFloat](uiscreen/nativescale.md)
  The native scale factor for the physical screen.
- [var scale: CGFloat](uiscreen/scale.md)
  The natural scale factor associated with the screen.
### Managing brightness
- [var brightness: CGFloat](uiscreen/brightness.md)
  The brightness level of the screen.
- [var wantsSoftwareDimming: Bool](uiscreen/wantssoftwaredimming.md)
  A Boolean value that indicates whether the screen may be dimmed lower than the hardware is normally capable of by emulating it in software.
### Managing screen modes
- [var currentMode: UIScreenMode?](uiscreen/currentmode.md)
  The current screen mode associated with the screen.
- [var preferredMode: UIScreenMode?](uiscreen/preferredmode.md)
  The preferred display mode for the screen.
- [var availableModes: [UIScreenMode]](uiscreen/availablemodes.md)
  The display modes that can be associated with the screen.
### Managing overscan compensation
- [var overscanCompensationInsets: UIEdgeInsets](uiscreen/overscancompensationinsets.md)
  The edge inset values needed to avoid clipping the rectangle.
- [var overscanCompensation: UIScreen.OverscanCompensation](uiscreen/overscancompensation-swift.property.md)
  For an external screen, this property sets the desired technique to compensate for overscan.
- [UIScreen.OverscanCompensation](uiscreen/overscancompensation-swift.enum.md)
  Describes different techniques for compensating for pixel loss at the edge of the screen.
### Getting the calibrated latency
- [var calibratedLatency: CFTimeInterval](uiscreen/calibratedlatency.md)
  The user-calibrated latency for the current screen.
### Getting the reference display mode status
- [var referenceDisplayModeStatus: UIScreen.ReferenceDisplayModeStatus](uiscreen/referencedisplaymodestatus-swift.property.md)
  The status of the screen’s reference display mode.
- [UIScreen.ReferenceDisplayModeStatus](uiscreen/referencedisplaymodestatus-swift.enum.md)
  Describes a screen’s reference display mode status.
- [var currentEDRHeadroom: CGFloat](uiscreen/currentedrheadroom.md)
  The screen’s current headroom when displaying extended dynamic range content.
- [var potentialEDRHeadroom: CGFloat](uiscreen/potentialedrheadroom.md)
  The screen’s maximum headroom when displaying extended dynamic range content.
### Getting a display link
- [func displayLink(withTarget: Any, selector: Selector) -> CADisplayLink?](uiscreen/displaylink(withtarget:selector:).md)
  Returns a display link object for the current screen.
- [var maximumFramesPerSecond: Int](uiscreen/maximumframespersecond.md)
  The maximum number of frames per second a screen can render.
### Capturing a snapshot
- [func snapshotView(afterScreenUpdates: Bool) -> UIView](uiscreen/snapshotview(afterscreenupdates:).md)
  Returns a snapshot view based on the current screen contents.
### Detecting screen capture
- [var isCaptured: Bool](uiscreen/iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.
- [var mirrored: UIScreen?](uiscreen/mirrored.md)
  The screen an external display mirrors from.
### Notifications
- [class let brightnessDidChangeNotification: NSNotification.Name](uiscreen/brightnessdidchangenotification.md)
  A notification that posts when a screen’s brightness changes.
- [class let modeDidChangeNotification: NSNotification.Name](uiscreen/modedidchangenotification.md)
  A notification that posts when a screen’s mode changes.
- [class let capturedDidChangeNotification: NSNotification.Name](uiscreen/captureddidchangenotification.md)
  A notification that posts when the capture status of a screen changes.
- [class let referenceDisplayModeStatusDidChangeNotification: NSNotification.Name](uiscreen/referencedisplaymodestatusdidchangenotification.md)
  A notification that posts when there’s a change to a screen’s reference display mode status.
### Deprecated
- [Deprecated symbols](uiscreen-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

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
- [Sendable](../Swift/Sendable.md)
- [UITraitEnvironment](uitraitenvironment.md)

## See Also

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)
  Fill connected displays with additional content from your app.
- [class UIScreenMode](uiscreenmode.md)
  A possible set of attributes that can apply to a screen object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen)*