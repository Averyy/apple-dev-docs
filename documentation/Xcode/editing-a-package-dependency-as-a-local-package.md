# Editing a package dependency as a local package

**Framework**: Xcode

Override a package dependency and edit its content by adding it as a local package.

#### Overview

When you’re using a Swift package as a package dependency in your app, you may want to make edits to it. For example, you may want to contribute a fix for a bug to an open-source package. However, you can’t directly edit the content of a package dependency. To make changes, add the Swift package as a local package to your app’s project. Don’t remove your package dependency; adding a local package overrides the package dependency with the same name. Xcode uses the package dependency again when you remove the local package from your project.

To add the Swift package as local package to your project:

1. Check out your package dependency’s source code from its Git repository.
2. Open your app’s Xcode project or workspace.
3. Choose File > Add Package Dependencies.
4. Click the Add Local button at the bottom of the package selection window.
5. Select the folder that contains your package and click the Add Package button.
6. Choose targets for the Package Products Xcode detects.

Now you can make changes to the local package and verify them by building and running your app. When you’re done editing the local package, push your changes to its remote Git repository. When the changes have made it into the package’s next release, remove the local package from your project, and update the package dependency to the new version.

## See Also

- [Adding package dependencies to your app](adding-package-dependencies-to-your-app.md)
  Integrate package dependencies to share code between projects, or leverage code from other developers.
- [Identifying binary dependencies](identifying-binary-dependencies.md)
  Find out if a package dependency references a binary and verify the binary’s authenticity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/editing-a-package-dependency-as-a-local-package)*