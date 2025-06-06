# Monitoring your Metal app’s graphics performance

**Framework**: Xcode

Catch performance issues using the Metal Performance HUD while your app is running.

#### Overview

The Metal Performance HUD (heads-up display) adds a real-time overlay to your app that displays and, optionally, logs common graphics performance information. The overlay helps you spot subtle performance issues, such as large variations in rendering time, so you can find the perfect scope to capture in Xcode (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)) or in Instruments (see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md)).

![A screenshot of the Metal Performance HUD over a rendered scene from Metal.](https://docs-assets.developer.apple.com/published/c32173abe2ef50b61edc5de0c7d4182b/gputools-runtime-hud%402x.png)

The GPU and resolution appear at the top of the HUD, along with the display scaling factor, refresh rate, and an indicator for whether the present mode is `direct` or `composited`.

![A cropped screenshot of the Metal Performance HUD showing the GPU, resolution, display scaling factor, present mode, and refresh rate.](https://docs-assets.developer.apple.com/published/fb2083002eccce956a7048d4b9622db5/gputools-runtime-hud-0%402x.png)

The middle section of the HUD shows three rows of information, each with three columns:

- The first column contains the mean values from the last 1.5 seconds of the frames per second (FPS), the present-to-present interval (Pre), and the GPU time (GPU).
- The second column contains the minimum values from the last 1.5 seconds of FPS, Pre, and GPU.
- The third column contains the maximum values from the last 1.5 seconds of FPS, Pre, and GPU.

When minimum and maximum values vary by more than 15% from the average, they appear with a red highligt for easier identification.

![A cropped screenshot of the Metal Performance HUD showing statistics for the FPS, the present-to-present interval, and the GPU time over the last 1.5 seconds.](https://docs-assets.developer.apple.com/published/701819d3b8bf2e5bdc5d9c0ab99dd43f/gputools-runtime-hud-1%402x.png)

The bottom section of the HUD shows the app’s overall memory footprint, the GPU memory footprint, and a graph of the last 200 frames of the present-to-present interval (Pre) and the GPU time (GPU).

![A cropped screenshot of the Metal Performance HUD showing the memory footprint, as well as a graph of the present-to-present interval and the GPU time.](https://docs-assets.developer.apple.com/published/d52f126d1178cddc942392ebcd7a5799/gputools-runtime-hud-2%402x.png)

For more information, see [`Discover Metal Performance HUD`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/110339/).

##### Enable the Metal Performance Hud in Xcode

Follow these steps to enable the Metal Performance HUD using the runtime diagnostics options in the scheme settings:

1. In the Xcode toolbar, choose Edit Scheme from the Scheme menu. Alternatively, choose Product > Scheme > Edit Scheme. ![An Xcode screenshot that shows the Scheme menu with the Edit Scheme menu item highlighted.](https://docs-assets.developer.apple.com/published/6276e85b8ecf3632dbf5391a2175b1f6/gputools-runtime-edit-scheme%402x.png)
2. In the scheme action panel, select Run.
3. In the action setting tab, click Diagnostics.
4. Select Show Graphics Overview to enable the Metal Performance HUD, and click Close. ![A screenshot of Xcode scheme editor with the Show Graphics Overview option enabled and highlighted.](https://docs-assets.developer.apple.com/published/1cb7a56cc4209bab46b588a3abb46a4c/gputools-runtime-show-graphics-overview%402x.png)

Now, the Metal Performance HUD runtime is enabled each time you run your scheme.

##### Enable Logging in Xcode

You can also optionally enable the output of per-frame statistics to the console by selecting the Log Graphics Overview option.

![A screenshot of the Xcode scheme editor with the Log Graphics Overview option enabled and highlighted.](https://docs-assets.developer.apple.com/published/2cc4762a43e7b6d0856866da858dd977/gputools-runtime-log-graphics-overview%402x.png)

> **Note**: You need to select both the Show Graphics Overview and the Log Graphics Overview options to output per-frame statistics.

Then, as your app is running, once per second (or more frequently at high present rates due to vsync-off or high-refresh and VRR displays), the HUD writes data in the following format to the console:

```None
metal-HUD: <first-frame-number-integer>,<frame-misses-integer>,<process-memory-usage-float>,<first-frame-present-interval-float>,<first-frame-gpu-time-float>,...<last-frame-present-interval-float>,<last-frame-gpu-time-float>
```

For example, the HUD wrote the following data to the console while running the [`Rendering a Scene with Deferred Lighting in Swift`](https://developer.apple.com/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-swift) sample code project:

![A screenshot of the per-frame statistics logs output from the Metal Performance HUD.](https://docs-assets.developer.apple.com/published/043e140b84047c43cae5f93931629a47/gputools-runtime-performance-numbers%402x.png)

##### Enable the Hud and Logging with Environment Variables

You can enable the Metal Performance HUD and logging by setting the following environment variables on your Metal app:

Alternatively, you can enable the HUD and logging programmatically as follows:

1. Add `MetalHudEnabled` to your app’s `Info.plist` file.
2. Either set `MetalHUDForceEnabled=1` in your app’s [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults), or configure your `CAMetalLayer` instance’s `developerHUDProperties` dictionary with the following: ```swift
myMetalLayer.developerHUDProperties = [
    "mode": "default",
    "logging": "default"
]
```

##### Enable the Hud and Logging on a Device

You can enable the Metal Performance HUD and logging on an iOS, iPadOS, or tvOS device in the Developer settings by following these steps:

1. Open the Settings app.
2. Select Developer.
3. Under Graphics HUD, toggle the Show Graphics HUD option to enable the Metal Performance HUD.
4. Toggle the Log Graphics Performance option to enable logging.

The Metal Performance HUD appears for apps you build and install yourself to your development devices.

> **Note**: Your device needs to have a development provisioning profile for the Developer options to appear in the Settings app.

The following screenshot shows the options in iOS:

![A screenshot of the Developer settings in iOS, highlighting the toggles to enable the Metal Performance HUD overlay and logging.](https://docs-assets.developer.apple.com/published/c1888ecc421bf8b22b981a82632e7eca/gputools-runtime-hud-settings-iOS%402x.png)

The following screenshot shows the options in tvOS:

![A screenshot of the Developer settings in tvOS, highlighting the toggles to enable the Metal Performance HUD overlay and logging.](https://docs-assets.developer.apple.com/published/088a65f9a3588dc934845291a76d65a3/gputools-runtime-hud-settings-tvOS.png)

## See Also

- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal API usage](validating-your-apps-metal-api-usage.md)
  Catch runtime issues in your Metal app using API Validation.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation while your app is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/monitoring-your-metal-apps-graphics-performance)*