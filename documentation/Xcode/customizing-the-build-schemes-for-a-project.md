# Customizing the build schemes for a project

**Framework**: Xcode

Specify which targets to build, and customize the settings Xcode uses to build, run, test, and profile those targets.

#### Overview

When you build, run, test, profile, or archive part of your project, Xcode uses the selected build scheme to determine what to do. A build scheme contains a list of targets to build, and any configuration and environment details that affect the selected action. For example, when you build and run an app, the scheme tells Xcode what launch arguments to pass to the app. Xcode provides default schemes for most targets, and you can customize those schemes or create new ones as needed.

To view your project’s current schemes, click the scheme name in the toolbar of your project window. Xcode displays a pop-up menu with a list of current schemes at the top, and commands to edit, create, and manage schemes at the bottom.

![A pop-up menu displays a list of schemes present in an Xcode project.](https://docs-assets.developer.apple.com/published/f7afef3afd8dd907dae0a062d8309f1b/build-select-scheme%402x.png)

To view and modify your project’s current schemes, select Manage Schemes. For example, disable automatic creation of schemes for new targets, and change scheme attributes such as which project contains the scheme. By default, Xcode shares schemes with other team members.

![The scheme manager panel shows the list of available schemes and offers controls to create new schemes.](https://docs-assets.developer.apple.com/published/8a6af9ca0a4d865322845f6ef0328d34/build-scheme-manage%402x.png)

##### Specify the Build Options for a Schemes Targets

When you tell Xcode to build a scheme, Xcode analyzes your project and generates the list of tasks required to build the targets of that scheme. To speed up builds, Xcode executes as many tasks as possible in parallel, taking advantage of whatever resources are available. To ensure that products build correctly, Xcode serializes tasks when dependencies exist between them. For example, Xcode builds a private framework before it builds the app that links against that framework.

To see a scheme’s current list of targets, edit the scheme and select the Build page. Use this page to add or remove targets and to configure additional build options.

![The edit scheme panel shows the targets and build configuration settings for an Xcode project.](https://docs-assets.developer.apple.com/published/3d00600bbd55e5ccb3ec5d0ef243e337/build-scheme-build-configuration%402x.png)

The following table lists the build options you can configure for your schemes.

| Build option | Description |
| --- | --- |
| Dependency Order | Build targets in parallel according to their dependencies. Choose this option, not Manual Order. |
| Manual Order | Build targets serially in the order listed in the scheme, underutilizing your Mac’s multiple processors. This option is deprecated. Don’t use it. |
| Find Implicit Dependencies | Gather information about additional dependencies during a build. The build system uses this information to help schedule build-related tasks. |

##### Specify Launch Arguments and Environment Variables

If your product configures itself using command-line arguments or environment variables, specify that information on the Arguments tab of the Run, Test, or Profile build scheme action.

- Xcode configures and exports environment variables before it runs the process.
- Xcode passes command-line arguments directly to the launched process.

##### Configure the Runtime Environment for Built Products

In the Run, Test, and Profile build scheme actions, the Info tab contains high-level information about how to launch and run your product. Some options are available for all build actions, but some options are specific to the current build action. The following table lists the available options.

| Action | Attribute | Description |
| --- | --- | --- |
| Run, Test, Profile | Build Configuration | Use configurations to allow a project to customize its build settings based on the configuration name. A debug configuration typically disables code optimizations for faster builds and enables the generation of debugging information. A release configuration enables code optimizations for better runtime performance and disables the generation of debugging information to reduce app size. |
| Run, Profile | Executable | The executable to run after a successful build. For an app, this attribute contains the app itself. For other products, specify the app to launch. |
| Run, Test | Debug Executable | An option to attach the debugger at launch time. |
| Run | Siri Intent Query | The string to feed to Siri to initiate a query. Leave this field blank to initiate queries on the device using the Siri interface. |
| Run, Test | LLDB Init File | The LLDB settings file to load. Specify command aliases and other debugger-related settings. |
| Run | Launch | The launch behavior. Typically, Xcode launches apps automatically after a successful build, but you can specify a different time to launch the app. |
| Test | Debug Process As | The system account to use for debugging. |
| Profile | Instrument | The performance metrics to gather in the Instruments app. |

Xcode uses information in the Options tab to configure the runtime environment for a product. Use these options to override language settings or specify simulated device data such as the current location. The following table lists the available options.

| Action | Attribute | Description |
| --- | --- | --- |
| Run | Core Location | Options to simulate location data. Select a default starting location from the pop-up menu. |
| Run | App Data | An `.xcappdata` package that contains the initial contents of the app’s container directory. Create app data packages from the Devices and Simulators window. Install the app on your device so that it appears in the window. Select the app and use the controls to download the app’s current container. Modify the contents of the downloaded `.xcappdata` file as needed, and add the file to your project. |
| Run | Routing App Coverage File | A GeoJSON file that defines the geographical region the app covers. |
| Run | StoreKit Configuration | A `.storekit` data file that contains the items your app makes available for purchase. Use this file to test your app’s StoreKit support. For more information, see [`Setting up StoreKit Testing in Xcode`](setting-up-storekit-testing-in-xcode.md) |
| Run | GPU Frame Capture | An option to capture diagnostic information about your app’s Metal usage. For more information, see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md). |
| Run | Background Fetch | An option to simulate the app’s launch from a background event. Use this option to test your background execution workflows. |
| Run | Localization Debugging | An option to highlight nonlocalized strings in your app. |
| Run, Test | App Language | The language to use during testing. Select System Language to use the device’s default language. |
| Run, Test | App Region | The locale to use during testing. Select System Region to use the device’s default region. |
| Run | XPC Services | Options to debug XPC services. |
| Run | View Debugging | An option to collect information about an app’s view hierarchies. |
| Run | Queue Debugging | An option to record backtraces for dispatch queues. |
| Run | Interface Builder | An option to attach automatically to remote tools. |
| Test | UI Testing | Options to capture screenshots as part of testing your product’s UI. |
| Test | Attachments | An option to delete attachments when a test succeeds. |
| Test | Code Coverage | An option to gather code coverage metrics for your test targets. |
| Profile | Testability | An option to enable testability when profiling tests. |

##### Run Diagnostics on Your Target

Xcode includes tools to validate the stability of your code and eliminate potential bugs. These tools annotate your code with runtime checks that examine specific types of operations. For example, one tool detects potential race conditions between your app’s threads. Enable these checks from the Diagnostics tab of your build scheme.

The following table lists the supported diagnostics.

| Action | Attribute | Description |
| --- | --- | --- |
| Run, Test | Runtime Sanitization | Options to detect memory corruption, race conditions, and code that yields undefined results. For more information, see [`Diagnosing memory, thread, and crash issues early`](diagnosing-memory-thread-and-crash-issues-early.md). |
| Run, Test | Runtime API Checking | An option to detect system APIs running incorrectly on threads other than the main thread. For more information, see [`Diagnosing memory, thread, and crash issues early`](diagnosing-memory-thread-and-crash-issues-early.md). |
| Run, Test | Memory Management | Options to detect buffer overflow and other memory-related errors. |
| Run | Metal | Options to validate your app’s usage of Metal APIs and shaders. For more information, see [`Metal developer workflows`](metal-developer-workflows.md). |

To detect memory-related issues, Xcode supports the following diagnostics:

- Malloc Scribble writes the value `0x55` to every byte of a released memory block. This action helps you detect code that accesses the released block.
- Malloc Guard Edges adds guard pages before and after large allocations. These pages detect code writes beyond the boundaries of an allocated memory block.
- Guard Malloc uses several techniques to crash your app at the point where a memory error occurs.
- Zombie Objects detects code that tries to access an already released object.
- Malloc Stack Logging captures function call stack information at the time of each memory allocation.
- Memory Graph on Resource Exception captures information about your memory graph. You can view the information in the debugger.

##### Run Tasks Before or After Scheme Actions

For each action in your scheme, you can run scripts or send emails before or after Xcode performs that action using pre-actions and post-actions. For example, you might use a post-action to log test results to a custom server each time you run your code. Unlike build phases, Xcode executes your actions only when you select the appropriate command from the Product menu.

To add a pre-action or post-action:

1. Click the disclosure triangle for the action.
2. Select Pre-actions or Post-actions
3. Click the Add button (+) and select the type of action to add.
4. Configure the details of the action.

![The edit scheme panel shows the pre- and post-actions for the Test command.](https://docs-assets.developer.apple.com/published/1d7d15e51847c8f5a4a54b88d76a3593/build-scheme-prepost-actions%402x.png)

For script actions, Xcode exposes the build settings for one of the scheme’s selected targets. Use environment variables to access the values of those variables. For a list of available build settings, see [`Build settings reference`](build-settings-reference.md).

## See Also

- [Customizing the build phases of a target](customizing-the-build-phases-of-a-target.md)
  Specify the tasks to perform during a build, including the source files to compile, the scripts to run, and the resources to include in the final product.
- [Creating build rules for custom file types](creating-build-rules-for-custom-file-types.md)
  Tell Xcode how to build your project’s custom file types, and provide dependency information to optimize the build process for each file.
- [Running custom scripts during a build](running-custom-scripts-during-a-build.md)
  Execute custom shell scripts during the build process, and run tools or other commands that your project requires.
- [Running code on a specific platform or OS version](running-code-on-a-specific-version.md)
  Add conditional compilation markers around code that requires a particular family of devices or minimum operating system version to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/customizing-the-build-schemes-for-a-project)*