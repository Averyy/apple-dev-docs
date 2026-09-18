# Customizing your workspace using themes

**Framework**: Xcode

Personalize the appearance of Xcode on your Mac.

#### Overview

Configure the look of your workspace using color themes and font palettes that apply across different views and controls throughout Xcode. You can choose from preset themes, adjust a theme using color sliders, and customize the basic font types that Xcode uses. You can also override the individual colors and fonts for specific purposes.

![A screenshot of Appearance settings showing the Appearance, preview, and Theme settings.](/images/com.apple.Xcode/appearance-settings@2x.png)

#### Change the Xcode Appearance Settings

Use Appearance settings to change the appearance of buttons, controls, and windows in Xcode. To use the macOS system Appearance setting, select System in the Appearance row. To use light appearance or dark appearance, regardless of the system settings, select Light or Dark.

When you use theme presets, the light appearance has a subtle look while the dark appearance is more vibrant.

#### Select Themes From Presets

On the Theme pane of Appearance settings, click Choose in the Theme row, and choose a custom or preset theme from the popover that appears. The preview updates to show your changes. Changes you make to themes also appear immediately in open Xcode windows. All types of editors and even live issues use the themes that you configure in the Theme pane.

![A screenshot of Theme settings showing the preset popover.](/images/com.apple.Xcode/select-theme-presets@2x.png)

To pick a separate theme for a workspace, click the Adjust Editor Options button on the right of the project window toolbar and choose Choose Workspace Theme from the pop-up menu. Choose a preset or custom theme from the popover that appears.

#### Change the Themes Color Palette

To change the intensity of a theme’s text colors, choose the custom or preset theme in the Theme pane. Then make the following edits using the controls below:

- To influence the intensity of the text colors, move the Foreground slider.
- To ramp up the background intensity, move the Background slider to the right. As you move the Background slider, you see a full window background color.
- To change the starting tint, click the Foreground or Background color wells and select a color from the popover. To pick a different color, click the eyedropper that opens the Colors window.
- To apply a gradient to the background, toggle on Background Gradient.

Then enter a name for the custom theme in the Name text field above the controls. The name you enter appears in the theme popover.

Set the colors for specific types of text (such as comments, numbers, and links) using the settings at the bottom of the Theme pane. Xcode generates the default values for the text colors from the theme’s palette. When you set individual colors manually, Xcode won’t change those values when you change the theme.

Use the controls below the theme palette controls to:

- Customize all types of text color, toggle on Customize All Colors and set individual colors below
- Customize individual text colors, toggle off Customize All Colors, click the color well for the type of text, and select a color from the popover
- Revert a color back to the default or automatic value, click the “Reset to Default Value” button next to the color well

![A screenshot of Theme settings showing the custom color palette with a different color selected.](/images/com.apple.Xcode/change-theme-colors@2x.png)

> **Note**: Xcode saves your theme changes to a file with the name you enter and a `.xcworkspacecolortheme` extension in the `~/Library/Developer/Xcode/UserData/FontAndColorThemes/` folder. If you toggle on “Keep a copy in iCloud” in Settings > General > Settings Import & Export, you can share themes between Mac computers.

#### Change the Themes Font Palette

The basic fonts for code, prose, and console act as a palette for fonts that appear across editors. If you change the basic fonts, Xcode automatically updates the rest of the fonts that Xcode uses.

In the Fonts pane, you can:

- Change the basic fonts, use the Code, Prose, and Console controls at the top of the Fonts pane
- Customize all fonts, toggle on Customize All Fonts and set fonts below
- Customize individual fonts, toggle off Customize All Fonts, and set specific fonts below
- Revert a font back to the automatic font, click the “Reset to Default Value” button next to the font settings

#### Import Themes From Previous Xcode Releases

To add colors that you configured in earlier Xcode releases, click the Import button on the Themes popover and select the color theme file (with a `.xcolortheme` extension) from the `~/Library/Developer/Xcode/UserData/FontAndColorThemes` folder.

## See Also

- [Downloading and installing additional Xcode components](downloading-and-installing-additional-xcode-components.md)
  Add more simulated devices, optional features, and support for additional platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/customizing-your-workspace-using-themes)*