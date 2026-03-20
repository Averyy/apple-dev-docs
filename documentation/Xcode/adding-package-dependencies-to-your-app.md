# Adding package dependencies to your app

**Framework**: Xcode

Integrate package dependencies to share code between projects, or leverage code from other developers.

#### Overview

Xcode comes with built-in support for source control accounts and makes it easy to leverage available Swift packages. Use Xcode to manage the versions of package dependencies and make sure your project has the most up-to-date code changes.

> **Note**: A package author can publish their Swift package to either public or private repositories. Xcode supports both private and publicly available packages.

##### Add a Package Dependency

To add a package dependency to your Xcode project, select File > Add Package Dependency and enter its source control repository URL. You can also navigate to your target’s General pane, and in the “Frameworks, Libraries, and Embedded Content” section, click the + button, select Add Other, and choose Add Package Dependency.

![Screenshot showing the dialogue for adding content to the “Frameworks, Libraries, and Embedded Content” with Add Package Dependency… selected.](https://docs-assets.developer.apple.com/published/9e53f203a6a4c3e6fcc05ab6a52ad4bc/adding-package-dependencies-to-your-app-1%402x.png)

Instead of adding a source control repository URL, you can search for a package on [`GitHub`](https://developer.apple.comhttps://github.com) or [`GitHub Enterprise`](https://developer.apple.comhttps://github.com/enterprise). Add your GitHub or GitHub Enterprise account in Xcode’s settings, and a list of package repositories appears as you type. The following screenshot shows a list of repositories for the search term `ExamplePackage` for a user who added their Git provider in Xcode’s settings.

![Screenshot showing the dialogue to add a package dependency. The user has entered ExamplePackage in the search field.](https://docs-assets.developer.apple.com/published/5912b3a4fb5c25545fe107028c8be837/adding-package-dependencies-to-your-app-2%402x.png)

If you’ve added a source control account in Xcode’s settings and you haven’t yet entered a search term, the list contains package repositories from:

- Your Git Repositories
- Your team’s Git repositories
- Your starred repositories on [`GitHub`](https://developer.apple.comhttps://github.com), [`GitHub Enterprise`](https://developer.apple.comhttps://github.com/enterprise), [`GitLab`](https://developer.apple.comhttps://gitlab.com), or your [`self-managed GitLab`](https://developer.apple.comhttps://about.gitlab.com/free-trial/self-managed/) instance

> ❗ **Important**: Only add package dependencies by trustworthy authors. In addition, adding a binary dependency comes with drawbacks over adding a source-based dependency. See [`Identifying binary dependencies`](identifying-binary-dependencies.md) to learn more.

##### Decide on Package Requirements

When you enter the package dependency’s URL or pick a Swift package from the list of packages, choose one of three *package requirements*. Package requirements determine the allowed versions of the package dependency in your project, and Xcode updates your package dependency based on the requirement that you choose.

- **Version**: Decide whether your project accepts updates to a package dependency up to the next major version or up to the next minor version. To be more restrictive, select a specific version range or an exact version. Major versions tend to have more significant changes than minor versions, and may require you to modify your code when they update. The version rule requires Swift packages to conform to semantic versioning. To learn more about the semantic versioning standard, visit [`Semantic Versioning 2.0.0`](https://developer.apple.comhttps://semver.org). Selecting the version requirement is the recommended way to add a package dependency. It allows you to create a balance between restricting changes and obtaining improvements and features.
- **Branch**: Select the name of the branch for your package dependency to follow. Use branch-based dependencies when you’re developing multiple packages in tandem and don’t want to publish versions of your package dependencies.
- **Commit**: Select the commit hash for your package dependency to follow. Choosing this option isn’t recommended, and you should only use this option in exceptional cases. While pinning your package dependency to a specific commit ensures that the package dependency doesn’t change and your code remains stable, you don’t receive any updates. If you worry about the stability of a remote package, consider one of the more restrictive options of the version-based requirement.

After you choose a package requirement, Xcode resolves and fetches the package dependency. Select the package’s products that you need, and add them to targets in your project.

In Xcode’s Project navigator, the Swift Package Dependencies section shows the newly added package dependency. Click the disclosure triangle to view the contents of the package as it exists locally on your Mac.

> 💡 **Tip**: Although Xcode updates your package dependencies and resolves package versions automatically, you can trigger both actions from the File > Packages menu.

##### Use Features and Assets Provided By a Swift Package

To use a Swift package’s functionality in your app, import a package’s product as a Swift module. The following code snippet shows a view controller that imports a Swift package’s `MyLibrary` module and uses the package’s functionality:

```swift
import UIKit

// Import the module that corresponds with the Swift package’s library product MyLibrary.
import MyLibrary

class ViewController: UIViewController {

    @IBOutlet var aLabel: UILabel!
    @IBOutlet var aButton: UIButton!
    @IBOutlet var anImageView: UIImageView!
    @IBOutlet var aCustomView: CustomView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // Use a string that the package exposes as a property in the MyLibrary file.
        self.aLabel.text = MyLibrary.titleText

        // Load an image that the MyLibrary package makes available through a class method.
        if let imagePath = MyClass.exampleImagePath() {
            self.anImageView.image = UIImage(contentsOfFile: imagePath)
        }

        // Use the Swift package’s CustomView class.
        self.aCustomView = CustomView()
    }

    // Show an alert by calling the package’s API.
    @IBAction func showAlert(_ sender: Any) {
        MyClass.showAlertUsing(viewController: self)
    }
}
```

##### Edit a Package Dependency

You can’t edit the content of your package dependencies directly. If you want to make changes to a package dependency, you need to add it as a *local package* to your project. See [`Editing a package dependency as a local package`](editing-a-package-dependency-as-a-local-package.md) to learn how you can override a package dependency with a local package and make edits.

##### Coordinate Package Versions Across Your Team

When collaborating on a project, make sure everyone uses the same version of a package dependency. When you add a package dependency to a project, Xcode creates the `Package.resolved` file. It lists the specific Git commits to which each package dependency resolves and the [`checksum`](https://developer.apple.com/documentation/PackageDescription/Target/checksum) of each binary dependency. Commit this file in Git to ensure that everyone is using the same version of a package dependency.

> 💡 **Tip**: You can find the `Package.resolved` file inside your .`xcodeproj` directory at *[appName]*`.xcodeproj/project.workspace/xcshareddata/swiftpm/Package.resolved`.

##### Delete a Package Dependency

To remove a package dependency from your Xcode project:

1. Select your project in the Project Editor and navigate to the Packages Dependencies pane.
2. Select the package from the list of package dependencies.
3. Click the - button from the bottom of the list and click Remove to confirm.

![Screenshot showing the confirmation dialogue that appears when removing a package dependency.](https://docs-assets.developer.apple.com/published/02b97a57423502e8cfac9b1a5dcf6193/adding-package-dependencies-to-your-app-3%402x.png)

## See Also

- [Managing your app’s information property list values](../BundleResources/managing-your-app-s-information-property-list.md)
  Customize the information property list values for your app using Xcode.
- [Creating a Mac version of your iPad app](../UIKit/creating-a-mac-version-of-your-ipad-app.md)
  Bring your iPad app to macOS with Mac Catalyst.
- [Setting up a watchOS project](../watchOS-Apps/setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [Embedding a command-line tool in a sandboxed app](embedding-a-helper-tool-in-a-sandboxed-app.md)
  Add a command-line tool to a sandboxed app’s Xcode project so the resulting app can run it as a helper tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app)*