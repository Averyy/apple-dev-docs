# Validating your app’s Metal shader usage

**Framework**: Xcode

Catch common shader runtime issues using Shader Validation.

#### Overview

Metal Shader Validation detects errors only discoverable during shader execution, such as accesses to non-resident resources, out-of-bounds memory accesses, undefined behavior, and attempts to access `nil` textures.

Examples of issues Shader Validation can detect in Metal apps include:

| Issue | Behavior that causes it |
| --- | --- |
| Resource not resident | Using resources from shaders, or Metal 4 commands, that are not present in any residency set associated with the command buffer or queue, nor in `useResource:usage:[stages:]` calls. |
| Out-of-bounds memory access | Loading or storing data outside the bounds of a buffer you pass from the host to the GPU, or accessing incorrect indices, slices, or the rank of tensor objects. |
| Misuse of Metal Performance Primitives | Mistakes involving tensor ranks, alignment, strides, planes, or out-of-bounds accesses. |
| Undefined interpolant behavior | Storing `INF` or `NaN` in vertex interpolants as part of the output of the vertex shader for members with attributes other than `[[position]]`. |
| Null resources usage | Accessing a null texture or buffer. |
| Illegal address space cast | Casting a pointer in the generic address space to an incorrect specific address space. |
| Binding of incorrect texture type | The shader is expecting a texture type different from the one the app is passing. Note: starting in GPU family `MTLGPUFamilyApple10`, it’s valid to bind texture arrays to slots expecting regular textures, and vice versa. |
| Binding of incorrect acceleration structure type | The shader expects an instancing acceleration structure and the app binds a primitive acceleration structure, or vice versa. |
| Usage flag mismatch | In Metal versions prior to Metal 4, using a texture from a shader in a manner inconsistent with the usage parameter you pass to `useResource:usage:[stages:]`. |

You can enable Shader Validation using the runtime diagnostics options in Xcode and visualizing issues in the Xcode UI, or by using environment variables and printing its results to the app’s standard error or log stream.

To ensure you see the most up-to-date debug information, set your app’s deployment target to the matching OS version, even if only temporarily. You can change the deployment target in the Xcode project settings. If you change the deployment target temporarily, remember to change it back before deploying your app.

> ❗ **Important**: The Shader Validation layer has a corresponding impact on GPU performance, and shaders might take longer to compile at runtime. This layer adds instrumentation code to all your GPU functions, which increases the amount of work they perform and the number of times they access memory.

For more information, see the WWDC20 video [`Debug GPU-side errors in Metal`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10616/) and the WWDC21 video [`Discover Metal debugging, profiling, and asset creation tools`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10157?time=770).

##### Enable Shader Validation in Xcode

Follow these steps to enable Shader Validation using the runtime diagnostics options in the Scheme settings:

1. In the Xcode toolbar, choose Edit Scheme from the Scheme menu. Alternatively, choose Product > Scheme > Edit Scheme.
2. In the Edit Scheme dialog, select Run.
3. Click the Diagnostics tab.
4. Select Shader Validation to enable it, and click Close.

Xcode enables Shader Validation each time you run your scheme.

