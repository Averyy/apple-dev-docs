# Building Swift packages and Swift Playgrounds app projects with Xcode Cloud

**Framework**: Xcode

Add your Swift package or Swift Playgrounds app project to an Xcode project to build it in Xcode Cloud.

#### Overview

Xcode Cloud comes with support for the Swift Package Manager, and using Swift package dependencies in your app project requires little to no configuration. However, Xcode Cloud can’t build standalone Swift packages. To build your Swift package with Xcode Cloud:

1. Create an app project or workspace in Xcode.
2. Add your Swift package as a local package as described in [`Organizing your code with local packages`](organizing-your-code-with-local-packages.md).
3. Commit your `Package.resolved` file.
4. Create your first workflow as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md).

When Xcode Cloud starts a build, it builds your Swift package as part of the app project.

Similarly, Xcode Cloud can’t build standalone apps you create with [`Swift Playgrounds`](https://developer.apple.comhttps://www.apple.com/swift/playgrounds/). To build an app you created with Swift Playgrounds, save the Swift Playground app project to your Mac, add it to an Xcode project as described above, then configure your first workflow for the Xcode project.

> **Note**: To learn more about building projects with Xcode Cloud that require Swift package dependencies, see [`Use Swift package dependencies and Git submodules`](making-dependencies-available-to-xcode-cloud#Use-Swift-package-dependencies-and-Git-submodules.md).

## See Also

- [Making dependencies available to Xcode Cloud](making-dependencies-available-to-xcode-cloud.md)
  Review dependencies and make them available to Xcode Cloud before you configure your project to use Xcode Cloud.
- [Configuring Xcode Cloud for your team](configuring-xcode-cloud-for-your-team.md)
  Start using continuous integration and delivery with Xcode Cloud as a team.
- [Sharing macOS and Xcode versions across Xcode Cloud workflows](sharing-custom-aliases-across-xcode-cloud-workflows.md)
  Use custom aliases to share configurations with multiple workflows.
- [Sharing environment variables across Xcode Cloud workflows](sharing-environment-variables-across-xcode-cloud-workflows.md)
  Apply common configurations to multiple workflows by using shared environment variables.
- [Setting the next build number for Xcode Cloud builds](setting-the-next-build-number-for-xcode-cloud-builds.md)
  Start numbering builds from a custom build number for your existing Mac app to avoid version collisions.
- [Including notes for testers with a beta release of your app](including-notes-for-testers-with-a-beta-release-of-your-app.md)
  Add text files to your Xcode project to provide notes to beta testers about what to test.
- [Removing your project from Xcode Cloud](removing-your-project-from-xcode-cloud.md)
  Remove your project from Xcode Cloud to delete app and workflow data, disconnect your Git repository, and remove the Slack integration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud)*