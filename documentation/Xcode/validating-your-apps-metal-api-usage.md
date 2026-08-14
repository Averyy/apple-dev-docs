# Validating your app’s Metal API usage

**Framework**: Xcode

Catch runtime issues in your Metal app using API Validation.

#### Overview

The API Validation layer checks for code that calls the Metal API incorrectly, including errors in creating resources, encoding Metal commands, and performing other common tasks. You can enable API Validation using the runtime diagnostics options in Xcode, or by using environment variables.

> ❗ **Important**: The API Validation layer has a small, but measurable, impact on CPU performance.

##### Enable Api Validation in Xcode

Follow these steps to enable API Validation using the runtime diagnostics options in the scheme settings:

1. In the Xcode toolbar, choose Edit Scheme from the Scheme menu. Alternatively, choose Product > Scheme > Edit Scheme. ![An Xcode screenshot that shows the Scheme menu with the Edit Scheme menu item highlighted.](/images/com.apple.Xcode/gputools-runtime-edit-scheme@2x.png)
2. In the scheme action panel, select Run.
3. In the action setting tab, click Diagnostics.
4. Select API Validation to enable it, and click Close. ![A screenshot of the Xcode scheme editor with the API Validation option enabled and highlighted.](/images/com.apple.Xcode/gputools-runtime-api-validation@2x.png)

Now, Xcode enables API Validation each time you run your scheme.

You can additionally use the Diagnostics tab to enable extra API Validation behaviors:

- Include load and store actions: You can enable this option to help debug incorrect load and store actions. It dynamically changes [`MTLLoadAction.dontCare`](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare) to [`MTLLoadAction.clear`](https://developer.apple.com/documentation/metal/mtlloadaction/clear) to fuchsia color, and writes an alternating red and white checkerboard pattern into each render target with a store action of [`MTLStoreAction.dontCare`](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare). Use this option to debug incorrect load and store action modes or assumptions on the “don’t care” behavior.
- Log non-fatal actions: Enable additional logging of incorrect or suboptimal Metal usage that doesn’t prevent app execution. Use this option to further lint your Metal app.

> **Note**: You can also control these options through environment variables.

##### Enable Api Validation with Environment Variables

You can also enable API Validation by setting the following environment variables on your Metal app:

- **MTL_DEBUG_LAYER=1**: Enables all API Validation tests.
- **MTL_DEBUG_LAYER_ERROR_MODE**: Sets the behavior for when a debug layer error occurs. Possible values are `assert` (default), `ignore`, and `nslog`. `assert` causes the debug layer to log and then assert on error. `ignore` causes the debug layer to ignore errors, which may cause undefined behavior. `nslog` causes the debug layer to log errors using [`NSLog`](https://developer.apple.com/documentation/foundation/nslog), which may also cause undefined behavior.
- **MTL_DEBUG_LAYER_VALIDATE_LOAD_ACTIONS=1**: Converts any [`MTLLoadAction.dontCare`](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare) to [`MTLLoadAction.clear`](https://developer.apple.com/documentation/metal/mtlloadaction/clear) using a fuchsia color, which you can use to locate and debug incorrect load action modes or assumptions on [`MTLLoadAction.dontCare`](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare) behavior.
- **MTL_DEBUG_LAYER_VALIDATE_STORE_ACTIONS=1**: Writes an alternating red-and-white checkerboard into each render target with a store action of [`MTLStoreAction.dontCare`](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare), which you can use to debug incorrect store action modes or assumptions on [`MTLStoreAction.dontCare`](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) behavior.
- **MTL_DEBUG_LAYER_VALIDATE_UNRETAINED_RESOURCES**: This option takes a bitfield of modes to enable. The default is 0x1. The bitfield values are: - **0x1**: Enabling this flag causes the command buffer to tag any objects bound to it, which the system doesn’t retain internally. This makes Metal Validation raise an error if the system deallocates a tagged object before the command buffer completes.
- **0x2**: Enabling this flag causes the command buffer to tag objects that it internally retains. This flag is generally unnecessary because the system can’t deallocate an object while the command buffer itself isn’t complete.
- **0x4**: Enabling this flag causes the system to treat deallocated tagged objects as errors even before committing the command buffer. This leads to a more immediate error (for example, in the call stack of the deallocation), which is more debuggable than at commit.
- **MTL_DEBUG_LAYER_WARNING_MODE**: Sets the behavior for when a debug layer warning occurs. Possible values are `assert`, `ignore` (default), `nslog`, and `oslog`. `assert` causes the debug layer to log and then assert on warning. `ignore` causes the debug layer to ignore warnings. `nslog` causes the debug layer to log warnings using [`NSLog`](https://developer.apple.com/documentation/foundation/nslog). `oslog` causes the debug layer to log warnings using [`os_log`](https://developer.apple.com/documentation/os/os_log).

For a complete list of settings, run `man MetalValidation` in Terminal.

> **Note**: API Validation only checks unretained resource references from instances of [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer) and not from [`MTL4CommandBuffer`](https://developer.apple.com/documentation/metal/mtl4commandbuffer).

## See Also

- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation.
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