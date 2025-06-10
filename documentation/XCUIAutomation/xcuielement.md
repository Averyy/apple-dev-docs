# XCUIElement

**Framework**: XCUIAutomation  
**Kind**: class

A UI element in an application.

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
class XCUIElement
```

#### Overview

In macOS and iPadOS 15 and later, [`XCUIElement`](xcuielement.md) provides a way to test your app with keyboard and mouse interactions, such as typing, clicking, scrolling, and moving and pausing the pointer. In iOS, [`XCUIElement`](xcuielement.md) provides a way to test your app with gestures, such as tapping, swiping, pinching, and rotating.

> **Note**:  [`XCUIElement`](xcuielement.md) adopts the [`XCUIElementAttributes`](xcuielementattributes.md) protocol, which provides additional properties for querying the current state of a UI element’s attributes.

## Topics

### Querying element state
- [func waitForExistence(timeout: TimeInterval) -> Bool](xcuielement/waitforexistence(timeout:).md)
  Waits the specified amount of time for an element to exist.
- [func waitForNonExistence(timeout: TimeInterval) -> Bool](xcuielement/waitfornonexistence(timeout:).md)
  Waits the specified amount of time for an element to no longer exist.
- [func wait<V>(for: KeyPath<XCUIElement, V>, toEqual: V, timeout: TimeInterval) -> Bool](xcuielement/wait(for:toequal:timeout:).md)
  Waits a specified amount of time for a property value to equal a specified value.
- [var exists: Bool](xcuielement/exists.md)
  Determines if the element exists.
- [var isHittable: Bool](xcuielement/ishittable.md)
  Determines if the system can compute a hit point for the element.
- [var debugDescription: String](xcuielement/debugdescription.md)
  Provides debugging information about the element.
### Querying descendant elements
- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](xcuielement/children(matching:).md)
  Returns a query for all direct children of the element matching the type you specify.
- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](xcuielement/descendants(matching:).md)
  Returns a query for all descendants of the element matching the type you specify.
### Typing text
- [func typeText(String)](xcuielement/typetext(_:).md)
  Types a string into the element.
### Combining keystrokes
- [func typeKey(XCUIKeyboardKey, modifierFlags: XCUIElement.KeyModifierFlags)](xcuielement/typekey(_:modifierflags:)-6gaoi.md)
  Types a single key from the XCUIKeyboardKey enumeration with the specified modifier flags.
- [func typeKey(String, modifierFlags: XCUIElement.KeyModifierFlags)](xcuielement/typekey(_:modifierflags:)-9ubn.md)
  Types a single key that a string represents with the flags you specify.
- [struct XCUIKeyboardKey](xcuikeyboardkey.md)
  Constants to represent keys that have no typewritten equivalent.
- [class func perform(withKeyModifiers: XCUIElement.KeyModifierFlags, block: () -> Void)](xcuielement/perform(withkeymodifiers:block:).md)
  Executes a block of code while holding a combination keystroke.
- [XCUIElement.KeyModifierFlags](xcuielement/keymodifierflags.md)
  Flags for simulating combination keystrokes with keys, such as Control, Option, Shift, and Command.
### Moving the pointer
- [func hover()](xcuielement/hover.md)
  Moves the pointer over the element.
### Clicking
- [func click()](xcuielement/click.md)
  Sends a click event to a hittable point computed for the element.
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement)](xcuielement/click(forduration:thendragto:).md)
  Clicks and holds an element for a duration you specify, and then drags it to another element.
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](xcuielement/click(forduration:thendragto:withvelocity:thenholdforduration:).md)
  Clicks and holds an element for a duration, drags it at a velocity, and holds it over another element for a duration, all of which you specify.
- [func doubleClick()](xcuielement/doubleclick.md)
  Sends a double-click event to a hittable point the system computes for the element.
- [func rightClick()](xcuielement/rightclick.md)
  Sends a Control-click event to a hittable point the system computes for the element.
### Scrolling
- [func scroll(byDeltaX: CGFloat, deltaY: CGFloat)](xcuielement/scroll(bydeltax:deltay:).md)
  Scrolls the view by the number of x and y pixels you specify.
### Tapping and pressing
- [func tap()](xcuielement/tap.md)
  Sends a tap event to a hittable point the system computes for the element.
- [func doubleTap()](xcuielement/doubletap.md)
  Sends a double-tap event to a hittable point the system computes for the element.
- [func press(forDuration: TimeInterval)](xcuielement/press(forduration:).md)
  Sends a press-and-hold gesture to a hittable point the system computes for the element, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement)](xcuielement/press(forduration:thendragto:).md)
  Initiates a press-and-hold gesture, then drags to another element.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](xcuielement/press(forduration:thendragto:withvelocity:thenholdforduration:).md)
  Initiates a press-and-hold gesture, drags to another element at a velocity, and holds for a duration, all of which you specify.
### Tapping multiple times
- [func twoFingerTap()](xcuielement/twofingertap.md)
  Sends a two-finger tap event to a hittable point the system computes for the element.
- [func tap(withNumberOfTaps: Int, numberOfTouches: Int)](xcuielement/tap(withnumberoftaps:numberoftouches:).md)
  Sends one or more taps with one or more touch points.
### Performing gestures
- [func swipeLeft()](xcuielement/swipeleft.md)
  Sends a swipe-left gesture.
- [func swipeLeft(velocity: XCUIGestureVelocity)](xcuielement/swipeleft(velocity:).md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight()](xcuielement/swiperight.md)
  Sends a swipe-right gesture.
- [func swipeRight(velocity: XCUIGestureVelocity)](xcuielement/swiperight(velocity:).md)
  Sends a swipe-right gesture with a velocity you specify.
- [func swipeUp()](xcuielement/swipeup.md)
  Sends a swipe-up gesture.
- [func swipeUp(velocity: XCUIGestureVelocity)](xcuielement/swipeup(velocity:).md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeDown()](xcuielement/swipedown.md)
  Sends a swipe-down gesture.
- [func swipeDown(velocity: XCUIGestureVelocity)](xcuielement/swipedown(velocity:).md)
  Sends a swipe-down gesture with a velocity you specify.
- [func pinch(withScale: CGFloat, velocity: CGFloat)](xcuielement/pinch(withscale:velocity:).md)
  Sends a pinching gesture with two touches.
- [func rotate(CGFloat, withVelocity: CGFloat)](xcuielement/rotate(_:withvelocity:).md)
  Sends a rotation gesture with two touches.
- [struct XCUIGestureVelocity](xcuigesturevelocity.md)
  A value that describes how fast a gesture moves across the screen, in pixels per second.
### Interacting with sliders
- [var normalizedSliderPosition: CGFloat](xcuielement/normalizedsliderposition.md)
  Returns the position of the slider’s indicator as a normalized value.
- [func adjust(toNormalizedSliderPosition: CGFloat)](xcuielement/adjust(tonormalizedsliderposition:).md)
  Manipulates the UI to change the value the slider displays to a new value, based on a normalized position.
### Interacting with pickers
- [func adjust(toPickerWheelValue: String)](xcuielement/adjust(topickerwheelvalue:).md)
  Changes the value that the picker wheel displays.
### Calculating coordinates
- [func coordinate(withNormalizedOffset: CGVector) -> XCUICoordinate](xcuielement/coordinate(withnormalizedoffset:).md)
  Creates and returns a new coordinate with a normalized offset.
### Supporting types
- [XCUIElement.ElementType](xcuielement/elementtype.md)
  The types of UI elements that you find, inspect, and interact with in a UI test.
- [XCUIElement.SizeClass](xcuielement/sizeclass.md)
  The user interface size classes you can inspect in a UI test.
- [XCUIElement.AttributeName](xcuielement/attributename.md)
  A set of string constants that serve as keys for storing element attributes in a dictionary.
### Deprecated methods
- [func swipeDown(withVelocity: XCUIGestureVelocity)](xcuielement/swipedown(withvelocity:).md)
  Sends a swipe-down gesture with a velocity you specify.
- [func swipeUp(withVelocity: XCUIGestureVelocity)](xcuielement/swipeup(withvelocity:).md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeLeft(withVelocity: XCUIGestureVelocity)](xcuielement/swipeleft(withvelocity:).md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight(withVelocity: XCUIGestureVelocity)](xcuielement/swiperight(withvelocity:).md)
  Sends a swipe-right gesture with a velocity you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [XCUIApplication](xcuiapplication.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [XCUIElementAttributes](xcuielementattributes.md)
- [XCUIElementSnapshotProviding](xcuielementsnapshotproviding.md)
- [XCUIElementTypeQueryProvider](xcuielementtypequeryprovider.md)
- [XCUIScreenshotProviding](xcuiscreenshotproviding.md)

## See Also

- [protocol XCUIElementAttributes](xcuielementattributes.md)
  Attributes exposed by UI elements.
- [protocol XCUIElementSnapshot](xcuielementsnapshot.md)
  A set of attributes to express a snapshot of an element’s attributes and descendant user interface hierarchy.
- [protocol XCUIElementSnapshotProviding](xcuielementsnapshotproviding.md)
  A method to capture a snapshot of an element’s attributes and descendant user interface hierarchy.
- [class XCUICoordinate](xcuicoordinate.md)
  A location on screen relative to a UI element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement)*