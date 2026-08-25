# Interacting with previews in the canvas

**Framework**: Xcode

Use the canvas controls to test your view’s appearance and behavior on different devices and configurations.

#### Overview

Previews let you interact with your views and identify interface issues without needing to run your app. Most projects that you create from a template, and most sample code projects, have previews in their interface files. You can also generate previews and playgrounds using coding intelligence.

To view previews, in the Project navigator, select an interface file that contains a preview macro. Xcode opens the file in the source editor on the right. To display the preview in the file, click Show Canvas in the upper-right corner of the project window toolbar. If the canvas is paused, click the Restart button to run the preview.

![A screenshot of the project window with an interface file selected in the Project navigator on the left, the source editor showing the file containing multiple preview macros in the middle, and the canvas showing the tab bar on the top with color scheme variants below on the right.](/images/com.apple.Xcode/show-previews-in-canvas@2x.png)

If you add multiple preview and playground macros to a file, you can switch between them using the tabs that appear at the top of the canvas. Xcode uses the name that you pass to the macro as the label for that preview.

For more information on adding previews and playgrounds, see [`Adding previews to your interface files`](adding-previews-to-your-interface-files.md) and [`Running code snippets using the playground macro`](running-code-snippets-using-the-playground-macro.md).

#### Interact with Your View in Live Mode

Use live mode to test control logic, animations, text entry, and responses to asynchronous code. The behavior of a live mode preview is similar to running your app on a simulated or physical device.

To switch to live mode, click the Live button in the lower-left corner of the canvas and interact with the single device preview that appears. This is the default mode for new previews that you add to your interface files.

![A cropped screenshot of the canvas toolbar on the bottom-left under the preview that shows the location of the live mode button.](/images/com.apple.Xcode/live-mode@2x.png)

#### Change the Preview Screen Size

To verify that your interface adjusts for different device sizes, you can change the preview to an arbitrary size without switching device types.

Click the Resizable button in the lower-left corner of the canvas. Then drag a handle on the top, bottom, or sides of the preview to resize the screen. Alternatively, enter dimensions for the screen at the bottom of the canvas.

![A screenshot of the project window with an interface file selected in the Project navigator on the left, a preview macro in the file highlighted in the middle, and resizable mode showing the handles on each side of the preview in the canvas on the right.](/images/com.apple.Xcode/resize-preview-screen@2x.png)

#### Highlight Code Using Selectable Mode

Use selectable mode to display preview code while interacting with it in the canvas.

To highlight the code for an element in the source editor, click the Selectable button in the lower-left corner of the canvas, and double-click the element in the canvas. Xcode highlights both the element in the canvas and the corresponding code in the source editor.

![A screenshot of the project window with an interface file selected in the Project navigator on the left, the source editor with a preview macro highlighted in the middle, and the canvas in selectable mode on the right.](/images/com.apple.Xcode/highlight-code-in-selectable-mode@2x.png)

Then you can change the code for the element in the source editor and see the results immediately in the canvas.

#### Compare Different View Configurations

Use variant mode to compare your view in different configurations side by side. For example, test how well your view supports different device orientations and text sizes for accessibility.

Click the Variant button in the lower-left corner of the canvas and choose a variant option from the pop-up menu:

![A screenshot of the project window with an interface file selected in the Project navigator on the left, the source editor with a preview macro highlighted in the middle, and the canvas showing orientation variants on the right.](/images/com.apple.Xcode/preview-orientation-variants@2x.png)

- **Color Scheme Variants**: Displays light and dark appearances of your view.
- **Contrast Variants**: Displays different contrasts of your view.
- **Control Borders Variants**: Displays the edges and borders of interactive controls, such as buttons.
- **Orientation Variants**: Displays your view in different portrait and landscape orientations.
- **Dynamic Type Variants**: Displays your view in different accessibility text sizes.

#### Test Views with Different Device Settings

Choose a specific device from the Preview Device pop-up menu in the lower-right corner of the canvas, such as an iPhone or My Mac. Then select device-specific options from the Device Settings button in the lower-right corner of the canvas.

For example, to see how your view looks in dark appearance, landscape right orientation, and extra large text:

1. Click Device Settings in the lower-right corner of the canvas.
2. Toggle Color Scheme on and select Dark Appearance under Color Scheme.
3. Toggle Orientation on and select Landscape Right under Orientation.
4. Toggle Dynamic Type on, and move the Dynamic Type slider to the X Large text setting.

![A screenshot of the project window with an interface file selected in the Project navigator on the left, the source editor with a preview macro highlighted in the middle, and the canvas showing orientation variants in dark appearance device settings on the right.](/images/com.apple.Xcode/change-device-settings@2x.png)

To reproduce interface issues, try turning on a combination of variant and device settings. For example, to see how your view adapts to different languages, select Orientation Variants from Variants. The canvas shows multiple orientations of your view. Then turn Language on and select a localization in Device Settings.

#### Capture Screenshots of Previews

To take a screenshot, click the Screenshot button in the lower-right corner of the canvas. In the sheet that appears, enter a file name, choose a location, and click Save.

## See Also

- [Creating an Xcode project for an app](creating-an-xcode-project-for-an-app.md)
  Set up a new project to start developing your app.
- [Adding previews to your interface files](adding-previews-to-your-interface-files.md)
  Write code to test your views on different devices and configurations without needing to run your app.
- [Running your app on simulated or physical devices](running-your-app-on-simulated-or-physical-devices.md)
  Launch your app on a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a physical device paired with your Mac.
- [Xcode updates](../updates/xcode.md)
  Learn about important changes to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/interacting-with-previews-in-the-canvas)*