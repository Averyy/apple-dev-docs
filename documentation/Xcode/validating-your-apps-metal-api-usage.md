# Validating your app’s Metal API usage

**Framework**: Xcode

Catch runtime issues in your Metal app using API Validation.

#### Overview

The API Validation layer checks for code that calls the Metal API incorrectly, including errors in creating resources, encoding Metal commands, and performing other common tasks. You can enable API Validation using the runtime diagnostics options in Xcode, or by using environment variables.

> ❗ **Important**: The API Validation layer has a small, but measureable, impact on CPU performance.

##### Enable Api Validation in Xcode

Follow these steps to enable API Validation using the runtime diagnostics options in the scheme settings:

1. In the Xcode toolbar, choose Edit Scheme from the Scheme menu. Alternatively, choose Product > Scheme > Edit Scheme. ![An Xcode screenshot that shows the Scheme menu with the Edit Scheme menu item highlighted.](https://docs-assets.developer.apple.com/published/6276e85b8ecf3632dbf5391a2175b1f6/gputools-runtime-edit-scheme%402x.png)
2. In the scheme action panel, select Run.
3. In the action setting tab, click Diagnostics.
4. Select API Validation to enable it, and click Close. ![A screenshot of the Xcode scheme editor with the API Validation option enabled and highlighted.](https://docs-assets.developer.apple.com/published/63896827dbb9bf90c727cf87385054eb/gputools-runtime-api-validation%402x.png)

Now, the API Validation runtime is enabled each time you run your scheme.

##### Enable Api Validation with Environment Variables

You can also enable API Validation by setting the following environment variables on your Metal app:

- **MTL_DEBUG_LAYER=1**: Enables all API Validation tests.
- **MTL_DEBUG_LAYER_ERROR_MODE**: Sets the behavior for when a debug layer error occurs. Possible values are `assert` (default), `ignore`, and `nslog`. `assert` causes the debug layer to log and then assert on error. `ignore` causes the debug layer to ignore errors, which may cause undefined behavior. `nslog` causes the debug layer to log errors using [`NSLog`](https://developer.apple.com/documentation/Foundation/NSLog), which may also cause undefined behavior.
- **MTL_DEBUG_LAYER_VALIDATE_LOAD_ACTIONS=1**: Converts any [`MTLLoadAction.dontCare`](https://developer.apple.com/documentation/Metal/MTLLoadAction/dontCare) to [`MTLLoadAction.clear`](https://developer.apple.com/documentation/Metal/MTLLoadAction/clear) using a fuchsia color, which you can use to locate and debug incorrect load action modes or assumptions on [`MTLLoadAction.dontCare`](https://developer.apple.com/documentation/Metal/MTLLoadAction/dontCare) behavior.
- **MTL_DEBUG_LAYER_VALIDATE_STORE_ACTIONS=1**: Writes an alternating red-and-white checkerboard into each render target with a store action of [`MTLStoreAction.dontCare`](https://developer.apple.com/documentation/Metal/MTLStoreAction/dontCare), which you can use to debug incorrect store action modes or assumptions on [`MTLStoreAction.dontCare`](https://developer.apple.com/documentation/Metal/MTLStoreAction/dontCare) behavior.
- **MTL_DEBUG_LAYER_VALIDATE_UNRETAINED_RESOURCES**: This option takes a bitfield of modes to enable. The default is 0x1. The bitfield values are: - **0x1**: Enabling this flag causes the command buffer to tag any objects bound to it, which the system doesn’t retain internally. If the system deallocates a tagged object before the command buffer completes, an error occurs.
- **0x2**: Enabling this flag causes the command buffer to tag objects that it internally retains. This flag is generally unnecessary because the system can’t deallocate an object while the command buffer itself isn’t complete.
- **0x4**: Enabling this flag causes the system to treat deallocated tagged objects as errors even before committing the command buffer. This leads to a more immediate error (for example, in the call stack of the deallocation), which is more debuggable than at commit.
- **MTL_DEBUG_LAYER_WARNING_MODE**: Sets the behavior for when a debug layer warning occurs. Possible values are `assert`, `ignore` (default), and `nslog`. `assert` causes the debug layer to log and then assert on warning. `ignore` causes the debug layer to ignore warnings. `nslog` causes the debug layer to log warnings using [`NSLog`](https://developer.apple.com/documentation/Foundation/NSLog).

For a complete list of settings, run `man MetalValidation` in Terminal.

## See Also

- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation while your app is running.
- [Monitoring your Metal app’s graphics performance](monitoring-your-metal-apps-graphics-performance.md)
  Catch performance issues using the Metal Performance HUD while your app runs.
- [Customizing the Metal Performance HUD](customizing-metal-performance-hud.md)
  Modify the appearance of your Metal heads-up display to monitor your graphics performance.
- [Understanding the Metal Performance HUD metrics](understanding-metal-performance-hud-metrics.md)
  Learn what each of the metrics reported by the heads-up display indicates.
- [Gaining performance insights with the Metal Performance HUD](gaining-performance-insights-with-metal-performance-hud.md)
  Catch potential performance issues while your app runs using the Metal heads-up display.
- [Generating performance reports with the Metal Performance HUD](generating-performance-reports-with-metal-performance-hud.md)
  Record your app’s performance using the heads-up display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/validating-your-apps-metal-api-usage)*