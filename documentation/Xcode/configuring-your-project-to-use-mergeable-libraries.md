# Configuring your project to use mergeable libraries

**Framework**: Xcode

Use mergeable dynamic libraries to get app launch times similar to static linking in release builds, without losing dynamically linked build times in debug builds.

#### Overview

In Xcode 14 or earlier, you include code from a separate library in your target using static linking or dynamic linking. You link a static library to your app when you build your target, which can increase both your build time and app size. The dynamic loader resolves dynamic symbols in the executable to point to the appropriate addresses in the dynamic libraries when you run your target, which can increase your app launch time.

In Xcode 15 or later, you can include symbols from a separate,  dynamic library for macOS and iOS app and framework targets. Mergeable dynamic libraries include extra metadata so that Xcode can merge the library into another binary, similar to linking a static library with `-all_load`. When you enable automatic merging, Xcode enables build settings that make app launching fast and keep debugging and development build times fast.

In this context, a debug or development build is unoptimized, where either the `clang` debug format is `-O0` or the `swiftc` debug format is `-Onone`. A release build uses optimizations. Xcode represents debug builds with a new build setting, `IS_UNOPTIMIZED_BUILD`.

In debug builds, Xcode 15 or later treats mergeable dependencies like normal dynamic libraries, without the overhead of creating mergeable metadata and merging all the libraries. In release builds, Xcode creates the mergeable metadata in your dynamic libraries, and merges dependencies into the target binary.

![A diagram that shows the difference between app binary structure and size in debug and release builds.](https://docs-assets.developer.apple.com/published/4d30d76e7fd1cf9d1def67b3378d1684/configuring-your-project-to-use-mergeable-libraries%402x.png)

In release builds, the binary is slightly larger, but avoids the overhead of loading dynamic links at runtime.

> **Note**: Session 10268: [`Meet mergeable libraries`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10268)

##### Merge Libraries Automatically in Xcode

To automatically merge libraries, first open your project in Xcode 15 or later. Then, add the `MERGED_BINARY_TYPE` build setting to your app target, and set the value to `automatic`. With this build setting, Xcode treats mergeable dependencies like normal dynamic libraries in debug builds, but performs steps in release mode to automatically handle merging for direct dependencies. For more information on the `MERGED_BINARY_TYPE` build setting, see [`Create Merged Binary`](build-settings-reference#Create-Merged-Binary.md).

A  is a library that meets two criteria:

- The library is listed in your target’s Link Binary with Libraries build phase.
- The library is the product of another target in your project.

An  is any other library dependency that doesn’t meet those two criteria — for example, a pre-built library, or a library’s dependencies.

In release builds:

- Xcode builds direct dependencies of the merged binary target as mergeable. This includes framework and dynamic library (dylib) targets.
- Xcode combines the mergeable libraries into the merged binary.
- Xcode also combines any mergeable pre-built XCFrameworks listed in your target’s Link Binary with Libraries build phase.
- Xcode embeds mergeable target products in either the merged binary product or into a product, such as an app, that contains the merged binary product. Xcode does  include the binaries from the libraries in the embedded copy.

> **Note**: Xcode does not automatically build indirect dependencies as mergeable in release builds. To configure indirect dependencies for merging, see the [`Manually configure merging`](https://developer.apple.com#Manually-configure-merging) section below.

In debug builds:

- Xcode builds direct dependencies of the merged binary target normally, and doesn’t generate the metadata to make them mergeable.
- The merged binary target links dylibs produced by direct dependencies to be reexported.
- Xcode strips mergeable metadata from any pre-built mergeable XCFrameworks.
- Xcode embeds those target dependency products in either the merged binary product, or into a product containing the merged binary product. Xcode doesn’t include their binaries in the embedded copy (this is the same as the release build behavior).
- Xcode also copies the target dependency products into a special location in the merged binary product. This special location contains only the binaries of the target dependency products. The merged binary product has an additional `@rpath` that points to the special location.

##### Manually Configure Merging

In some cases, you may want to manually configure merging between your app or framework target and dependent libraries. For example, you might not want to automatically merge dependencies that you share between an app and an app extension if you’re concerned about the app extension’s binary size. To set up manual merging, configure your app or framework target, then configure your dependent libraries.

In your app or framework target, add the build setting `MERGED_BINARY_TYPE` and set it to `manual`. After you add that setting to your target:

- In release builds, Xcode merges the products of any of its direct dependencies which have `MAKE_MERGEABLE` enabled using the linker flags `-merge_framework`, `-merge-l`, and so on.
- In debug builds, Xcode links any of your target’s direct dependencies which have `MERGEABLE_LIBRARY` enabled, but not `MAKE_MERGEABLE` with the linker flags `-reexport_framework`, `-reexport-l`, and so on.
- Xcode uses normal linking for targets that don’t have `MERGEABLE_LIBRARY` enabled. This is the same linking that Xcode uses for static libraries, or dynamic libraries that aren’t mergeable.

For each dependent library that you want to use merging, add the build setting `MERGEABLE_LIBRARY`, and set it to `YES`. For more information on the `MERGEABLE_LIBRARY` build setting, see [`Build Mergeable Library`](build-settings-reference#Build-Mergeable-Library.md).

##### Reduce Dependencies with a Group Library

To create a group library that organizes your dependencies in your top level framework or app project:

- Create a new target in your project for your group library.
- Confirm that your group library has the build setting `MERGED_BINARY_TYPE` set to `automatic`.
- Add mergeable libraries as dependencies for your group library.
- Add your group library as a dependency to your app or framework’s target.
- Remove the individual libraries that you added to your group library as dependencies from your app or framework’s target.

##### Create a Pre Built Mergeable Library

To create a mergeable library that you can distribute as a binary package rather than as source:

- Enable the Build Mergeable Library build setting on your library target.
- Create an XCFramework from an archive of your library. For more information, see [`Creating a multiplatform binary framework bundle`](creating-a-multi-platform-binary-framework-bundle.md).

When you include your mergeable library in an XCFramework, Xcode adds the key `MergeableMetadata` to the XCFramework’s `Info.plist` file to indicate to other projects that your library in the XCFramework is mergeable. You can only use XCFrameworks with mergeable metadata in Xcode 15 and later; in earlier versions, Xcode returns a build error.

To use your XCFramework that contains mergeable metadata, add it to the Link Binaries build phase of a target that you configured for automatic or manual merging. For more information, see [`Link against additional frameworks and libraries`](customizing-the-build-phases-of-a-target#Link-against-additional-frameworks-and-libraries.md).

## See Also

- [Improving the speed of incremental builds](improving-the-speed-of-incremental-builds.md)
  Tell the Xcode build system about your project’s target-related dependencies, and reduce the compiler workload during each build cycle.
- [Improving build efficiency with good coding practices](improving-build-efficiency-with-good-coding-practices.md)
  Shorten compile times by reducing the number of symbols your code exports and by giving the compiler the explicit information it needs.
- [Building your project with explicit module dependencies](building-your-project-with-explicit-module-dependencies.md)
  Reduce compile times by eliminating unnecessary module variants using the Xcode build system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-your-project-to-use-mergeable-libraries)*