![A screenshot of Metal validation options with the Shader Validation option enabled and the quick jump button highlighted.](https://docs-assets.developer.apple.com/published/601a622b3d63955df82ad34360db27b5/gputools-runtime-shader-jump%402x.png)

##### Customize Shader Validation Options

You can customize Shader Validation behaviors from the Diagnostics tab:

Select Raise Runtime Issues on Error to log errors Shader Validation detects in the Issue navigator. When you specify this option, you can also create a shader breakpoint.

Choose Abort on Error to cause Shader Validation to stop the program when it logs an error. Use in situations where repeated GPU restarts affect system responsiveness.

Enable Log Allocation Stacktraces to track CPU stacktraces where your app allocates Metal resources. Use this option to obtain the CPU allocation stacktrace of the resource involved in an error. This option increases memory usage.

Choose Detect GPU Stack Overflow to check for GPU stack overflow caused by indirect function calls and recursion.

> **Note**: Except for setting an Xcode shader breakpoint, you can control these options through the environment variables in section “Enable Shader Validation with environment variables” below.

##### Selectively Enable Shader Validation

When enabling Shader Validation, you can also choose to only enable (or disable) Shader Validation for specific pipelines. This advanced control can be particularly useful when you want to focus your debugging on specific pipelines of interest. It can also greatly improve the performance of the apps you debug, due to the reduced amount of instrumented pipelines.

Shader Validation instruments all pipelines by default (`MTL_SHADER_VALIDATION_DEFAULT_STATE=all`). To change this behavior, you can set `MTL_SHADER_VALIDATION_DEFAULT_STATE=none`.

Next, you can set `MTL_SHADER_VALIDATION_ENABLE_PIPELINES` and `MTL_SHADER_VALIDATION_DISABLE_PIPELINES` to selectively enable and disable instrumentation for given pipelines. You can use the pipeline labels and Shader Validation unique identifiers (UIDs) as entries (see [`Print pipeline UIDs`](https://developer.apple.comPrint-pipeline-UIDs)). Multiple entries need to be comma-separated, without spaces (see `man MetalValidation` for more information). In the following example, the pipelines with the label `foo` are the only pipelines not instrumented by Shader Validation.

**Swift**:

```swift
let descriptor = MTLRenderPipelineDescriptor()
descriptor.label = "foo"
pipeline = ...
```

**Objective-C**:

```obj-c
MTLRenderPipelineDescriptor *descriptor = ...;
descriptor.label = @"foo";
pipeline = ...
```

**C++**:

```cpp
MTL::RenderPipelineDescriptor* descriptor = ...;
descriptor->setLabel(MTLSTR("foo"));
pipeline = ...
```

```zsh
> export MTL_SHADER_VALIDATION=1
> export MTL_SHADER_VALIDATION_DEFAULT_STATE=all
> export MTL_SHADER_VALIDATION_DISABLE_PIPELINES="foo"
...

> ./<application>
```

Alternatively, you can programmatically set your pipeline descriptor property [`shaderValidation`](https://developer.apple.comhttps://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/4354231-shadervalidation) to either `MTLShaderValidationEnabled` or `MTLShaderValidationDisabled`.

In the following example, `pipe` is the only pipeline instrumented by Shader Validation.

**Swift**:

```swift
let descriptor = MTLRenderPipelineDescriptor()
descriptor.shaderValidation = .enabled
pipe = try device.makeRenderPipelineState(descriptor: descriptor)
```

**Objective-C**:

```obj-c
MTLRenderPipelineDescriptor *descriptor = ...;
descriptor.shaderValidation = MTLShaderValidationEnabled;
pipe = [device newRenderPipelineStateWithDescriptor:descriptor error:&error];
```

**C++**:

```cpp
MTL::RenderPipelineDescriptor* descriptor = ...;
descriptor->setShaderValidation(MTL::ShaderValidationEnabled);
pipe = device->newRenderPipelineState(descriptor, &error);
```

```zsh
> export MTL_SHADER_VALIDATION=1
> export MTL_SHADER_VALIDATION_DEFAULT_STATE=none
> ...

> ./<application>
```

Finally, you can query the Shader Validation state of a pipeline through the [`shaderValidation`](https://developer.apple.comhttps://developer.apple.com/documentation/metal/mtlrenderpipelinestate/4354232-shadervalidation) property of pipeline state objects.

##### Print Pipeline Uids

Shader Validation generates UIDs for all pipelines you process, which you can use as an entry to `MTL_SHADER_VALIDATION_ENABLE_PIPELINES` and `MTL_SHADER_VALIDATION_DISABLE_PIPELINES`. This is useful when your app has no pipeline labels.

To print the UIDs to Console or a `log stream` instance, set `MTL_SHADER_VALIDATION_DUMP_PIPELINES=1` in your terminal or Xcode Environment Variables Scheme settings.

> **Note**: To see the logs, go to Action > Include Debug Messages in Console.

![A screenshot of the Console displaying dumped Shader Validation UIDs.](https://docs-assets.developer.apple.com/published/1b67f69cc82a8010b711b747ed1a96d0/gputools-runtime-shader-validation-uid-in-console%402x.png)

##### View Shader Validation Errors in Xcode

After enabling Shader Validation, if Metal encounters errors while executing the commands in a command buffer, Xcode displays the error details in the source editor as shown below:

![A screenshot of the Xcode source editor with a triggered Shader Validation error.](https://docs-assets.developer.apple.com/published/078c74d9ef447399b4936e42d7ba93a1/gputools-runtime-shader-trap%402x.png)

You can find the breakpoint in the Breakpoint navigator if you want to modify or remove it in the future. For more information, see [`Setting breakpoints to pause your running app`](setting-breakpoints-to-pause-your-running-app.md).

![A screenshot of the Xcode Breakpoint navigator with a Shader Validation breakpoint enabled.](https://docs-assets.developer.apple.com/published/e340aa8ab8ccc8e2b6450e709c2afdf9/gputools-runtime-shader-breakpoint%402x.png)

If you discover an error in your shader, consider taking a capture and investigating with the shader debugger (see [`Investigating visual artifacts`](investigating-visual-artifacts.md)).

##### View Shader Validation Errors in the Terminal

You can enable Shader Validation for any Metal app via environment variables, even when you don’t have access to its source.

By default, Shader Validation logs any issues it finds to the OS log. You can view these directly in the terminal, using the `log stream` command:

`log stream -process <appname>`

You can also configure Shader Validation to copy its messages to the app’s standard error stream by setting environment variables `MTL_SHADER_VALIDATION=1` and `MTL_SHADER_VALIDATION_REPORT_TO_STDERR=1`.

##### Enable Shader Validation with Environment Variables

You can also enable Shader Validation and customize its behavior by setting the following environment variables on your Metal app:

- **`MTL_SHADER_VALIDATION=1`**: Enables all Shader Validation tests.
- **`MTL_SHADER_VALIDATION_ENABLE_ERROR_REPORTING=1`**: Enables Shader Validation error reporting.
- **`MTL_SHADER_VALIDATION_REPORT_TO_STDERR=1`**: Prints Shader Validation messages to the standard error stream.
- **`MTL_SHADER_VALIDATION_ABORT_ON_FAULT=1`**: Causes Shader Validation to stop the program when it logs an error. Use in situations where repeated GPU restarts affect system responsiveness.
- **`MTL_SHADER_VALIDATION_COMPILER_INLINING`**: Determines the amount of code inlining that occurs. Possible values are `default` and `full`. Setting the value to `full` forces inlining. Increasing inlining can result in improved runtime performance at the cost of compile time performance. Decreasing inlining can result in improved compile time performance at the cost of runtime performance.
- **MTL_SHADER_VALIDATION_FAIL_MODE**: Sets the behavior for handling invalid accesses. Possible values are `zerofill` (default) and `allow`. `zerofill` causes invalid reads to return `0`, and drops any invalid writes. `allow` allows an invalid read or write, but can result in command buffer failure, depending on the platform. It also reduces compile and runtime performance impact.
- **MTL_SHADER_VALIDATION_GLOBAL_MEMORY=1**: Checks all global memory accesses. Accessing invalid memory follows the behavior that `MTL_SHADER_VALIDATION_FAIL_MODE` specifies.
- **MTL_SHADER_VALIDATION_THREADGROUP_MEMORY=1**: Checks all threadgroup memory accesses. Accessing invalid memory follows the behavior that `MTL_SHADER_VALIDATION_FAIL_MODE` specifies.
- **`MTL_SHADER_VALIDATION_TEXTURE_USAGE=1`**: Checks all texture member functions, such as `read`, `write`, `get_width`, and so on. Metal honors your setting for `MTL_SHADER_VALIDATION_FAIL_MODE` when an app triggers an invalid texture operation, including accessing a `nil` texture instance, a valid but nonresident texture instance, a resident texture instance that’s a type that doesn’t match the shader’s signature, or a resident texture instance that doesn’t have an appropriate [`MTLResourceUsage`](https://developer.apple.com/documentation/Metal/MTLResourceUsage) configuration from one of the resource usage methods of an [`MTLComputeCommandEncoder`](https://developer.apple.com/documentation/Metal/MTLComputeCommandEncoder) or [`MTLRenderCommandEncoder`](https://developer.apple.com/documentation/Metal/MTLRenderCommandEncoder) instance (see [`Argument buffer resource preparation commands`](https://developer.apple.com/documentation/Metal/argument-buffer-resource-preparation-commands)).
- **`MTL_SHADER_VALIDATION_STACK_OVERFLOW=1`**: Checks all indirect calls (calls by function pointer, visible functions, intersection functions, and dynamic libraries), as well as recursive calls. If the call stack depth for such functions exceeds the value in `maxCallStackDepth` for that stage, an error occurs and the system skips the function call.
- **`MTL_SHADER_VALIDATION_TENSOR_VALIDATION=1`**: Checks tensor operations for invalid arguments. If this value is set to any non-zero value, shader validation instruments all tensors. `MTL_SHADER_VALIDATION_FAIL_MODE` determines the result of accessing invalid memory. Defaults to `1`. Set to `0` to disable.
- **`MTL_SHADER_VALIDATION_GENERIC_ADDRESS_SPACE=1`**: Checks correctness of static casts of pointer types from generic address spaces to specific address spaces. Defaults to `1`.
- **`MTL_SHADER_VALIDATION_NAN_INF=1`**: Checks whether the vertex stage of a render pipeline state object writes `INF` or `NaN` into any interpolants. Writing `INF` or `NaN` into interpolants, other than the one with the `[[position]]` attribute, results in undefined GPU behavior. Defaults to `1`. Set to `0` to disable.

For a complete list of settings, run `man MetalValidation` in Terminal.

If you discover an error in your shader, consider taking a capture (see [`Capturing a Metal workload programmatically`](capturing-a-metal-workload-programmatically.md)) and investigating with the Metal debugger (see [`Debugging the shaders within a draw command or compute dispatch`](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md)).

##### Review Metal Shader Validation Constraints

Because Metal Shader Validation relies on live shader instrumentation, it’s incompatible with Metal Binary Archives.

Additionally, to use indirect command buffers with Shader Validation, enable pipeline and buffer inheritance.

Metal Shader Validation doesn’t track residency of pages backing Metal sparse resources.

## See Also

- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal API usage](validating-your-apps-metal-api-usage.md)
  Catch runtime issues in your Metal app using API Validation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/validating-your-apps-metal-shader-usage)*