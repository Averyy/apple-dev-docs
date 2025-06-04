# Building watchOS app Interfaces Using the Storyboard

**Framework**: Watchkit

Create the user interface for your watchOS app by nesting stacks.

## Overview

watchOS apps use a simplified, stack-based layout model for their user interfaces. Xcode automatically groups elements into horizontal and vertical stacks, and you can fine-tune the layout by modifying the element’s attributes. Additionally, you can ensure that your interface works as expected on all Apple Watch sizes by using resizable elements and size-specific customizations.

As you add items to the storyboard, Xcode stacks them vertically, with each item on its own line ([`Figure 1`](https://developer.apple.com/documentation/watchkit/storyboard_support/building_watchos_app_interfaces_using_the_storyboard#3295988)).

Use Groups to create horizontal or vertical stacks ([`Figure 2`](https://developer.apple.com/documentation/watchkit/storyboard_support/building_watchos_app_interfaces_using_the_storyboard#3172421)). Groups don’t have a default visual representation, but you can configure a background color or image as needed. Nest Groups, as necessary, to create more complex layouts.

You can fine-tune an interface element’s size and layout using the Attributes inspector. All interface elements have the following attributes:

Groups provide additional options to manage their content:

## Topics

### Controls
- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/connecting-your-user-interface-to-your-code))
  Connect the interface objects in your storyboard to outlets and action methods in your WatchKit extension.
### Navigation
- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))
  Help users navigate between interface controllers.

## See Also

- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard)*