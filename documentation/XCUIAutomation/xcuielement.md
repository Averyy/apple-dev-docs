# XCUIElement

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

A UI element in an application.

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
class XCUIElement
```

```objc
@interface XCUIElement : NSObject
```

## Overview

In macOS and iPadOS 15 and later, [`XCUIElement`](./xcuielement.md) provides a way to test your app with keyboard and mouse interactions, such as typing, clicking, scrolling, and moving and pausing the pointer. In iOS, [`XCUIElement`](./xcuielement.md) provides a way to test your app with gestures, such as tapping, swiping, pinching, and rotating.

> **Note**:  [`XCUIElement`](./xcuielement.md) adopts the [`XCUIElementAttributes`](./xcuielementattributes.md) protocol, which provides additional properties for querying the current state of a UI element’s attributes.

## Topics

### Querying element state
- [func waitForExistence(timeout: TimeInterval) -> Bool](./xcuielement/waitforexistence%28timeout%29.md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](./xcuielement/waitfornonexistence%28timeout%29.md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](./xcuielement/wait%28for,toequal,timeout%29.md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](./xcuielement/exists.md)
  Determines if the element exists.
- [var isHittable: Bool](./xcuielement/ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](./xcuielement/debugdescription.md)
  Provides debugging information about the element.
### Querying descendant elements
- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](./xcuielement/children%28matching%29.md)
  Returns a query for all direct children of the element matching the type you specify.
- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](./xcuielement/descendants%28matching%29.md)
  Returns a query for all descendants of the element matching the type you specify.
### Typing text
- [func typeText(String)](./xcuielement/typetext%28_%29.md)
  Types a string into the element.
### Combining keystrokes
- [func typeKey(XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)](./xcuielement/typekey%28_,modifierflags%29-6gaoi.md)
  Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.
- [func typeKey(String, modifierFlags: XCUIElement.KeyModifierFlags)](./xcuielement/typekey%28_,modifierflags%29-9ubn.md)
  Types a single key that a string represents with the flags you specify.
- [struct XCUIKeyboardKey](./xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [class func perform(withKeyModifiers: XCUIElement.KeyModifierFlags, block: () -> Void)](./xcuielement/perform%28withkeymodifiers,block%29.md)
  Executes a block of code while holding a combination keystroke.
- [XCUIElement.KeyModifierFlags](./xcuielement/keymodifierflags.md)
  Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.
### Moving the pointer
- [func hover()](./xcuielement/hover%28%29.md)
  Moves the pointer over the element.
### Clicking
- [func click()](./xcuielement/click%28%29.md)
  Sends a click event to a hittable point computed for the element.
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement)](./xcuielement/click%28forduration,thendragto%29.md)
  Clicks and holds an element for a duration you specify, and then drags it to another element.
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](./xcuielement/click%28forduration,thendragto,withvelocity,thenholdforduration%29.md)
  Clicks and holds an element for a duration, drags it at a velocity, and holds it over another element for a duration, all of which you specify.
- [func doubleClick()](./xcuielement/doubleclick%28%29.md)
  Sends a double-click event to a hittable point the system computes for the element.
- [func rightClick()](./xcuielement/rightclick%28%29.md)
  Sends a Control-click event to a hittable point the system computes for the element.
### Scrolling
- [func scroll(byDeltaX: CGFloat, deltaY: CGFloat)](./xcuielement/scroll%28bydeltax,deltay%29.md)
  Scrolls the view by the number of x and y pixels you specify.
### Tapping and pressing
- [func tap()](./xcuielement/tap%28%29.md)
  Sends a tap event to a hittable point the system computes for the element.
- [func doubleTap()](./xcuielement/doubletap%28%29.md)
  Sends a double-tap event to a hittable point the system computes for the element.
- [func press(forDuration: TimeInterval)](./xcuielement/press%28forduration%29.md)
  Sends a press-and-hold gesture to a hittable point the system computes for the element, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement)](./xcuielement/press%28forduration,thendragto%29.md)
  Initiates a press-and-hold gesture, then drags to another element.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](./xcuielement/press%28forduration,thendragto,withvelocity,thenholdforduration%29.md)
  Initiates a press-and-hold gesture, drags to another element at a velocity, and holds for a duration, all of which you specify.
### Tapping multiple times
- [func twoFingerTap()](./xcuielement/twofingertap%28%29.md)
  Sends a two-finger tap event to a hittable point the system computes for the element.
- [func tap(withNumberOfTaps: Int, numberOfTouches: Int)](./xcuielement/tap%28withnumberoftaps,numberoftouches%29.md)
  Sends one or more taps with one or more touch points.
### Performing gestures
- [func swipeLeft()](./xcuielement/swipeleft%28%29.md)
  Sends a swipe-left gesture.
- [func swipeLeft(velocity: XCUIGestureVelocity)](./xcuielement/swipeleft%28velocity%29.md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight()](./xcuielement/swiperight%28%29.md)
  Sends a swipe-right gesture.
- [func swipeRight(velocity: XCUIGestureVelocity)](./xcuielement/swiperight%28velocity%29.md)
  Sends a swipe-right gesture with a velocity you specify.
- [func swipeUp()](./xcuielement/swipeup%28%29.md)
  Sends a swipe-up gesture.
- [func swipeUp(velocity: XCUIGestureVelocity)](./xcuielement/swipeup%28velocity%29.md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeDown()](./xcuielement/swipedown%28%29.md)
  Sends a swipe-down gesture.
- [func swipeDown(velocity: XCUIGestureVelocity)](./xcuielement/swipedown%28velocity%29.md)
  Sends a swipe-down gesture with a velocity you specify.
- [func pinch(withScale: CGFloat, velocity: CGFloat)](./xcuielement/pinch%28withscale,velocity%29.md)
  Sends a pinching gesture with two touches.
- [func rotate(CGFloat, withVelocity: CGFloat)](./xcuielement/rotate%28_,withvelocity%29.md)
  Sends a rotation gesture with two touches.
- [struct XCUIGestureVelocity](./xcuigesturevelocity.md)
  A value that describes how fast a gesture moves across the screen, in pixels per second.
### Interacting with sliders
- [var normalizedSliderPosition: CGFloat](./xcuielement/normalizedsliderposition.md)
  Returns the position of the slider’s indicator as a normalized value.
- [func adjust(toNormalizedSliderPosition: CGFloat)](./xcuielement/adjust%28tonormalizedsliderposition%29.md)
  Manipulates the UI to change the value the slider displays to a new value, based on a normalized position.
### Interacting with pickers
- [func adjust(toPickerWheelValue: String)](./xcuielement/adjust%28topickerwheelvalue%29.md)
  Changes the value that the picker wheel displays.
### Calculating coordinates
- [func coordinate(withNormalizedOffset: CGVector) -> XCUICoordinate](./xcuielement/coordinate%28withnormalizedoffset%29.md)
  Creates and returns a new coordinate with a normalized offset.
### Supporting types
- [XCUIElement.ElementType](./xcuielement/elementtype.md)
  The types of UI elements that you find, inspect, and interact with in a UI test.
- [XCUIElement.SizeClass](./xcuielement/sizeclass.md)
  The user interface size classes you can inspect in a UI test.
- [XCUIElement.AttributeName](./xcuielement/attributename.md)
  A set of string constants that serve as keys for storing element attributes in a dictionary.
### Deprecated methods
- [func swipeDown(withVelocity: XCUIGestureVelocity)](./xcuielement/swipedown%28withvelocity%29.md)
  Sends a swipe-down gesture with a velocity you specify.
- [func swipeUp(withVelocity: XCUIGestureVelocity)](./xcuielement/swipeup%28withvelocity%29.md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeLeft(withVelocity: XCUIGestureVelocity)](./xcuielement/swipeleft%28withvelocity%29.md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight(withVelocity: XCUIGestureVelocity)](./xcuielement/swiperight%28withvelocity%29.md)
  Sends a swipe-right gesture with a velocity you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [XCUIApplication](./xcuiapplication.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [XCUIElementAttributes](./xcuielementattributes.md)
- [XCUIElementSnapshotProviding](./xcuielementsnapshotproviding.md)
- [XCUIElementTypeQueryProvider](./xcuielementtypequeryprovider.md)
- [XCUIScreenshotProviding](./xcuiscreenshotproviding.md)

## See Also

### UI elements
- [protocol XCUIElementAttributes](./xcuielementattributes.md)
  Attributes exposed by UI elements.
- [protocol XCUIElementSnapshot](./xcuielementsnapshot.md)
  A set of attributes to express a snapshot of an element’s attributes and descendant user interface hierarchy.
- [protocol XCUIElementSnapshotProviding](./xcuielementsnapshotproviding.md)
  A method to capture a snapshot of an element’s attributes and descendant user interface hierarchy.
- [class XCUICoordinate](./xcuicoordinate.md)
  A location on screen relative to a UI element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement)*