# Porting your macOS apps to Apple silicon

**Framework**: Apple Silicon

Create a version of your macOS app that runs on both Apple silicon and Intel-based Mac computers.

#### Overview

Port your existing macOS app to Apple silicon by creating a universal binary and modifying your code to handle architectural differences. A universal binary looks no different than a regular app, but its executable file contains two versions of your compiled code. One version runs natively on Apple silicon, and the other runs natively on Intel-based Mac computers. At runtime, the system automatically chooses which version to run on the current platform.

![ThAn illustration of an app, where the main executable file supports the arm64 and x86_64 architectures.](https://docs-assets.developer.apple.com/published/8576d4db4481980842af6b4189e0c79e/porting-your-macos-apps-to-apple-silicon-1%402x.png)

To build a universal binary, you need Xcode 12 or a later version, which adds `arm64` to the standard list of build architectures for macOS binaries. When you open your project and do a clean build, Xcode creates a universal binary automatically if your project uses the standard architectures. If you use custom makefiles or build scripts, add the `arm64` architecture to your build system.

After you create a universal binary, test it on both architectures and determine whether you need to make additional changes. macOS frameworks shield apps from most architectural differences between platforms, but some differences may still require you to change your code. In addition, architectural differences may affect your app’s performance and require further changes.

> **Note**: On Apple silicon, apps built for the `x86_64` architecture run under the Rosetta translation environment. For more information, see [`About the Rosetta translation environment`](about-the-rosetta-translation-environment.md).

To learn how to build a universal binary, see [`Building a universal macOS binary`](building-a-universal-macos-binary.md).

##### Create a Porting Plan

Early in the porting process, identify the workflow you’ll use to build and test your code. Xcode runs on all Mac computers, so build your code on either an Apple silicon or Intel-based Mac computer and do your initial testing there. However, always test, tune, and validate your code on both computer types to uncover issues specific to that architecture.

![An illustration of the process for building, debugging, and tuning your code on Apple silicon-based Mac computers and Intel-based Mac computers.](https://docs-assets.developer.apple.com/published/c3701ee00fbe41f996a5f0aae509daf6/porting-your-macos-apps-to-apple-silicon-2%402x.png)

In addition to a workflow plan, identify potential areas to investigate during the porting process. The porting effort for `arm64` depends on how much you rely on hardware-specific features. If you rely mostly on Apple frameworks and technologies, your porting effort may be small. If you tuned your code specifically for the `x86_64` architecture and hardware capabilities, porting to `arm64` may require additional effort.

To start your investigation, make a note of any code that does the following:

- Interacts with third-party libraries you don’t own.
- Interacts with the kernel or hardware.
- Relies on specific GPU behaviors.
- Contains assembly instructions.
- Manages threads or optimizes your app’s multithreaded behavior.
- Contains hardware-specific assumptions or performance optimizations.

The list above is not exhaustive, but it offers a starting point for your investigation. Hardware and architectural differences may introduce bugs or performance issues to your code on Apple silicon. Identifying potential problem areas early will save you time later.

Always have a well-defined test plan, ideally with a set of automated test suites you can run at build time. In addition to testing your code’s correctness, gather metrics on your app’s performance. Examine your app’s memory usage, and measure how long it takes to execute specific tasks on both Apple silicon and Intel-based Mac computers. Use that information to identify additional areas to investigate.

##### Obtain Universal Versions of Linked Libraries

If your project depends on any third-party libraries, contact the original vendors and ask them to provide you with universal versions of those libraries. All code running in the same process must support the same architecture. You cannot produce a universal version of your binary without universal versions of all linked libraries. If one or more libraries is not universal, the linker reports errors.

![TAn illustration that shows the linker creating a universal app from the app’s code and a universal library.](https://docs-assets.developer.apple.com/published/89e8c4c8fe530c1e7e34c783fac72822/porting-your-macos-apps-to-apple-silicon-3%402x.png)

To learn how to create your own universal binaries, see [`Building a universal macOS binary`](building-a-universal-macos-binary.md).

##### Update Plug Ins to Universal Binaries

A universal plug-in runs natively on any Mac computer. If your app supports a plug-in model, create universal versions of the plug-ins that you manage. If your company allows external developers to contribute plug-ins, encourage those developers to create universal versions of their plug-ins.

Universal plug-ins are essential if your app loads those plug-ins directly into its process space. Code running in the same process must support the same architecture. If your app attempts to load a plug-in with an incompatible architecture, the system reports an error at load time.

![An illustration of an XPC service managing a plug-in for an app.](https://docs-assets.developer.apple.com/published/f3c16c0dcc7416b1f72398a74b7edb69/porting-your-macos-apps-to-apple-silicon-4%402x.png)

Plug-ins that run out-of-process using an XPC service may run using a different architecture than the app itself. To give your developers time to update their plug-ins, provide two non-universal XPC services—one to run `arm64` plug-ins and one to run `x86_64` plug-ins. A single XPC service can manage either native or translated plug-ins, but not both at the same time. When creating the services, give each one a unique bundle identifier so they may run simultaneously.

For information about how to communicate with out-of-process plug-ins using XPC, see [`XPC`](https://developer.apple.com/documentation/Foundation/xpc).

##### Address Architectural Differences

Apart from large-scale changes to the processor and graphics hardware, subtle architectural differences exist between Apple silicon and Intel-based Mac computers. During the porting process, audit your code to identify fixes for any potential architectural issues. For example, look for places where your code relies on specific hardware features or configurations.

The following list identifies several known architectural differences between Apple silicon and Intel-based Mac computers. Update code that relies on any of the following:

- Virtual memory-page sizes
- Cache line sizes
- Variadic functions
- Memory that is simultaneously writable and executable
- Just-in-time compilers
- Realtime threads
- Explicit thread priorities
- Hardware-specific details
- Assembly-language instructions or builtin intrinsics
- Vector unit instructions
- C++ ABI details

> **Note**: Both Apple silicon and Intel-based Mac computers use the little-endian format for data, so you don’t need to make endian conversions in your code. However, continue to minimize the need for endian conversions in custom data formats that you create.

For additional information about architectural differences, see [`Addressing architectural differences in your macOS code`](addressing-architectural-differences-in-your-macos-code.md).

##### Update Gpu Specific Code

Metal on Apple silicon supports the features of both Intel-based Mac computers and iOS devices. If your app adopts Metal features that are found only on Intel-based Mac computers, consider also adopting the iOS-specific features in your `arm64` code. Adopting these features can lead to performance improvements for many apps.

If your app uses Metal, OpenGL, or OpenCL, be aware of the following differences:

- The GPU and CPU on Apple silicon share memory.
- OpenGL is deprecated, but is available on Apple silicon.
- OpenCL is deprecated, but is available on Apple silicon when targeting the GPU. The OpenCL CPU device is not available to arm64 apps.

For information about how to update your graphics code, see [`Porting your Metal code to Apple silicon`](porting-your-metal-code-to-apple-silicon.md).

##### Update Drivers System Extensions and Kernel Extensions

When porting code to macOS 11, be aware of the following requirements for code that interacts with the kernel:

- Implement hardware drivers using DriverKit. macOS 11 requires you to use a DriverKit extension when support for one is available. Most driver types now support DriverKit, and only a few still require the creation of a kernel extension.
- Kernel extensions must support the native architecture. Kernel extensions run in the kernel, and the kernel always runs as a native process. You cannot run kernel extensions using Rosetta translation.
- The installation and uninstallation of kernel extensions requires a reboot. When you install a kernel extension, the system doesn’t load your extension until after a reboot.

For more information about kernel extension and driver changes, see [`Implementing drivers, system extensions, and kexts`](https://developer.apple.com/documentation/SystemExtensions/implementing-drivers-system-extensions-and-kexts).

##### Migrate Away From Specific Technologies

macOS includes a few technologies that are currently deprecated or discouraged for active development. If your app uses one of the following technologies, migrate to an appropriate replacement as soon as possible:

- OpenGL—Use [`Metal`](https://developer.apple.com/documentation/Metal) instead.
- OpenCL—Use [`Metal`](https://developer.apple.com/documentation/Metal) instead.
- AddressBook—Use the [`Contacts`](https://developer.apple.com/documentation/Contacts) framework instead.
- Carbon APIs—Migrate to [`AppKit`](https://developer.apple.com/documentation/AppKit), [`Foundation`](https://developer.apple.com/documentation/Foundation), and other modern APIs.
- IOKit kernel extensions—Migrate to DriverKit where appropriate; see [`DriverKit`](https://developer.apple.com/documentation/DriverKit) framework.

Apple silicon still provides support for the preceding technologies, and you may continue to use them in macOS 11. However, this support may be removed in a future version of macOS, so migration to newer technologies is recommended.

##### Debug and Test Your Code

Apple silicon supports all debugging and testing tools found on Intel-based Mac computers. Use the Xcode IDE to set and monitor breakpoints and monitor other aspects of your app’s behavior. Use `lldb` from the command line to perform similar tasks outside of the Xcode interface.

For more information about how to debug and test your code, see [`Xcode`](https://developer.apple.com/documentation/Xcode).

##### Tune Your Apps Performance

Apple silicon runs all performance tools found on Intel-based Mac computers. Use Instruments and other performance tools to gather different types of metrics for your app, including information about its memory usage, speed, energy usage, and more. You can also use command-line tools such as `leaks`, `heap`, `top`, `fs_usage`, `sc_usage`, `vm_stat`, `otool`, `sample`, `malloc_history`, and `vmmap` to identify potential performance issues.

Architectural differences between `arm64` and `x86_64` mean that techniques that work well on one system might not work well on the other. For example:

- Don’t assume a discrete GPU means better performance. The integrated GPU in Apple processors is optimized for high performance graphics tasks. See [`Porting your Metal code to Apple silicon`](porting-your-metal-code-to-apple-silicon.md).
- Don’t assume that all processor cores are equal. The processors on Apple silicon contain a mixture of performance cores (P-cores) and efficiency cores (E-cores), which execute tasks with different performance characteristics. Use Quality-of-Service (QoS) classes to help the system schedule your tasks on the right type of core.

During the porting process, measure your app’s performance on both Apple silicon and Intel-based Mac computers and investigate any discrepancies. Tasks that take longer to run on one platform may require additional tuning.

For specific tips on tuning universal binaries, see [`Tuning your code’s performance for Apple silicon`](tuning-your-code-s-performance-for-apple-silicon.md).

## Topics

### Additional Porting Tips
- [Addressing architectural differences in your macOS code](addressing-architectural-differences-in-your-macos-code.md)
  Fix problems that stem from architectural differences between Apple silicon and Intel-based Mac computers.
- [Porting your audio code to Apple silicon](porting-your-audio-code-to-apple-silicon.md)
  Eliminate issues in your audio-specific code when running on Apple silicon Mac computers.
- [Porting just-in-time compilers to Apple silicon](porting-just-in-time-compilers-to-apple-silicon.md)
  Update your just-in-time (JIT) compiler to work with the Hardened Runtime capability, and with Apple silicon.

## See Also

- [Building a universal macOS binary](building-a-universal-macos-binary.md)
  Create macOS apps and other executables that run natively on both Apple silicon and Intel-based Mac computers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-silicon/porting-your-macos-apps-to-apple-silicon)*