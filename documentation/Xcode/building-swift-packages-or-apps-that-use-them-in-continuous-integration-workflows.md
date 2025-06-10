# Building Swift packages or apps that use them in continuous integration workflows

**Framework**: Xcode

Build Swift packages with an existing continuous integration setup and prepare apps that consume package dependencies within an existing CI pipeline.

#### Overview

 (CI) is the process of automating and streamlining the building, analyzing, testing, archiving, and publishing of your apps to ensure that they’re always in a releasable state. Use either [`Xcode Cloud`](xcode-cloud.md) or the `xcodebuild` command directly on other CI systems to build Swift packages and apps that use them.

Most projects that contain or depend on Swift packages don’t require additional configuration. However, be sure to commit your project’s `Package.resolved` file to your Git repository. This ensures a reliable CI workflow that always uses the expected version of a package dependency. If your project depends on packages that require authentication, or you need to use your Mac’s Git tooling instead of the tooling which comes bundled with Xcode, you may need to perform additional configuration.

> ❗ **Important**: While you can build a standalone Swift package locally with Xcode, Xcode Cloud requires the package to be part of a project or workspace. To learn about building Swift packages with Xcode Cloud, see [`Building Swift packages and Swift Playgrounds app projects with Xcode Cloud`](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md).

##### Use the Expected Version of a Package Dependency

To ensure the CI workflow’s reliability, make sure it uses the appropriate version of package dependencies. Xcode stores the exact version of each package dependency in a file called `Package.resolved`. The file automatically updates when package requirements in your Xcode project or in the `Package.swift` manifest file change. Commit this file to your Git repository to ensure it’s always up-to-date on the CI environment to prevent the CI from building your project with unexpected versions of package dependencies.

> 💡 **Tip**: You can find the `Package.resolved` file inside your `.xcodeproj` directory at `.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved`.

If your CI pipeline uses the `xcodebuild` command directly, also pass the `-disableAutomaticPackageResolution` flag. This flag ensures that the CI pipeline always uses the package dependencies as defined in the `Package.resolved` file.

##### Provide Credentials

If your Xcode project only depends on publicly available Swift packages, you don’t need to perform additional configuration steps. Xcode Cloud or the `xcodebuild` command automatically resolve package dependencies for you. However, to resolve package dependencies that require authentication, or , you need to provide credentials to your CI setup. For information on granting Xcode Cloud access to private dependencies, see [`Making dependencies available to Xcode Cloud`](making-dependencies-available-to-xcode-cloud.md).

If you’re using the `xcodebuild` command directly, use SSH–based Git URLs for your packages and configure your SSH credentials. Set up your `known_hosts` file in the `~/.ssh` directory of the macOS user that runs your CI tasks. `xcodebuild` honors your SSH configuration — there’s no additional setup required.

If your SSH keys are password-protected, add them to the SSH agent before invoking `xcodebuild` by modifying the SSH configuration file as described in [`Tech Note 2449`](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2449/_index.html).

##### Use Your Systems Git Tooling

When you use the `xcodebuild` directly, it uses Xcode’s built-in Git tooling to connect to repositories. In many cases, you don’t need to make changes to how `xcodebuild` connects to them. However, some use cases require you use the configuration you set for your Mac’s Git installation. For example:

- URL remapping
- Proxy configurations
- Advanced SSH configurations, for example, disabling the `StrictHostKeyChecking` setting

To have `xcodebuild` use your Mac’s Git installation and configuration, pass `-scmProvider system` to the `xcodebuild` command.

For more information on using `xcodebuild`, see [`Technical Note 2339`](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2339/_index.html).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows)*