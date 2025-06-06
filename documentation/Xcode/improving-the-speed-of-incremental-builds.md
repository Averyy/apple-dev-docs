# Improving the speed of incremental builds

**Framework**: Xcode

Tell the Xcode build system about your project’s target-related dependencies, and reduce the compiler workload during each build cycle.

#### Overview

The Xcode build system manages the compilation and linking of the code in targets. Common types of targets include apps, app extensions, frameworks, libraries, and test suites. A simple project might contain only one target, such as the app you want to build. A more complex project might contain multiple targets with interdependencies, such as a private framework and an app that depends on that framework.

Always ensure that your project’s inter-target dependencies and configuration details are accurate. When you build a target, Xcode does as much work as possible in parallel. Fewer dependencies leads to greater parallelization, but an accurate dependency map is necessary to prevent build and runtime errors. Similarly, providing detailed configuration data helps Xcode schedule build-time tasks correctly and efficiently.

> **Note**: Following coding best practices can also improve Xcode’s efficiency during compilation. For more information, see [`Improving build efficiency with good coding practices`](improving-build-efficiency-with-good-coding-practices.md).

##### Measure the Time It Takes for Each Build Task

Before you perform any build optimizations, always gather timing information to see where optimizations might be most effective. Open your project in Xcode and choose Product > Perform Action > Build With Timing Summary to build your target with detailed timing information. To view the timing information for a specific build, select that build in the Report navigator.

