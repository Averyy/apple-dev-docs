# XCUICoordinate

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

A location on screen relative to a UI element.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUICoordinate
```

```objc
@interface XCUICoordinate : NSObject
```

## Overview

Coordinates are dynamic, like the elements to which they refer, and may compute different screen locations at different times, or be invalid if the element they reference doesn’t exist.

## Topics

### Getting coordinate properties
- [var referencedElement: XCUIElement](./xcuicoordinate/referencedelement.md)
  The element that the coordinate is based on, either directly or through the coordinate from which it was derived.
- [var screenPoint: CGPoint](./xcuicoordinate/screenpoint.md)
  The dynamically computed value of the coordinate’s location on screen.
### Moving the pointer
- [func hover()](./xcuicoordinate/hover%28%29.md)
  Moves the pointer to the coordinate.
### Clicking
- [func click()](./xcuicoordinate/click%28%29.md)
  Sends a click event at the coordinate.
- [func click(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](./xcuicoordinate/click%28forduration,thendragto%29.md)
  Clicks and holds for a duration you specify, then drags to the other coordinate.
- [func click(forDuration: TimeInterval, thenDragTo: XCUICoordinate, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](./xcuicoordinate/click%28forduration,thendragto,withvelocity,thenholdforduration%29.md)
  Clicks and holds for a duration, drags at a velocity, and holds over the other coordinate for a duration, all of which you specify.
- [func doubleClick()](./xcuicoordinate/doubleclick%28%29.md)
  Sends a double-click event at the coordinate.
- [func rightClick()](./xcuicoordinate/rightclick%28%29.md)
  Sends a Control-click event at the coordinate.
### Scrolling
- [func scroll(byDeltaX: CGFloat, deltaY: CGFloat)](./xcuicoordinate/scroll%28bydeltax,deltay%29.md)
  Scrolls the view by the number of x and y pixels you specify.
### Tapping and pressing
- [func tap()](./xcuicoordinate/tap%28%29.md)
  Sends a tap event at the coordinate.
- [func doubleTap()](./xcuicoordinate/doubletap%28%29.md)
  Sends a double-tap event at the coordinate.
- [func press(forDuration: TimeInterval)](./xcuicoordinate/press%28forduration%29.md)
  Initiates a press-and-hold gesture at the coordinate, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](./xcuicoordinate/press%28forduration,thendragto%29.md)
  Initiates a press-and-hold gesture at the coordinate, then drags to another coordinate.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](./xcuicoordinate/press%28forduration,thendragto,withvelocity,thenholdforduration%29.md)
  Initiates a press-and-hold gesture, drags to another coordinate with a velocity you specify, and holds for a duration you specify.
### Performing gestures
- [func swipeLeft()](./xcuicoordinate/swipeleft%28%29.md)
  Sends a swipe-left gesture.
- [func swipeLeft(velocity: XCUIGestureVelocity)](./xcuicoordinate/swipeleft%28velocity%29.md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight()](./xcuicoordinate/swiperight%28%29.md)
  Sends a swipe-right gesture.
- [func swipeRight(velocity: XCUIGestureVelocity)](./xcuicoordinate/swiperight%28velocity%29.md)
  Sends a swipe-right gesture with a velocity you specify.
- [func swipeUp()](./xcuicoordinate/swipeup%28%29.md)
  Sends a swipe-up gesture.
- [func swipeUp(velocity: XCUIGestureVelocity)](./xcuicoordinate/swipeup%28velocity%29.md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeDown()](./xcuicoordinate/swipedown%28%29.md)
  Sends a swipe-down gesture.
- [func swipeDown(velocity: XCUIGestureVelocity)](./xcuicoordinate/swipedown%28velocity%29.md)
  Sends a swipe-down gesture with a velocity you specify.
### Creating relative coordinates
- [func withOffset(CGVector) -> XCUICoordinate](./xcuicoordinate/withoffset%28_%29.md)
  Creates a new coordinate with an absolute offset in points from the original coordinate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### UI elements
- [class XCUIElement](./xcuielement.md)
  A UI element in an application.
- [protocol XCUIElementAttributes](./xcuielementattributes.md)
  Attributes exposed by UI elements.
- [protocol XCUIElementSnapshot](./xcuielementsnapshot.md)
  A set of attributes to express a snapshot of an element’s attributes and descendant user interface hierarchy.
- [protocol XCUIElementSnapshotProviding](./xcuielementsnapshotproviding.md)
  A method to capture a snapshot of an element’s attributes and descendant user interface hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate)*