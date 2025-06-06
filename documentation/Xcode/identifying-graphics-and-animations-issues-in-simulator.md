# Identifying graphics and animations issues in Simulator

**Framework**: Xcode

Reveal performance and display issues in your views with color overlays, and slow down animations to debug and improve them.

#### Overview

When your app encounters issues such as hitches, blurred views, or misplaced views, use Simulator’s color overlays to help you diagnose several common causes:

When your app encounters issues with animations, such as unexpected jumps, hitches, or diversions from an expected course of changes, use Simulator’s tool to slow down animations so that you can examine them more closely than you can at full speed, and determine the right course of corrective action.

##### Debug and Optimize Graphics Using Color Overlays

Highlight images and areas of the screen that may create issues with rendering, scrolling performance, and memory in Simulator. Choose Debug > Color and select a color overlay to show or hide in your app:

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