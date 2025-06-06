# Making dependencies available to Xcode Cloud

**Framework**: Xcode

Review dependencies and make them available to Xcode Cloud before you configure your project to use Xcode Cloud.

#### Overview

Xcode Cloud combines the tools you use to create apps and frameworks: [`Xcode`](https://developer.apple.comhttps://developer.apple.com/xcode/), [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/), and [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). However, your Xcode project or workspace may require additional dependencies or third-party tools to compile your code. For example, you may use a library created by the open source community or Swift package dependencies to reuse and share code between apps.

If Xcode Cloud can’t access a private dependency or a third-party tool, it won’t be able to successfully build your project. To avoid a failing build and save time when you start using Xcode Cloud, review your dependencies and make sure that Xcode Cloud can access them before configuring your project to use Xcode Cloud.

> **Note**: The temporary build environment that Xcode Cloud uses includes tools that are part of macOS and Xcode — for example, Python — and additionally [`Homebrew`](https://developer.apple.comhttps://brew.sh) to support installing third-party dependencies and tools. For more information, see the “Use a custom build script to install a third-party dependency or tool” section below.

##### Use Swift Package Dependencies and Git Submodules

Xcode Cloud supports Swift packages and dependencies that you manage using Git submodules without any separate configuration if their repositories are publicly accessible. If you use private dependencies, Xcode Cloud helps you access them. For more information on using them, see [`Grant Xcode Cloud access to private dependencies`](making-dependencies-available-to-xcode-cloud#Grant-Xcode-Cloud-access-to-private-dependencies.md) below.

Following the best practice for using Swift package dependencies in a CI/CD environment, Xcode Cloud doesn’t use automatic package resolution and instead relies on the `Package.resolved` file to resolve your dependencies. If you use Swift package dependencies in your project, make sure to include the `Package.resolved` file in your Git repository and commit any changes to it. Don’t include the file in your `.gitignore` file. Additionally, make sure the `Package.resolved` file resides at `$filename.xcodeproj/project.workspace/xcshareddata/swiftpm/Package.resolved`.

> **Note**: Forcing Xcode Cloud to use automatic package resolution — for example, by changing settings in a custom build script — may result in undefined behavior and failing builds.

For general information on building Swift packages in a continuous integration and delivery environment, see [`Building Swift packages or apps that use them in continuous integration workflows`](building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows.md).

##### Grant Xcode Cloud Access to Private Dependencies

When you configure your project or workspace to use Xcode Cloud, Xcode detects the source code management (SCM) provider you use to host your code. It also detects the SCM provider for each private Git submodule, Swift package dependency, or Git repository you access in a custom script and helps you grant Xcode Cloud access to it. For example, if you host your code with [`Bitbucket Server`](https://developer.apple.comhttps://bitbucket.org/product/enterprise) and use a private dependency you host with [`GitLab`](https://developer.apple.comhttps://gitlab.com), Xcode helps you connect both your Bitbucket Server and your GitLab account to Xcode Cloud.

If you add a new private package dependency that Xcode Cloud can’t access, the next build fails. To resolve the issue, navigate to the failed build’s build report, and let Xcode or App Store Connect help you connect Xcode Cloud to the dependency’s SCM provider.

> **Note**: You need to host your private dependencies with one of the supported SCM providers. For more information on supported SCM providers, see [`Source code management setup`](source-code-management-setup.md).

Building your project may require access to more than one instance of your self-hosted SCM provider — a common case for large teams. For example, you may use two different GitHub Enterprise instances where one hosts your app’s code and the other hosts your dependencies. If this scenario applies to you, finish the initial onboarding workflow for the project in Xcode and connect the instance that hosts your app’s code, then let the first build fail. After the build failure, Xcode suggests a fix to connect the other instance.

##### Review Third Party Dependencies

If you use a third-party dependency manager like [`CocoaPods`](https://developer.apple.comhttps://cocoapods.org) or [`Carthage`](https://developer.apple.comhttps://github.com/Carthage/Carthage), or require an additional tool to successfully build your project, you’ll need to make changes to your project or workspace before you can use Xcode Cloud.

Because third-party tools and dependencies require additional work, review and simplify your third-party dependencies before you configure your project or workspace to use Xcode Cloud. For example, you may be able to replace a dependency with a framework that Apple provides. Alternatively, see if its creator offers the dependency as a Swift package. If so, you can use the package and take advantage of the support for the Swift Package Manager without configuring Xcode Cloud to use a third-party tool.

If switching to a Swift package dependency or removing a dependency isn’t practical, follow the instructions below to ensure Xcode Cloud can access dependencies and required tooling.

##### Use a Custom Build Script to Install a Third Party Dependency or Tool

The temporary build environment Xcode Cloud uses to perform a build doesn’t include third-party tools or dependencies. However, it includes [`Homebrew`](https://developer.apple.comhttps://brew.sh), an open source package manager you can use to install additional software. For example, you can use Homebrew to install dependency managers like [`CocoaPods`](https://developer.apple.comhttps://cocoapods.org) or [`Carthage`](https://developer.apple.comhttps://github.com/Carthage/Carthage).

To install a tool with Homebrew:

1. Create a directory next to your Xcode project or workspace and name it `ci_scripts`.
2. Create an executable shell script, name it `ci_post_clone.sh`, and save it in the `ci_scripts` directory. For example, use the Shell Script template in Xcode to create the file, and then make it an executable by running `chmod +x ci_post_clone.sh` in Terminal.
3. Open the custom script in Xcode and add the necessary commands to install a tool with Homebrew.

> **Note**: You can use custom build scripts to perform a variety of tasks, but you can’t obtain administrator privileges by using `sudo`.

For more information about custom build scripts, see [`Writing custom build scripts`](writing-custom-build-scripts.md).

##### Make Cocoapods Dependencies Available to Xcode Cloud

CocoaPods is an open source dependency manager for Apple platforms. However, the temporary build environment that Xcode Cloud uses to perform a build doesn’t come with the tool pre-installed. If you use CocoaPods, first make sure you commit both your `Podfile` and the `Podfile.lock` file. Then, decide between one of the following options:

- Add the `Pods` directory to your Git repository by committing it.
- Exclude the `Pods` directory from source control by adding it to your `.gitignore` file.

If you commit the `Pods` directory and its contents, you won’t need to install CocoaPods to enable Xcode Cloud to build your project or workspace. It’s worth noting, however, that your source code repository takes up more space when adding the `Pods` directory. Additionally, remember that committing binary dependencies can affect the performance of your Git repository. It’s a general issue when using Git and not specific to Xcode Cloud.

> 💡 **Tip**: If you decide to commit the `Pods` directory, consider using [`Git LFS`](https://developer.apple.comhttps://git-lfs.github.com) . It’s pre-installed on the temporary build environment Xcode Cloud uses to build your project.

If you choose to exclude the `Pods` directory from source control, you’ll need to install CocoaPods using a custom build script. The benefit, however, is that the source code repository takes up less disk space and doesn’t slow down your Git repository. To install CocoaPods using a custom build script:

1. Create a post-clone script as described in [`Use a custom build script to install a third-party dependency or tool`](making-dependencies-available-to-xcode-cloud#Use-a-custom-build-script-to-install-a-third-party-dependency-or-tool.md).
2. Add commands to the script that install CocoaPods with [`Homebrew`](https://developer.apple.comhttps://brew.sh) and that download your CocoaPods dependencies. The following code snippet shows a basic script to achieve this: ```bash
#!/bin/sh

# Install CocoaPods using Homebrew.
brew install cocoapods

# Install dependencies you manage with CocoaPods.
pod install
```

##### Make Carthage Dependencies Available to Xcode Cloud

Carthage is an open source dependency manager for Apple platforms. However, the temporary build environment that Xcode Cloud uses to build your project doesn’t come with the tool pre-installed. To facilitate projects that rely on the `carthage copy-frameworks` command — most projects do — , install Carthage using a custom build script:

1. Create a post-clone script as described in [`Use a custom build script to install a third-party dependency or tool`](making-dependencies-available-to-xcode-cloud#Use-a-custom-build-script-to-install-a-third-party-dependency-or-tool.md).
2. Add the necessary commands to the script to install Carthage using Homebrew and build your Carthage dependencies.

## See Also

- [Configuring Xcode Cloud for your team](configuring-xcode-cloud-for-your-team.md)
  Start using continuous integration and delivery with Xcode Cloud as a team.
- [Sharing macOS and Xcode versions across Xcode Cloud workflows](sharing-custom-aliases-across-xcode-cloud-workflows.md)
  Use custom aliases to share configurations with multiple workflows.
- [Sharing environment variables across Xcode Cloud workflows](sharing-environment-variables-across-xcode-cloud-workflows.md)
  Apply common configurations to multiple workflows by using shared environment variables.
- [Building Swift packages and Swift Playgrounds app projects with Xcode Cloud](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md)
  Add your Swift package or Swift Playgrounds app project to an Xcode project to build it in Xcode Cloud.
- [Setting the next build number for Xcode Cloud builds](setting-the-next-build-number-for-xcode-cloud-builds.md)
  Start numbering builds from a custom build number for your existing Mac app to avoid version collisions.
- [Including notes for testers with a beta release of your app](including-notes-for-testers-with-a-beta-release-of-your-app.md)
  Add text files to your Xcode project to provide notes to beta testers about what to test.
- [Removing your project from Xcode Cloud](removing-your-project-from-xcode-cloud.md)
  Remove your project from Xcode Cloud to delete app and workflow data, disconnect your Git repository, and remove the Slack integration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/making-dependencies-available-to-xcode-cloud)*