# Adding StandBy and CarPlay support to your widget

**Framework**: WidgetKit

Ensure that your small system family widget works well in StandBy and CarPlay.

#### Overview

People can choose your small system family widgets from the widget gallery in StandBy or CarPlay:

Because widgets in StandBy appear similar to widgets in CarPlay, when you ensure your widget supports one, it automatically supports the other. To support StandBy and CarPlay appearances, update your small widget:

- Make the background removable.
- Focus on showing only glanceable information.
- Use larger typography, and make it easy to read from a distance.

For more information about making a background removable and optimizing your widget for additional contexts, refer to [`Update your small widget to support StandBy and CarPlay`](preparing-widgets-for-additional-contexts-and-appearances#Update-your-small-widget-to-support-StandBy-and-CarPlay.md).

If your widget isn’t a good fit for StandBy or CarPlay, consider marking the applicable context as a disfavored location as described in [`Indicate that a widget might not fit a specific context`](preparing-widgets-for-additional-contexts-and-appearances#Indicate-that-a-widget-might-not-fit-a-specific-context.md). Doing so doesn’t exclude your widget from CarPlay or StandBy, but it communicates to people that these locations aren’t the best fit.

##### Linking to Your App in Carplay and Using Buttons or Toggles

In CarPlay, the way your widget links to your app depends on the specific context of using your app in a vehicle:

- If the vehicle  supports touch input and your app supports CarPlay integration, tapping the widget or one of its buttons opens the app’s CarPlay template.
- If the vehicle supports touch input but your app doesn’t integrate with CarPlay, people can’t open your app from the widget and the system dims it to indicate that a tap doesn’t have an effect.
- If the vehicle doesn’t support touch input, people can’t open your app from the widget.

For additional information about linking to your app from your widget, refer to [`Review linking behavior in CarPlay`](linking-to-specific-app-scenes-from-your-widget-or-live-activity#Review-linking-behavior-in-CarPlay.md).

| Vehicle features | Buttons and toggles functional | Open the app from a tap |
| --- | --- | --- |
| Touchscreen display available | Yes | Yes, requires your app to offer CarPlay integration |
| Display without touchscreen capabilities | No | No |

Additionally, your widget’s buttons and toggles behave differently to match the CarPlay context:

- If the vehicle supports touch input, people tap a widget’s buttons and toggles to perform their functionality.
- If the vehicle doesn’t have a touchscreen, widgets and buttons are inactive, and people can’t tap the widget to open your app in CarPlay or on their phone.

> **Note**: CarPlay integration is only available to apps with specific functionality. For more information, see [`CarPlay`](https://developer.apple.com/documentation/CarPlay).

##### Test Widgets in Carplay

To test widgets in CarPlay, preview your widget in Xcode to verify that your widget works in StandBy and the CarPlay Simulator. For more information, refer to [`Previewing widgets and Live Activities in Xcode`](previewing-widgets-and-live-activities-in-xcode.md) and [`Using the CarPlay Simulator`](https://developer.apple.com/documentation/CarPlay/using-the-carplay-simulator).

## See Also

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md)
  Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](displaying-the-right-widget-background.md)
  Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)
  Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [struct WidgetRenderingMode](widgetrenderingmode.md)
  Constants that indicate the rendering mode for a widget.
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/adding-standby-and-carplay-support-to-your-widget)*