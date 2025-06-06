# Understanding build product layout changes in Xcode

**Framework**: Xcode

#### Overview

The layout of unoptimized builds for app and app extension targets have changed in Xcode. This enables tools and workflows, such as the Previews execution mode that shares build products with normal build-and-run debug builds. This layout saves time and helps prevent correctness issues caused by tools needing different types of build configurations for their work.

If you need an advanced workflow that depends on the specific layout of executables in unoptimized builds, you can opt out of the default behavior if necessary.

##### Inspect Your App Bundle

If you open your app bundle, you see two dynamic library files (`.dylib`) in the executable directory. For example, this is part of the layout of an iOS app bundle:

```None
MyApp.app
    - MyApp
    - MyApp.debug.dylib
    - __preview.dylib
    - <other resources>
```

The file with the `.debug.dylib` suffix contains all of your code that’s linked as the executable binary in a release configuration. The `MyApp` executable becomes a small stub that trampolines over to the entry point in the debug `.dylib` for a normal build-and-run, or passes control to Previews when necessary from Xcode. Previews uses the  `__preview.dylib` to perform this early interposition.

The symbols and Mach-O sections of an unoptimized build link into this separate `.dylib` file, unlike release builds that link into the main binary.

##### Opt Out of the Debug Dylib

If you expect to scan for custom linker sections you inject, use `OTHER_LDFLAGS` for specific control of your output binary. Or if you have tooling that scans binaries for specific symbols for verification, then you may need to adapt to this default unoptimized build layout. If you can’t change your tooling to scan the debug `.dylib`, then you can opt out of this layout completely.

The build setting `ENABLE_DEBUG_DYLIB` controls this mode and defaults to `YES` if these three conditions are met:

- The build target is a bundled executable target
- `SWIFT_VERSION` is set
- `SWIFT_OPTIMIZATION_LEVEL` is set to `-Onone`

You can override this by adding `ENABLE_DEBUG_DYLIB=NO` to that specific target. This is a per-target override and isn’t meant to be applied workspace-wide. It only has an effect on executable targets.

Opting out makes the target ineligible to use Previews. Previews continue to work for frameworks and packages separate from the executable target. You should continue using Previews for dependent targets if you need to opt out of this for your main executable target.

If this article doesn’t address your build issues, file feedback using the [`Feedback Assistant`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/).

## See Also

- [Configuring the build settings of a target](configuring-the-build-settings-of-a-target.md)
  Specify the options you use to compile, link, and produce a product from a target, and identify settings inherited from your project or the system.
- [Adding a build configuration file to your project](adding-a-build-configuration-file-to-your-project.md)
  Specify your project’s build settings in plain-text files, and supply different settings for debug and release builds.
- [Build settings reference](build-settings-reference.md)
  A detailed list of individual Xcode build settings that control or change the way a target is built.
- [Identifying and addressing framework module issues](identifying-and-addressing-framework-module-issues.md)
  Detect and fix common problems found in framework modules with the module verifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/understanding-build-product-layout-changes)*