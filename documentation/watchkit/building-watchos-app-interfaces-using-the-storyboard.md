# Building watchOS app Interfaces Using the Storyboard

**Framework**: WatchKit

Create the user interface for your watchOS app by nesting stacks.

#### Overview

watchOS apps use a simplified, stack-based layout model for their user interfaces. Xcode automatically groups elements into horizontal and vertical stacks, and you can fine-tune the layout by modifying the element’s attributes. Additionally, you can ensure that your interface works as expected on all Apple Watch sizes by using resizable elements and size-specific customizations.

As you add items to the storyboard, Xcode stacks them vertically, with each item on its own line ([`Figure 1`](storyboard_support/building_watchos_app_interfaces_using_the_storyboard#3295988.md)).

![A screenshot of a storyboard scene with three buttons stacked horizontally.](https://docs-assets.developer.apple.com/published/9100c5dcbc2e2dd9efdbda264280e41f/media-3295988%402x.png)

Use Groups to create horizontal or vertical stacks ([`Figure 2`](storyboard_support/building_watchos_app_interfaces_using_the_storyboard#3172421.md)). Groups don’t have a default visual representation, but you can configure a background color or image as needed. Nest Groups, as necessary, to create more complex layouts.

![A screenshot with a Group containing a horizontal stack of buttons.](https://docs-assets.developer.apple.com/published/9799d1483038c93393bfd7c9cb936929/media-3172421%402x.png)

##### Customize the Layout Using Attributes

You can fine-tune an interface element’s size and layout using the Attributes inspector. All interface elements have the following attributes:

Groups provide additional options to manage their content:

## Topics

### Controls
- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md)
  Connect the interface objects in your storyboard to outlets and action methods in your WatchKit extension.
### Navigation
- [Navigating Between Scenes](navigating-between-scenes.md)
  Help users navigate between interface controllers.

## See Also

- [class WKInterfaceObject](wkinterfaceobject.md)
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKInterfaceController](wkinterfacecontroller.md)
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAlertAction](wkalertaction.md)
  An object that encapsulates information about a button displayed in an alert or action sheet.
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md)
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md)
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md)
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard)*