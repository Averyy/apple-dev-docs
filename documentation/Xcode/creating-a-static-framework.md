# Creating a static framework

**Framework**: Xcode

Configure your project to build a new static framework.

#### Overview

In Xcode 15 or later, you can use a static framework to bundle resources with a static library. A static framework is a framework bundle whose main binary is a static archive. When a client links and embeds the framework, Xcode 15 or later omits the main binary from the embedded framework bundle because it’s already statically linked into the client. To create a static framework in Xcode, create a new framework target, configure the new target as a static framework target, and add all your source files and resources to the new framework target. Build, analyze, and test your static framework for each platform that it supports.

To distribute your static framework, configure its target for distribution in Xcode, then create an archive of your framework for each platform that it supports. Package all variants of your framework into an XCFramework bundle that you can sign. For more information about configuring and archiving your static framework for distribution, and creating an XCFramework bundle, see [`Creating a multiplatform binary framework bundle`](creating-a-multi-platform-binary-framework-bundle.md). Xcode verifies if your static framework’s code signature is tampered or becomes invalid. For more information about verifying XCFrameworks, see [`Verifying the origin of your XCFrameworks`](verifying-the-origin-of-your-xcframeworks.md).

##### Add a New Framework Target to Your Project

You can add the new framework target to an existing Xcode project. Create a framework that supports either a single platform or multiple platforms.

To add a new framework target:

1. Choose File > New > Target.
2. In the sheet that appears, choose the platform you wish to support. To create a framework that supports a single platform, choose that platform in the sheet. To create a framework that supports multiple platforms, choose Multiplatform in the sheet.
3. Scroll down to the Framework & Library section.
4. Select the Framework template.
5. Click Next.
6. Specify the name of your framework and configure the language and other options.
7. Click Finish.

![A sheet displays the available templates for a new target. The multiplatform framework template is selected.](https://docs-assets.developer.apple.com/published/143b7c7bd31699fa966b3c1041d09ebc/creating-a-static-framework-1%402x.png)

When you create a new framework target from a template, Xcode adds a target that builds a dynamic framework automatically. It also adds an umbrella header to the target. The header’s name is generated from your framework name, followed by a dot and the letter . For example, if you name your framework SampleFramework, Xcode automatically adds a header file with the name `SampleFramework.h` to the target.

##### Convert the New Framework Target From Dynamic to Static

After adding the new framework target to your Xcode project, set its Mach-O Type build setting to Static Library to convert it from dynamic to static. For more information about the Mach-O Type build setting, see the [`Build settings reference`](build-settings-reference.md).

To edit the Mach-O Type build setting:

1. In the project editor, select your new framework target, then click Build Settings.
2. Enter “Mach-O Type” in the search field to locate the Mach-O Type build setting.
3. Choose Static Library from the setting value list.

![A screenshot that shows the Mach-O Type build setting.](https://docs-assets.developer.apple.com/published/e09ee14d3776881b016058a989030da8/creating-a-static-framework-2%402x.png)

##### Add Source Files to Your Framework Target

After you have a static framework target, add new or existing source files, such as Swift files, to the target. After adding them, check that these files appear in the Compile Sources build phase of the static framework target. For more information on adding new or existing files to a target, see [`Managing files and folders in your Xcode project`](managing-files-and-folders-in-your-xcode-project.md).

![A screenshot that shows the Compile Source build phase for a target.](https://docs-assets.developer.apple.com/published/dd1ae368cdbbddbc987b8c18f68bae59/creating-a-static-framework-3%402x.png)

##### Add Resources to Your Framework Target

You can add resources such as asset catalogs, storyboards, image files, and a privacy manifest to a static framework. The resource files appear in the Copy Bundle Resources build phase of the static framework target. The following image shows the Copy Bundle Resources build phase of a static framework that includes a privacy manifest file:

![A screenshot that shows the Copy Bundle build phase for a target. The phase contains a privacy manifest file.](https://docs-assets.developer.apple.com/published/59f30f7d7ccb38f873be5673399d9ea2/creating-a-static-framework-4%402x.png)

To add a privacy manifest to your static framework in Xcode, see [`Privacy manifest files`](https://developer.apple.com/documentation/BundleResources/privacy-manifest-files).

##### Add Public and Private Headers to Your Framework Target

If your static framework target contains public or private headers that you want to make available to external clients, add a Headers build phase to your target, then drag these files into Headers. For more information about adding public and private headers to a target, see [`Customizing the build phases of a target`](customizing-the-build-phases-of-a-target.md).

Additionally, add your public headers to your framework umbrella header.

##### Build Analyze and Test Your Framework

Build, analyze, and test your static framework for each platform that it supports. The example below shows the bundle structure of `SampleFramework` after building it for iOS:

To test your static framework, create a release build of your framework, then embed it in an app that utilizes it. For more information about creating a release build of your static framework, see [`Testing a release build`](testing-a-release-build.md). Build and run the test app.

##### Embed Your Framework in an App

To embed your static framework in an app:

1. In the project editor, select the app target, then click General.
2. Expand the Frameworks, Libraries, and Embedded Content section.
3. Click the Add button (+), select Add Other, then choose Add Files to locate your static framework.
4. Click Open.
5. Choose the Embed & Sign option from the Embed value list for the static framework.

![A screenshot that shows the Frameworks, Libraries, and Embedded Content section in the target editor area.](https://docs-assets.developer.apple.com/published/f0b1f4d431c00517b5691dba0834d2d6/creating-a-static-framework-6%402x.png)

## See Also

- [Creating a multiplatform binary framework bundle](creating-a-multi-platform-binary-framework-bundle.md)
  Combine variants of a binary framework or library into an XCFramework bundle that supports multiple platforms.
- [Identifying and addressing framework module issues](identifying-and-addressing-framework-module-issues.md)
  Detect and fix common problems found in framework modules with the module verifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-a-static-framework)*