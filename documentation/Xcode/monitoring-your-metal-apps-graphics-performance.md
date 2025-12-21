# Monitoring your Metal app’s graphics performance

**Framework**: Xcode

Catch performance issues using the Metal Performance HUD while your app runs.

#### Overview

The Metal Performance HUD (heads-up display) adds a real-time overlay to your app that displays and, optionally, logs common graphics performance information. The overlay helps you spot subtle performance issues, such as large variations in rendering time, so you can find the perfect scope to capture in Xcode (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)) or in Instruments (see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md)).

![A screenshot of the Metal Performance HUD over a rendered scene from Metal.](https://docs-assets.developer.apple.com/published/9fde0c144909c9da0129fffda297698c/metal-hud-app%402x.png)

By default, the top of the HUD shows the Metal device, resolution, an indicator for whether the present mode is direct or composited, the amount of memory allocated by the app and Metal, and whether Game Mode is turned on or off (see [`Use Game Mode on Mac`](https://developer.apple.comhttps://support.apple.com/en-us/105118)).

The bottom section of the HUD shows the average frames per second (FPS), GPU time, and frame interval. Below the frame interval is a chart graphing the frame interval from the past 120 frames.

![A cropped screenshot of the Metal Performance HUD showing the GPU, resolution, display scaling factor, present mode, and refresh rate.](https://docs-assets.developer.apple.com/published/cab7f5055c95c64dfc1e11e62829a887/metal-hud-app-zoomed%402x.png)

You can also customize the HUD to include more metrics. To learn more, see [`Customizing the Metal Performance HUD`](customizing-metal-performance-hud.md).

For more information about the metrics provided by the HUD, see [`Understanding the Metal Performance HUD metrics`](understanding-metal-performance-hud-metrics.md).

##### Enable the Hud and Logging in Xcode

Follow these steps to enable the Metal Performance HUD using the runtime diagnostics options in the scheme settings:

1. In the Xcode toolbar, choose Edit Scheme from the Scheme menu. Alternatively, choose Product > Scheme > Edit Scheme. ![An Xcode screenshot that shows the Scheme menu with the Edit Scheme menu item highlighted.](https://docs-assets.developer.apple.com/published/ff9b85fcfb0ccf4ed67a04eeadbe422b/metal-hud-xcode-scheme%402x.png)
2. In the scheme action panel, select Run.
3. In the action setting tab, click Diagnostics.
4. Select Show Graphics Overview to enable the Metal Performance HUD, and click Close. ![A screenshot of Xcode scheme editor with the Show Graphics Overview option enabled and highlighted.](https://docs-assets.developer.apple.com/published/e6b9c3382210821110de57a47b0909b2/metal-hud-xcode-diagnostics%402x.png)

Now, Xcode enables the Metal Performance HUD runtime each time you run your scheme.

You can also optionally enable the output of per-frame statistics to the console by selecting the Log Graphics Overview option.

![A screenshot of the Xcode scheme editor with the Log Graphics Overview option enabled and highlighted.](https://docs-assets.developer.apple.com/published/e189a8f0075bce45381fdd7459ca92b0/metal-hud-xcode-diagnostics-log%402x.png)

> **Note**: You need to select both the Show Graphics Overview and the Log Graphics Overview options to output per-frame statistics.

##### Enable the Hud and Logging with Environment Variables

You can enable the Metal Performance HUD and logging by setting the following environment variables on your Metal app:

##### Enable the Hud and Logging on a Device

You can enable the Metal Performance HUD and logging on an iOS, iPadOS, or tvOS device in the Developer settings by following these steps:

1. Open the Settings app.
2. Select Developer.
3. Under Graphics HUD, toggle the Show Graphics HUD option to enable the Metal Performance HUD.
4. Toggle the Log Graphics Performance option to enable logging.

The Metal Performance HUD appears for apps you build and install yourself to your development devices.

> **Note**: Your device needs to have a development provisioning profile for the Developer options to appear in the Settings app.

The following screenshot shows the options in iOS:

![A screenshot of the Developer settings in iOS, highlighting the toggles to enable the Metal Performance HUD overlay and logging.](https://docs-assets.developer.apple.com/published/c05466ddf012b3296586a8609987f42a/metal-hud-ios-top%402x.png)

The following screenshot shows the options in tvOS:

![A screenshot of the Developer settings in tvOS, highlighting the toggles to enable the Metal Performance HUD overlay and logging.](https://docs-assets.developer.apple.com/published/f1202dbd1c5bc72869c2984d196a9578/metal-hud-tv-settings%402x.png)

##### Enable the Hud and Logging with Information Property List and User Defaults

Alternatively, you can enable the HUD and logging programmatically with one of the following methods:

- Add `MetalHudEnabled` to your app’s `Info.plist` file.
- Add `MetalHUDForceEnabled=1` in your app’s [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults).

##### Utilize the Logging Capabilities

If you enable logging, once per second as your app runs, the HUD writes data in the following format to the console:

```None
metal-HUD: <first-frame-number-integer>,<graphics-memory-usage-float>,<process-memory-usage-float>,<first-frame-present-interval-float>,<first-frame-gpu-time-float>,...<last-frame-present-interval-float>,<last-frame-gpu-time-float>
```

For example, the HUD writes the following data to the console while running the [`Rendering a scene with deferred lighting in Swift`](https://developer.apple.com/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-swift) sample code project:

![A screenshot of the per-frame statistics logs output from the Metal Performance HUD.](https://docs-assets.developer.apple.com/published/043e140b84047c43cae5f93931629a47/gputools-runtime-performance-numbers%402x.png)

When you enable shader compiler logging, as your app runs, the Metal HUD emits signposts for each compiled shader. The subsystem is `com.apple.metal.hud` and the category is `Logging`.

```None
[com.apple.metal.hud:Logging] CompileShader: name: ParticleVs compilation-time: 5496250 cached: 0
[com.apple.metal.hud:Logging] CompileShader: name: ParticlePs compilation-time: 6335000 cached: 0
```

##### Understand Encoder Gpu Time Tracking

You can turn on encoder GPU time tracking by ticking the `Enable Encoder GPU Time Tracking` option in the configuration panel or by setting `MTL_HUD_ENCODER_TIMING_ENABLED` to `1` in the environment variable.

With encoder GPU time tracking, the Metal Performance HUD leverages [`GPU counters and counter sample buffers`](https://developer.apple.com/documentation/Metal/gpu-counters-and-counter-sample-buffers) to track GPU timing for each command encoder to provide enhanced GPU time reporting.

> ❗ **Important**: Encoder GPU time tracking is only available if your app doesn’t use the Metal counter sample buffer. It also may increase the CPU cost of the Metal HUD due to additional data processing.

Encoder GPU time measures GPU activity by tracking the start and end times of work within individual encoder stages (vertex, fragment, and compute). This differs from standard GPU time, which captures the overall duration of command buffers. For command buffers containing many encoders, there may be idle periods in between encoders that can inflate the standard GPU time, providing a less accurate measure of actual GPU workload.

The overlay shows the encoder GPU time as well as the GPU time and the percentage to the total frame time for each encoder type. Below the timing metrics, a GPU timeline visualizes the GPU execution of the last three frames, updating every second.

![A screenshot showing the Metal HUD encoder GPU time.](https://docs-assets.developer.apple.com/published/64eebc2008088a2f84e0ae99c669e6ac/metal-hud-app-gpu-timeline-zoomed%402x.png)

With the encoder GPU time tracking enabled, the Metal Performance HUD also tracks command buffer and encoder labels. Two new optional metrics become available: Top Labeled Command Buffers and Top Labeled Encoders. These metrics show the three most GPU-intensive command buffers and encoders by label, helping you quickly pinpoint potential performance bottlenecks.

![A screenshot showing the top labeled command buffers and encoders.](https://docs-assets.developer.apple.com/published/0826eddb53403afe0c816978b2d090db/metal-hud-app-top-objects-zoomed%402x.png)

##### Display the Value Range of Metrics

You can visualize the range of common metrics in the overlay by enabling the Show Metrics Value Range option in the configuration panel or by setting `MTL_HUD_SHOW_VALUE_RANGE` to `1` in the environment variable.

With this option, the HUD visualizes common metrics in three columns:

- The first column contains the average value of the last 120 frames.
- The second column contains the minimum values of the last 1200 frames.
- The third column contains the maximum values of the last 1200 frames.

![A screenshot showing the Metal HUD reporting value range of metrics.](https://docs-assets.developer.apple.com/published/09e525d4252d5bc2b49128a2e5d3596d/metal-hud-app-value-range%402x.png)

## See Also

- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal API usage](validating-your-apps-metal-api-usage.md)
  Catch runtime issues in your Metal app using API Validation.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation while your app is running.
- [Customizing the Metal Performance HUD](customizing-metal-performance-hud.md)
  Modify the appearance of your Metal heads-up display to monitor your graphics performance.
- [Understanding the Metal Performance HUD metrics](understanding-metal-performance-hud-metrics.md)
  Learn what each of the metrics reported by the heads-up display indicates.
- [Gaining performance insights with the Metal Performance HUD](gaining-performance-insights-with-metal-performance-hud.md)
  Catch potential performance issues while your app runs using the Metal heads-up display.
- [Generating performance reports with the Metal Performance HUD](generating-performance-reports-with-metal-performance-hud.md)
  Record your app’s performance using the heads-up display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/monitoring-your-metal-apps-graphics-performance)*