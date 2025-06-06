# Publishing a Swift package with Xcode

**Framework**: Xcode

Publish your Swift package privately, or share it globally with other developers.

#### Overview

Making your Swift packages available online enables you to use the support for Swift package dependencies in Xcode. By publishing your Swift packages to private Git repositories, you can manage and integrate internal dependencies across your projects, allowing you to reduce duplicate code and promote maintainability. Publish your packages publicly, and share your code with developers around the world. To get started, you just need a Swift package and an account with a provider of hosted Git repositories.

##### Provide Information on Your Swift Package

Every newly created Swift package contains a blank `README.md` file for you to modify. Consider adding information to it so other developers can learn more your Swift package, for example:

- A description of the functionality of your Swift package
- Licensing information
- Supported platforms and versions of Swift
- Contact information

Some developers even choose to include tutorials or usage documentation as part of their `README.md` file.

##### Put Your Local Swift Package Under Version Control

When you create a new Swift package with Xcode, check “Create Git repository on my Mac” in the sheet for creating a new package.

If you already have a local package that’s not using version control, put it under version control using Xcode. Open your Swift package, select the Source Control menu, choose New Git Repositories, check the checkbox next to your package, and click Create. This initializes a Git repository, adds your package to the staging area, and commits your files.

![Screenshot showing the dialogue when following the directions to put a standalone Swift package under version control.](https://docs-assets.developer.apple.com/published/25cc750fddc0390c43fdc6672b5edd58/publishing-a-swift-package-with-xcode-1%402x.png)

##### Tag Your Latest Commit

It’s a best practice to create a version tag for a Swift package; however, there are other ways to add a package to a project, as described in [`Adding package dependencies to your app`](adding-package-dependencies-to-your-app.md). To create a version tag, tag the last commit with the package version. A  is a three period-separated integer. An example is `1.0.0.` The package version must conform to  to ensure that your package behaves in a predictable manner when developers update their package dependency to a newer version.

To learn more about the semantic versioning standard, visit [`Semantic Versioning 2.0.0`](https://developer.apple.comhttps://semver.org).

> **Note**: Make sure to commit any changes that you want to include in the release of your Swift package before creating a version tag.

Make sure to commit any changes that you want to include in the release of your Swift package before creating a version tag.

In the Source Code Navigator, click the disclosure triangle next to Branches to show a list of your branches, then select a branch. In the history editor, Control-click a commit, then choose Tag “Your Identifier” from the pop-up menu. In the sheet that appears, enter a tag name that follows the semantic versioning standard, such as `1.2.4`. Add an optional message, then click Create.

##### Make Your Swift Package Publicly Available

Ensure the Source Control Navigator is visible and select your local repository. Right-click it, and choose Create  Remote. In case you’ve already created an empty remote repository for your Swift package, choose Add Existing Remote.

> ❗ **Important**: You need to add a hosted Git account in Xcode’s Settings to be able to create or connect a Git remote.

You need to add a hosted Git account in Xcode’s Settings to be able to create or connect a Git remote.

Next, push your local changes and the version tag to your Git remote. Click the Source Control menu, select Push, choose the branch from the dropdown menu, check the checkbox next to Include Tags, and click Push.

Ensure your Git repository is public, and let people know that the package exists. Other developers only need the package’s Git URL to get started.

Learn more about adopting package dependencies in [`Adding package dependencies to your app`](adding-package-dependencies-to-your-app.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/publishing-a-swift-package-with-xcode)*