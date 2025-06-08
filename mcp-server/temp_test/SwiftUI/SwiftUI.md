# SwiftUI

**Framework**: SwiftUI  
**Kind**: module

Declare the user interface and behavior for your app on every platform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

#### Overview

SwiftUI provides views, controls, and layout structures for declaring your app’s user interface. The framework provides event handlers for delivering taps, gestures, and other types of input to your app, and tools to manage the flow of data from your app’s models down to the views and controls that users see and interact with.

Define your app structure using the [`App`](app.md) protocol, and populate it with scenes that contain the views that make up your app’s user interface. Create your own custom views that conform to the [`View`](view.md) protocol, and compose them with SwiftUI views for displaying text, images, and custom shapes using stacks, lists, and more. Apply powerful modifiers to built-in views and your own views to customize their rendering and interactivity. Share code between apps on multiple platforms with views and controls that adapt to their context and presentation.

![A screenshot of Xcode showing an app and its preview.](https://docs-assets.developer.apple.com/published/fab1d65d44232c5a0be4c36d8c6a763b/SwiftUI-Hero%402x.png)

You can integrate SwiftUI views with objects from the [`UIKit`](https://developer.apple.com/documentation/UIKit), [`AppKit`](https://developer.apple.com/documentation/AppKit), and [`WatchKit`](https://developer.apple.com/documentation/WatchKit) frameworks to take further advantage of platform-specific functionality. You can also customize accessibility support in SwiftUI, and localize your app’s interface for different languages, countries, or cultural regions.

##### Featured Samples

## Topics

### Essentials
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [Learning SwiftUI](https://developer.apple.com/tutorials/swiftui-concepts)
  Discover tips and techniques for building multiplatform apps with this set of conceptual articles and sample code.
- [Exploring SwiftUI Sample Apps](https://developer.apple.com/tutorials/Sample-Apps)
  Explore these SwiftUI samples using Swift Playgrounds on iPad or in Xcode to learn about defining user interfaces, responding to user interactions, and managing data flow.
- [SwiftUI updates](../Updates/SwiftUI.md)
  Learn about important changes to SwiftUI.
### App structure
- [App organization](app-organization.md)
  Define the entry point and top-level structure of your app.
- [Scenes](scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](documents.md)
  Enable people to open and manage documents.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](search.md)
  Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.
### Data and storage
- [Model data](model-data.md)
  Manage the data that your app uses to drive its interface.
- [Environment values](environment-values.md)
  Share data throughout a view hierarchy using the environment.
- [Preferences](preferences.md)
  Indicate configuration preferences from views to their container views.
- [Persistent storage](persistent-storage.md)
  Store data for use across sessions of your app.
### Views
- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.
### View layout
- [Layout fundamentals](layout-fundamentals.md)
  Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md)
  Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](custom-layout.md)
  Place views in custom arrangements and create animated transitions between layout types.
- [Lists](lists.md)
  Display a structured, scrollable column of information.
- [Tables](tables.md)
  Display selectable, sortable data arranged in rows and columns.
- [View groupings](view-groupings.md)
  Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](scroll-views.md)
  Enable people to scroll to content that doesn’t fit in the current display.
### Event handling
- [Gestures](gestures.md)
  Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](input-events.md)
  Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](clipboard.md)
  Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Drag and drop](drag-and-drop.md)
  Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](focus.md)
  Identify and control which visible object responds to user interaction.
- [System events](system-events.md)
  React to system events, like opening a URL.
### Accessibility
- [Accessibility fundamentals](accessibility-fundamentals.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](accessible-appearance.md)
  Enhance the legibility of content in your app’s interface.
- [Accessible controls](accessible-controls.md)
  Improve access to actions that your app can undertake.
- [Accessible descriptions](accessible-descriptions.md)
  Describe interface elements to help people understand what they represent.
- [Accessible navigation](accessible-navigation.md)
  Enable users to navigate to specific user interface elements using rotors.
### Framework integration
- [AppKit integration](appkit-integration.md)
  Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.
- [UIKit integration](uikit-integration.md)
  Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.
- [WatchKit integration](watchkit-integration.md)
  Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
- [Technology-specific views](technology-specific-views.md)
  Use SwiftUI views that other Apple frameworks provide.
### Tool support
- [Previews in Xcode](previews-in-xcode.md)
  Generate dynamic, interactive previews of your custom views.
- [Xcode library customization](xcode-library-customization.md)
  Expose custom views and modifiers in the Xcode library.
### Protocols
- [protocol GlassBackgroundEffect](glassbackgroundeffect.md)
  A specification for the appearance of a glass background.
### Structures
- [struct AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md)
  The automatic glass background effect.
- [struct ContentToolbarPlacement](contenttoolbarplacement.md)
- [struct FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md)
  The feathered glass background effect.
- [struct GlassBackgroundEffectConfiguration](glassbackgroundeffectconfiguration.md)
  A configuration used to build a custom effect.
- [struct PlateGlassBackgroundEffect](plateglassbackgroundeffect.md)
  The plate glass background effect.
- [struct ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md)
  Properties influencing the scroll view a scroll target behavior applies to.
- [struct ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md)
  The context in which a scroll target behavior can decide its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI)*