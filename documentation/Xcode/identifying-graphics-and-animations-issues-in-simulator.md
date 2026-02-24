# Identifying graphics and animations issues in Simulator

**Framework**: Xcode

Reveal performance and display issues in your views with color overlays, and slow down animations to debug and improve them.

#### Overview

When your app encounters issues such as hitches, blurred views, or misplaced views, use Simulator’s color overlays to help you diagnose several common causes:

- **Excess blending**: when your app draws too many views with transparency on top of each other, and the system has to perform work to blend the views together.
- **Copying**: when Core Animation needs to make copies of your image for display.
- **Misalignment**: when your app attempts to display an image that doesn’t divide evenly into the scale factor for a device, or an image that doesn’t fit in the size of a view, the image may be blurry or slightly out of position.
- **Offscreen rendering**: when your app renders a view offscreen before moving it onscreen to display.

When your app encounters issues with animations, such as unexpected jumps, hitches, or diversions from an expected course of changes, use Simulator’s tool to slow down animations so that you can examine them more closely than you can at full speed, and determine the right course of corrective action.

##### Debug and Optimize Graphics Using Color Overlays

Highlight images and areas of the screen that may create issues with rendering, scrolling performance, and memory in Simulator. Choose Debug > Color and select a color overlay to show or hide in your app:

- **Color Blended Layers**: Simulator overlays views in red that your app draws on top of other views and that have blending enabled. Simulator overlays other areas in green. Minimize blended layers to improve rendering and scrolling performance.
- **Color Copied Images**: Simulator overlays images in blue that Core Animation must copy instead of using the original. Minimize copied images to improve memory usage and performance.
- **Color Misaligned Images**: Simulator overlays images in magenta whose bounds are not aligned to the destination pixels. Fix misaligned images to avoid blurs and performance issues. Simulator overlays images in yellow that your app draws with a scale factor. Minimize images with scale factors to improve rendering and scrolling performance.
- **Color Off-screen Rendered**: Simulator overlays content in yellow that is rendered offscreen. Only use off-screen rendering when you have confirmed with tests that the memory and performance tradeoffs work for your app.

You can show multiple overlays at the same time.

Examine your app while you’re displaying overlays to help tune performance. For more information, see [`Improving your app’s performance`](improving-your-app-s-performance.md).

##### Slow Down Animations to Diagnose Problems

Unrelated performance issues, logic issues, unforeseen layout circumstances, and other problems can interfere with smooth animations in your app. Slow down the rate of animations to examine them closely so that you can narrow down possibilities for the root cause. Repeatable issues that occur in animations are frequently a logic or layout issue, while non-repeatable issues can be caused by other issues that slow down your app’s main queue.

Choose Debug > Slow Animations to slow down animations or return them to normal speed. A checkmark indicates that Simulator is running animations slowly.

## See Also

- [Testing in Simulator versus testing on hardware devices](testing-in-simulator-versus-testing-on-hardware-devices.md)
  Review the differences between Simulator and hardware devices to determine which you should choose to test a scenario.
- [Sharing data with Simulator](sharing-data-with-simulator.md)
  Enter text directly in Simulator, or share location data, images, web addresses, files, or data from the clipboard with Simulator.
- [Testing complex hardware device scenarios in Simulator](testing-complex-hardware-device-scenarios-in-simulator.md)
  Test hardware device-specific scenarios, such as Face ID or Touch ID authentication, fall detection, getting a memory warning, or location changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/identifying-graphics-and-animations-issues-in-simulator)*