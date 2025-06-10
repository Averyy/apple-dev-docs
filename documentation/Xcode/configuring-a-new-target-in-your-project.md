# Configuring a new target in your project

**Framework**: Xcode

Configure your project to build a new product, and add the code and resources the product requires.

#### Overview

A target specifies a product to build, such as an app, framework, app extension, or unit test. A project can contain multiple targets, usually representing related parts of a single product. For example, a project might contain separate targets for an app, a private framework, an app extension, and a suite of tests.

When you create a new project from a template, Xcode adds one or more targets to the project automatically. For example, the multiplatform app template contains separate targets for an iOS app and Mac app.

![An Xcode project that contains three targets.](https://docs-assets.developer.apple.com/published/fde42f90bbd1c2fbf1b5c60aa1805f67/build-targets%402x.png)

To view the targets in a project, select the project in the navigator area. The editor area displays the current project and target information. Select a target to view general information about it, and to view its current build settings and capabilities. Changes you make to a target’s configuration affect that target only. Changes you make to the project affect all targets.

##### Add a New Target to Your Project

Add new targets to create separate products in your project, augment an existing app using app extensions, or factor code into a private framework. You can also add new apps, system extensions, test suites, and other types of targets to your project.

To add a new target:

1. Choose File > New > Target.
2. Select the platform for the new target.
3. Choose a starting template.
4. Click Next.
5. Provide a name for the target and configure other target-related options, such as the programming language.
6. Click Finish.

![A sheet displays the available templates for a new target.](https://docs-assets.developer.apple.com/published/73ad9e85b4ef36d52a2c29823db05767/build-target-templates%402x.png)

You can embed some types of targets, directly into the bundle of an existing app. This option simplifies the setup process for frameworks, app extensions, and other products that you plan to ship inside your app. When you embed a target, Xcode configures the necessary project settings to build the target and copy it into your app. Xcode also creates the necessary dependencies to ensure that the targets build in the proper order.

##### Add Source Files and Other Content to a Target

Target templates contain default files to help you start development. Choose File > New to create new files and embed them directly into an existing target. To assign an existing file to a new target, select the file and update its membership attributes in the Identity inspector.

![The inspector that shows which targets contain the selected file.](https://docs-assets.developer.apple.com/published/fd2e4a4fcb17245adc1c69b040d395d5/build-target-membership-settings%402x.png)

For more information about how to add files to a project, see [`Managing files and folders in your Xcode project`](managing-files-and-folders-in-your-xcode-project.md).

##### Configure a Dependency Between Two Targets

Dependencies tell Xcode the correct order in which to build a set of targets. Xcode builds targets in parallel when it can, but sometimes it must build targets serially. For example, Xcode must build a custom framework before it builds an app that links against that framework. When you embed a new target inside an app, Xcode creates a dependency between the app and target if the scheme’s Find Implicit Dependencies option is enabled. If that option is disabled, you must configure the dependency yourself.

To view and add dependencies, select a target and open its build phase settings. The Dependencies build phase contains the targets that Xcode must successfully build before it builds the current target. Xcode can build multiple dependent targets simultaneously if there are no interdependencies between those targets.

![The editor area that displays the target’s explicit dependencies.](https://docs-assets.developer.apple.com/published/50c07a081d62561b8dae9d40fa1ffc77/build-phase-settings-dependencies%402x.png)

When there’s a relationship between targets that Xcode can’t easily detect, add dependencies manually. While Xcode can add dependencies automatically when the Find Implicit Dependencies build scheme option is enabled, it can’t detect all dependencies. For example, Xcode can’t detect when a target relies on data files built by a custom script in another target. If you don’t specify a needed dependency, Xcode might report errors or build the targets incorrectly.

> **Note**: If your target depends on content in a different Xcode project, add a reference to the project before configuring any dependencies. For more information, see [`Managing multiple projects and their dependencies`](managing-multiple-projects-and-their-dependencies.md).

For more information on optimizing your targets to improve build times, see [`Improving the speed of incremental builds`](improving-the-speed-of-incremental-builds.md).

## See Also

- [Configuring a multiplatform app](configuring-a-multiplatform-app-target.md)
  Share project settings and code across platforms in a single app target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project)*