![A screenshot of Xcode build results that include detailed timing information.](https://docs-assets.developer.apple.com/published/dfbcc8f34dce5c30e636d91c50997cef/improving-the-speed-of-incremental-builds-1%402x.png)

> **Note**: To generate timing information using the `xcodebuild` command-line tool, pass the `-showBuildTimingSummary` option to the tool.

The first time you build your project, Xcode builds everything, but subsequent builds are incremental. For each incremental build, pay particular attention to the preparation section and the specific tasks that Xcode performs for each target.

- If Xcode didn’t build your targets in parallel, open the Scheme Editor for your target and make sure the Build Order option is set to Dependency Order.
- Look for extraneous tasks, such as custom scripts, and assess whether Xcode needs to run those scripts during each incremental build.
- If compilation of a particular file takes significantly longer than other files, examine the file to see if header importation issues are causing the delay.

##### Declare Inputs and Outputs for Custom Scripts and Build Rules

If you use custom build scripts in your Xcode projects, make sure Xcode runs those scripts only when needed. You might use scripts to run custom tools, set build-environment variables programmatically, or perform other target-specific tasks. For example, you might use them to generate assets or other resource files from a proprietary data source. By default, Xcode runs custom scripts during every build cycle, including incremental builds. It also executes those scripts serially with respect to other tasks.

If you don’t need Xcode to run your scripts every time you build a target, provide at least one input file and one output file for the script. Xcode uses a script’s input and output files to determine when to run it. Specifically, Xcode runs your script when any of the following conditions are true:

- Your script doesn’t have any input files.
- Your script doesn’t have any output files.
- Your script’s input files changed.
- Your script’s output files are missing.

Specify input and output files, along with the script itself, in the Run Script build-phase editor. You may specify input and output files individually or in an Xcode file list — a file with an `.xcfilelist` filename extension that lists the name of each file on a separate line.

![A screenshot of the Run Script build-phase editor in Xcode.](https://docs-assets.developer.apple.com/published/3c4d87fe04d1d987ccd9f8e1fe61543b/improving-the-speed-of-incremental-builds-2%402x.png)

You must still specify an input and output file to prevent Xcode from running the script every time, even if your script doesn’t actually require those files. For a script that requires no input, provide a file that never changes as the input file. For a script with no outputs, create a static output file from your script so Xcode has something to check.

##### Create Module Maps for Custom Frameworks and Libraries

Module maps improve source compilation times by shortening the time it takes to import header files. A module map provides the compiler with a list of headers that the framework contains. When a framework includes a module map, the compiler doesn’t preprocess header files separately for each source file. Instead, it builds a cache of the framework’s symbol information and reuses that cache during subsequent compilations, which saves significant time.

The system frameworks already include module maps, but you must provide module maps for any custom frameworks in your project. To add a module map, enable the `DEFINES_MODULE` build setting for your framework or library. Xcode enables this build setting automatically for new frameworks, but you might need to set it for older projects. When enabled, the compiler produces a module map with the contents of your target’s public header files.

![A screenshot of the DEFINES_MODULE build setting in Xcode.](https://docs-assets.developer.apple.com/published/d3afac2c05ccaed02b9eae7b5d36503b/improving-the-speed-of-incremental-builds-3%402x.png)

> ❗ **Important**: To obtain the benefit from module maps, always include the framework name in any import statements. If you don’t include the framework name, the compiler can’t determine whether a module map is present. For more information on how to import header files from a module, see [`Include framework names in import statements`](improving-build-efficiency-with-good-coding-practices#Include-framework-names-in-import-statements.md).

Before you create a module map, make sure your framework meets the following requirements:

- Your framework’s header files must not rely on any external contextual information. Xcode compiles your module map separately from the rest of your project’s source files. Don’t rely on source-specific information to change the meaning or values of symbols in your headers.
- The module must be self contained. Because Xcode compiles module maps separately, your framework’s header files must include everything they need to compile correctly.

To get the maximum reuse benefit from module maps, compile your app’s source files with identical build options. Xcode builds your framework’s module map using the same options as the source file that imports that framework. If your app’s source files use different options, Xcode must recompile the module map for each new set of options. Using identical options allows Xcode to reuse the cache in each subsequent source file.

##### Make Sure Your Targets Dependencies Are Accurate

Verifying that your targets have accurate dependencies ensures they build correctly and in a timely manner. Out-of-date dependencies might force Xcode to build targets serially when it might have built them in parallel. Missing dependencies might cause correctness issues or even build errors. For example, if your app doesn’t have an explicit dependency to a separate code module, like an app extension, Xcode might build the app with an older version of the module that doesn’t work properly.

When you know a dependency exists between two targets in your Xcode project, create an explicit dependency between them. Xcode creates some dependencies automatically based on how you configure your project. For example, when you embed a new framework inside an existing app, Xcode automatically adds the framework to the app’s list of dependencies. At other times, you specify the dependencies yourself using the Dependencies build phase editor, as shown below. Use the + and - buttons to add or remove dependencies for your target.

![A screenshot of the Dependencies build phase in Xcode.](https://docs-assets.developer.apple.com/published/1702d5e45d4e6a62ea8e324909ef87df/improving-the-speed-of-incremental-builds-4%402x.png)

If a target depends on code in a different Xcode project, create a reference to that project by dragging it into the navigator pane of your current project. The presence of the other project in the navigator pane gives Xcode the information it needs to track dependencies on items in the other project. Without this reference, Xcode doesn’t know to build your target when the remote project changes.

##### Refactor Your Targets to Improve Parallelism

Inter-target dependencies require Xcode to build those targets in a specific order. When a target has many dependencies, or when it depends on large, monolithic modules, Xcode must serialize more tasks. To improve build performance, simplify your target’s dependency list, and break up monolithic targets so that Xcode can do more work in parallel.

Consider the following illustration, which shows an XML engine that depends on a monolithic utilities framework. Although the XML engine relies on only a small portion of the framework, Xcode must rebuild the engine when any part of the framework changes. Breaking up the framework into smaller modules and creating more fine-grained dependencies might eliminate some unnecessary rebuilds. In the refactored version, changes to the utilities framework no longer trigger an automatic rebuild of the XML engine.

![An illustration that compares monolithic and refactored modules by showing that XML parsing is now outside the utilities framework in the refactored module.](https://docs-assets.developer.apple.com/published/80621ea35b76167cecccabf9e92ffadd/improving-the-speed-of-incremental-builds-5%402x.png)

When one target depends on many child targets, Xcode cannot start to build the target until it finishes all of the children. Consider a single Tests target that executes automated tests on an app, app extension, and private framework. Splitting up the tests by target allows Xcode to run each suite independently as soon as the corresponding target is ready, which increases parallelization.

![An illustration that changes a single test target dependent on three other targets, into three test targets with each dependent on only one other target. ](https://docs-assets.developer.apple.com/published/1b4d5805094686fd2ec3a8057fd641ed/improving-the-speed-of-incremental-builds-6%402x.png)

You need to decide whether modifications to your project’s targets offer any benefit. Increasing the number of targets can improve parallelization, but it also adds complexity to your project. Always validate any target or dependency changes to ensure your code still builds correctly. In addition, always measure the speed of the resulting builds to verify that the changes lead to tangible improvements.

## See Also

- [Configuring your project to use mergeable libraries](configuring-your-project-to-use-mergeable-libraries.md)
  Use mergeable dynamic libraries to get app launch times similar to static linking in release builds, without losing dynamically linked build times in debug builds.
- [Improving build efficiency with good coding practices](improving-build-efficiency-with-good-coding-practices.md)
  Shorten compile times by reducing the number of symbols your code exports and by giving the compiler the explicit information it needs.
- [Building your project with explicit module dependencies](building-your-project-with-explicit-module-dependencies.md)
  Reduce compile times by eliminating unnecessary module variants using the Xcode build system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/improving-the-speed-of-incremental-builds)*