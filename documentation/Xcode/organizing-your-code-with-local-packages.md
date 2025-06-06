# Organizing your code with local packages

**Framework**: Xcode

Simplify maintenance, promote modularity, and encourage reuse by organizing your app’s code into local Swift packages.

#### Overview

As you develop your app, organize its code in a modular way to keep it maintainable by creating Swift packages and using them as .

First, identify code that’s a good candidate for modularization; for example, networking logic, source files that contain utilities, and so on. Next, move the code into a local package like this:

1. Open your Xcode project and create a local Swift package as part of your project by selecting File > New > Package (or Swift Package in versions earlier than Xcode 15)
2. To create a package pre-configured for a library, select Multiplatform from the top of the package templates dialog, choose the Library template, and click Next. Choose from the other templates in the dialog to create packages configured for other kinds of content.
3. Choose a project and a group, but don’t create a new Git repository if your app is already under version control; then create the new Swift package.
4. Move your code to the new package in the Project navigator and make any needed updates to the . The amount of configuration depends on your requirements. For example, you might need to vend your code as a library product and declare the package’s targets. To learn more about configuring a Swift package, see [`Creating a standalone Swift package with Xcode`](creating-a-standalone-swift-package-with-xcode.md).
5. Select your project in the Project navigator, then select your app target and navigate to its General pane.
6. Click the + button in the “Frameworks, Libraries, and Embedded Content” section, select the local package’s library product, and add it as a dependency.

When you organize your app’s codebase using local packages, your Swift package’s code is part of the same repository as your app’s code. As you create more apps, consider moving local packages to their own Git repositories, and add them to your apps as a package dependency to reuse code across apps. You may even consider sharing them with other developers. For more information, see [`Publishing a Swift package with Xcode`](publishing-a-swift-package-with-xcode.md).

## See Also

- [Creating a standalone Swift package with Xcode](creating-a-standalone-swift-package-with-xcode.md)
  Bundle executable or shareable code into a standalone Swift package.
- [Bundling resources with a Swift package](bundling-resources-with-a-swift-package.md)
  Add resource files to your Swift package and access them in your code.
- [Localizing package resources](localizing-package-resources.md)
  Ensure that your Swift package provides localized resources for many locales.
- [Distributing binary frameworks as Swift packages](distributing-binary-frameworks-as-swift-packages.md)
  Make binaries available to other developers by creating Swift packages that include one or more XCFrameworks.
- [Developing a Swift package in tandem with an app](developing-a-swift-package-in-tandem-with-an-app.md)
  Add your published Swift package as a local package to your app’s project and develop the package and the app in tandem.
- [PackageDescription](../PackageDescription/PackageDescription.md)
  Create reusable code, organize it in a lightweight way, and share it across your projects and with other developers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages)*