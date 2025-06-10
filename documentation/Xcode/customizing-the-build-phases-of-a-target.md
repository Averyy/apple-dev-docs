# Customizing the build phases of a target

**Framework**: Xcode

Specify the tasks to perform during a build, including the source files to compile, the scripts to run, and the resources to include in the final product.

#### Overview

When you build a target in your Xcode project, the build system executes a specific set of tasks to produce the resulting product. In Xcode, you specify the files and scripts for your target using build phases. The build system then uses that information and other build settings to determine the tasks required to build the target.

Xcode configures the initial build phases for each target at creation time, but you can add or modify those build phases later. You might add build phases to copy additional files to your app bundle, or to execute custom shell scripts. You can also examine the build phases to diagnose potential issues. For example, you might make sure that Xcode is linking your code against third-party libraries that your code uses.

##### View and Add Build Phases to a Target

To view the build phases for a target, select the target and navigate to the Build Phases tab, as shown in the following figure. To add a new build phase, click the Add button (+) and select an appropriate build phase from the pop-up menu. Xcode disables any menu options that aren’t valid. For example, Xcode disables the Compile Sources build phase if your target already contains a build phase of that type.

![A figure that shows the build phases associated with a target.](https://docs-assets.developer.apple.com/published/2f0001d8c395d742c2d1420e82ce719a/build-phase-editor%402x.png)

Xcode supports the following build phases:

-  Specifies other targets, in the same project or a referenced project, that Xcode must build before it builds the current target. The order of the targets indicates the order in which Xcode starts building them. Xcode builds multiple dependent targets in parallel when possible. For information about how to configure a dependency, see [`Configuring a new target in your project`](configuring-a-new-target-in-your-project.md).
-  Contains the list of source files to compile. This build phase typically contains Swift and Objective-C files, but it can contain any other compilable source files. You can specify distinct compiler flags for each source file. A target can include only one build phase of this type. You can’t include this build phase in Aggregate and External Build Tool targets.
-  Links your compiled sources with other frameworks and libraries. With this build phase, Xcode links your code against Apple frameworks, platform libraries, and any other frameworks and libraries you list explicitly. A target can include only one build phase of this type. You can’t include this build phase in Aggregate and External Build Tool targets. For more information, see [`Link against additional frameworks and libraries`](https://developer.apple.com#Link-against-additional-frameworks-and-libraries).
-  Copies files to the bundle directory designated for resources. On macOS, the designated resources directory is the `Contents\Resources` directory. On iOS, the bundle stores global resources in the bundle’s `Contents` directory. As part of the copy operation, the build system can process the files first, and copy the results to the bundle. A target can include only one build phase of this type, and the target must have a bundle directory. For more information, see [`Copy files to the finished product`](https://developer.apple.com#Copy-files-to-the-finished-product).
-  Associates public, private, or project header files with the target. Public and private headers define the API that the target exposes to external clients. Xcode copies these header files into `Headers` and `PrivateHeaders` subfolders within the built product. Project headers contain the API that the target uses, but Xcode doesn’t expose the API to external clients. A target can include only one build phase of this type. For more information, see [`Add public and private headers to a target`](https://developer.apple.com#Add-public-and-private-headers-to-a-target).
-  Copies files and other built products to the specified destination. The build system normally doesn’t process files you specify using this build phase, but you can change that behavior by enabling the `APPLY_RULES_IN_COPY_FILES` build setting. When copying other products, this build phase signs the products if necessary. A target can contain multiple build phases of this type. For more information, see [`Copy files to the finished product`](https://developer.apple.com#Copy-files-to-the-finished-product).
-  Runs a custom shell script, which you might use to execute custom tools and logic at specific points in the build process. A target can contain multiple build phases of this type. For more information on creating and managing build scripts, see [`Running custom scripts during a build`](running-custom-scripts-during-a-build.md).

> **Note**: For some operations, Xcode customizes the name of an existing build phase to reflect the corresponding action. For example, when you embed a framework in an app, Xcode configures a Copy Files build phase with the title Embed Frameworks.

After you add a build phase, configure its contents. For most build phases, you add one or more files related to the associated task. In some cases, you can also configure additional settings. For example, in the Compile Sources build phase, you can add compiler flags to individual files.

Xcode adds new build phases to the end of the list initially. You can rearrange build phases by dragging them in the editor, but Xcode still executes tasks according to dependency order. To remove a build phase from your target, click the close button (x) next to that build phase.

##### Link Against Additional Frameworks and Libraries

Most targets include a Link Binary with Libraries build phase, which resolves your code’s references to frameworks, libraries, external XCFrameworks, and library products in Swift packages. If your project relies on custom libraries, add them to this build phase and specify the linkage type. For each library, you can specify the following details.

- For multiplatform targets, use the Filters control to specify which platforms to support.
- Specify whether a library is required or optional. This option reflects legacy link options for some frameworks. Do not change this setting in modern projects.

![A figure that shows the configuration options for a library in the link build phase.](https://docs-assets.developer.apple.com/published/51e6e02cc3bd4e9f03b952ca606177c7/build-link-options%402x.png)

Xcode automatically links your Swift code against Apple frameworks and libraries, so you don’t need to include them in this build phase. For C, C++, and Objective-C code, Xcode links against Apple frameworks and libraries only when the `CLANG_MODULES_AUTOLINK` build setting is enabled, which it is by default. Add any add third-party libraries or custom libraries from your own project to this build phase.

##### Add Public and Private Headers to a Target

Frameworks and libraries typically expose APIs for external clients to call, and other targets can expose APIs too. If your target exposes any API to external clients, use a Headers build phase to add the appropriate header files to the built product. Clients use your header files to learn about and call the available APIs.

In the Headers build phase, drag files to one of three sections:

- Drag files with publicly supported symbols to the Public section. Public headers represent the public contract between your code and any clients that access it. Xcode places these files in a `Headers` directory inside the bundle.
- Drag files with private symbols to the Private section. Private headers contain additional interfaces that you make available to clients, but that aren’t necessarily part of the public contract between your code and clients. Xcode places these files in a `PrivateHeaders` directory inside the bundle.
- Drag files that contain internal project interfaces to the Project section. Xcode doesn’t copy these files into the built product.

When Xcode copies files to the built product, the Headers build phase usually doesn’t modify files. However, if you enable the `COPY_HEADERS_RUN_UNIFDEF` build setting, Xcode runs the `unifdef` tool over your headers to remove preprocessor conditional code.

##### Copy Files to the Finished Product

To copy custom resources or data files into a bundle, add a Copy Files or Copy Bundle Resources build phase to your target. Xcode uses a Copy Bundle Resources build phase to copy storyboards and asset catalogs to the appropriate directory for resources, which differs by platform. Xcode also uses instances of the Copy Files build phase to embed frameworks, app extensions, app clips, and other content inside your bundle. You use these build phases to copy other project files into a bundle. For example, you might copy templates for new documents into your app’s bundle.

![A figure that shows the Copy Bundle Resources and Copy Files build phases for a target.](https://docs-assets.developer.apple.com/published/8484d6cea58a1181baeb7e2985e597c5/build-copy-files-phase%402x.png)

The Copy Bundle Resources build phase places files in the bundle’s designated resource directory. The Copy Files build phase supports the following destination directories:

- Products Directory: Places items in the same directory as the built product.
- Wrapper: Places items in the root of the bundle directory.
- Executables: Places items in the same directory as the bundle’s main binary.
- Resources: Places items in the platform-specific directory for resources.
- Java Resources: Places items in the `Resources/Java` subfolder.
- Frameworks: Places items in the `Frameworks` subfolder.
- Shared Frameworks: Places items in the `SharedFrameworks` subfolder.
- Shared Support: Places items in the `SharedSupport` subfolder.
- Plugins: Places items in the `Plugins` subfolder.
- XPC Services: Places items in the `XPCServices` subfolder.
- System Extensions: Places items in the `Library/SystemExtensions` subfolder.
- App Clips: Places items in the `AppClips` subfolder.

For each build phase, you can supply a subpath string to copy files to a specific subdirectory of the target destination. For example, if you select the Resources destination for a Mac app and include the subpath string `Templates`, Xcode copies the files to the `Resources/Templates` subfolder in the app bundle.

> **Note**: The Copy Files build phase supports signing any resources you place in the bundle. Typically, you use this option when copying built products such as app extensions to your bundle.

For details on the location of platform-specific bundle directories, see [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle)

## See Also

- [Customizing the build schemes for a project](customizing-the-build-schemes-for-a-project.md)
  Specify which targets to build, and customize the settings Xcode uses to build, run, test, and profile those targets.
- [Creating build rules for custom file types](creating-build-rules-for-custom-file-types.md)
  Tell Xcode how to build your project’s custom file types, and provide dependency information to optimize the build process for each file.
- [Running custom scripts during a build](running-custom-scripts-during-a-build.md)
  Execute custom shell scripts during the build process, and run tools or other commands that your project requires.
- [Running code on a specific platform or OS version](running-code-on-a-specific-version.md)
  Add conditional compilation markers around code that requires a particular family of devices or minimum operating system version to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/customizing-the-build-phases-of-a-target)*