# WidgetKit

**Framework**: WidgetKit  
**Kind**: module

Extend the reach of your app by creating widgets, watch complications, Live Activities, and controls.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

#### Overview

Using WidgetKit, you can make your app’s content available in contexts outside the app and extend its reach by building an ecosystem of glanceable, up-to-date experiences.

![A conceptual image that shows a small widget on iPhone, a rectangular widget on Apple Watch, and a small widget on the Mac desktop.](https://docs-assets.developer.apple.com/published/273bac77dde0ed1da3f887a44dd0a092/widgetkit-hero%402x.png)

The ecosystem that WidgetKit enables consists of:

##### Develop Glanceable Features Iteratively

WidgetKit enables features across iPad, iPhone, the Mac, Apple Watch, and Apple Vision Pro, but only in a way that best fits a person’s device and personal needs. For example, WidgetKit powers widgets on all platforms in various sizes. It also powers Live Activities and controls, features that aren’t available on Apple Vision Pro.

Even though not every feature that WidgetKit powers is available on every platform or device, widgets, Live Activities, controls, and watch complications share technology and design similarities. This makes it easy to develop features in tandem and to expand usage across contexts.

Use an iterative approach and start with support for one feature or select sizes of widgets — for example, start with a small widget as described in [`Creating a widget extension`](creating-a-widget-extension.md), but plan and design additional sizes and features across platforms from the beginning. Then allow people to view your content in as many contexts as possible. For more information, refer to [`Developing a WidgetKit strategy`](developing-a-widgetkit-strategy.md).

##### Understand Interactivity and Personalization

The WidgetKit ecosystem enables people to view your app content in new contexts and offers specific interactions with your app when and where they need it:

- People tap a widget, watch complication, or Live Activity to launch the corresponding app or the app’s scene with matching information or functionality. For example, tapping an Emoji Ranger widget or watch complication launches the scene in the app that matches the displayed hero. For more information, refer to [`Linking to specific app scenes from your widget or Live Activity`](linking-to-specific-app-scenes-from-your-widget-or-live-activity.md).
- People use buttons and toggles in widgets, controls, and Live Activities to interact with your app without launching it. For example, the large widget of the [`Emoji Rangers: Supporting Live Activities, interactivity, and animations`](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project includes a button that people tap to give the healing capability of their hero a temporary boost.

In addition to offering relevant information and specific interactivity at a glance, people use widgets, watch complications, Live Activities, and controls to personalize their devices:

- People configure widgets and watch complications to display details specific to their needs. For example, a widget of the [`Emoji Rangers: Supporting Live Activities, interactivity, and animations`](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project allows people to configure the hero that appears on the widget.
- People arrange widgets and watch complications in the way that works best for them. When they stack widgets and enable Smart Rotate on iPhone or iPad, WidgetKit automatically rotates the most relevant widget to the top, making sure people see the most important details at the right time. On Apple Watch, the Smart Stack displays widgets based on contextual relevance, and people pin a favorite widget to a fixed position in the Smart Stack.

##### Update Content with Timelines and Push Notifications

Widgets and watch complications use a special mechanism to update their content: You create a timeline of data updates and hand it to WidgetKit. WidgetKit then makes sure the widget or complication updates its content in an energy-efficient way. For more information on timelines, refer to [`Keeping a widget up to date`](keeping-a-widget-up-to-date.md). Additionally, widgets can receive updates by using the Apple Push Notification service (APNs) and remote push notifications.

Live Activities don’t use timelines to update their content. Instead, they use [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit) and ActivityKit push notifications you send with APNs. For more information, refer to [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit).

Controls don’t use timelines to update their content. Instead, your controls update their content when someone uses them, the app reloads them, or the system receives a remote push notification from APNs.

##### Create a Focused Glanceable Design

Widgets, watch complications, Live Activities, and controls are small and require a focused, glanceable design. For design guidance, refer to [`Human Interface Guidelines > Widgets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets), [`Human Interface Guidelines > Complications`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications), [`Human Interface Guidelines > Live Activities`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities), and [`Human Interface Guidelines > Controls`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/controls).

## Topics

### Essentials
- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [WidgetKit updates](../Updates/WidgetKit.md)
  Learn about important changes in WidgetKit.
### Widget creation
- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Supporting additional widget sizes](supporting-additional-widget-sizes.md)
  Offer widgets in additional contexts by adding support for various widget sizes.
- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md)
  Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [@MainActor @preconcurrency protocol Widget](../SwiftUI/Widget.md)
  The configuration and content of a widget to display on the Home screen or in Notification Center.
- [@MainActor @preconcurrency protocol WidgetBundle](../SwiftUI/WidgetBundle.md)
  A container used to expose multiple widgets from a single widget extension.
- [struct StaticConfiguration](staticconfiguration.md)
  An object describing the content of a widget that has no user-configurable options.
- [enum WidgetFamily](widgetfamily.md)
  Values that define the widget’s size and shape.
### Presentation
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [Displaying the right widget background](displaying-the-right-widget-background.md)
  Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)
  Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md)
  Ensure that your small system family widget works well in StandBy and CarPlay.
- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [SwiftUI views for widgets](swiftui-views.md)
  Present your app’s content in widgets with SwiftUI views.
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [struct WidgetRenderingMode](widgetrenderingmode.md)
  Constants that indicate the rendering mode for a widget.
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.
### visionOS widgets
- [Updating your widgets for visionOS](updating-your-widgets-for-visionos.md)
  Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [@MainActor @preconcurrency func widgetTexture(_ material: WidgetTexture) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/widgetTexture(_:).md)
  Specifies the widget texture for this widget.
- [struct WidgetTexture](widgettexture.md)
  Values that define the texture of the widget’s coating layer.
- [@MainActor @preconcurrency func supportedMountingStyles(_ styles: [WidgetMountingStyle]) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/supportedMountingStyles(_:).md)
  Specifies the mounting style for this widget.
- [struct WidgetMountingStyle](widgetmountingstyle.md)
  Values that define the widget’s supported mounting style.
- [struct LevelOfDetail](levelofdetail.md)
  The level of detail the view is recommended to have.
### Interactivity
- [Adding interactivity to widgets and Live Activities](adding-interactivity-to-widgets-and-live-activities.md)
  Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [Animating data updates in widgets and Live Activities](animating-data-updates-in-widgets-and-live-activities.md)
  Use SwiftUI animations to indicate data updates in your widgets and Live Activities.
- [Linking to specific app scenes from your widget or Live Activity](linking-to-specific-app-scenes-from-your-widget-or-live-activity.md)
  Add deep links to your widgets and Live Activities that enable people to open a specific scene in your app.
### Configurable widgets
- [Making a configurable widget](making-a-configurable-widget.md)
  Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](migrating-from-sirikit-intents-to-app-intents.md)
  Configure your widgets for backward compatibility.
- [struct AppIntentConfiguration](appintentconfiguration.md)
  An object describing the content of a widget that uses a custom intent to provide user-configurable options.
- [struct WidgetInfo](widgetinfo.md)
  A structure that contains information about user-configured widgets.
- [struct AppIntentRecommendation](appintentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.
- [struct IntentConfiguration](intentconfiguration.md)
  An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [struct IntentRecommendation](intentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.
### Timeline management
- [Keeping a widget up to date](keeping-a-widget-up-to-date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [protocol TimelineProvider](timelineprovider.md)
  A type that advises WidgetKit when to update a widget’s display.
- [protocol AppIntentTimelineProvider](appintenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.
- [protocol IntentTimelineProvider](intenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.
- [struct TimelineProviderContext](timelineprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [protocol TimelineEntry](timelineentry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [struct Timeline](timeline.md)
  An object that specifies a date for WidgetKit to update a widget’s view.
- [class WidgetCenter](widgetcenter.md)
  An object that contains a list of user-configured widgets and is used for reloading widget timelines.
### Push notification updates
- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md)
  Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- [protocol WidgetPushHandler](widgetpushhandler.md)
  A type that can receive push information about widget refreshes and relevance refreshes.
- [struct WidgetPushInfo](widgetpushinfo.md)
  A structure that contains information about the push token for updating widgets and widget relevances.
### watchOS widgets
- [struct AccessoryWidgetGroup](accessorywidgetgroup.md)
  A view type that has a label at the top and three content views masked with a circle or rounded square.
- [struct AccessoryWidgetGroupStyle](accessorywidgetgroupstyle.md)
  The style for an [`AccessoryWidgetGroup`](accessorywidgetgroup.md) view.
- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
### Accessibility
- [Adding accessible descriptions to widgets and Live Activities](../ActivityKit/adding-accessible-descriptions-to-widgets-and-live-activities.md)
  Describe the interface elements of your widgets and Live Activities to help people understand what they represent.
### Location services in widgets
- [Accessing location information in widgets](accessing-location-information-in-widgets.md)
  Incorporate location information into your widget presentation to make it more relevant and contextual.
### Networking
- [Making network requests in a widget extension](making-network-requests-in-a-widget-extension.md)
  Update your widget with new information you fetch with a network request.
### Smart Stacks
- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [struct TimelineEntryRelevance](timelineentryrelevance.md)
  An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [struct RelevanceConfiguration](relevanceconfiguration.md)
  A type that describes the content of a widget that uses relevance clues.
- [protocol RelevanceEntriesProvider](relevanceentriesprovider.md)
  A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [protocol RelevanceEntry](relevanceentry.md)
  A type that specifies the information to render a widget at a specific relevance configuration.
- [struct WidgetRelevance](widgetrelevance.md)
  A type collecting the relevances for a widget kind.
- [struct WidgetRelevanceAttribute](widgetrelevanceattribute.md)
  A type describing when a specific widget could be relevant.
- [struct WidgetRelevanceGroup](widgetrelevancegroup.md)
  A type for configuring widget behavior in the watchOS Smart Stack.
### Widget preview and debugging
- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md)
  Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Debugging widgets](debugging-widgets.md)
  Set environment variables in Xcode to control your widget’s configuration in the debugger.
- [struct WidgetPreviewContext](widgetpreviewcontext.md)
  A specification for the context of a widget preview.
- [Preview macros](preview-macros.md)
  Use Swift macros to create widget previews in Xcode.
### Live Activities
- [struct ActivityConfiguration](activityconfiguration.md)
  An object that describes the content of a Live Activity.
- [struct DynamicIsland](dynamicisland.md)
  The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [let NSUserActivityTypeLiveActivity: String](nsuseractivitytypeliveactivity.md)
  A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [enum ActivityPreviewViewKind](activitypreviewviewkind.md)
  Values that represent Live Activity presentations for use in Xcode previews.
- [enum ActivityFamily](activityfamily.md)
  A family that defines the Live Activity’s size.
### Controls
- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md)
  Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md)
  Customize the way controls display across the system and offer people the ability to configure them.
- [struct ControlWidgetToggle](controlwidgettoggle.md)
  A control template representing a toggle.
- [class ControlCenter](controlcenter.md)
  An object that contains a list of user-configured controls and is used for reloading controls.
- [struct ControlWidgetButton](controlwidgetbutton.md)
  A control template representing a button.
### Control values and previews
- [protocol ControlValueProvider](controlvalueprovider.md)
  A type that provides a value to a control widget template.
- [protocol AppIntentControlValueProvider](appintentcontrolvalueprovider.md)
  A type that uses a custom intent to provide a value to a control template.
### Control configuration
- [struct StaticControlConfiguration](staticcontrolconfiguration.md)
  The description of a control widget that has no user-configurable options.
- [struct AppIntentControlConfiguration](appintentcontrolconfiguration.md)
  The description of a control widget that uses a custom intent to provide user-configurable options.
- [struct ControlInfo](controlinfo.md)
  A structure that contains information about user-configured controls.
### Control updates
- [Updating controls locally and remotely](updating-controls-locally-and-remotely.md)
  Update and reload controls from your app or using push notifications.
- [protocol ControlPushHandler](controlpushhandler.md)
  A type that can receive push information about user-configured controls.
- [struct ControlPushInfo](controlpushinfo.md)
  A structure that contains information about the push token of a user-configured control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WidgetKit)*