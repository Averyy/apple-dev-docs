# Swift packages

**Framework**: Xcode

Create reusable code, organize it in a lightweight way, and share it across Xcode projects and with other developers.

#### Overview

![An image illustrating how Xcode supports bundling code, resources, and binaries into a Swift package.](https://docs-assets.developer.apple.com/published/e8b388997f04b268375040a5b9e59ef5/swift-packages%402x.png)

Swift packages are reusable components of Swift, Objective-C, Objective-C++, C, or C++ code that developers can use in their projects. They bundle source files, binaries, and resources in a way that’s easy to use in your app’s project.

Xcode supports creating and publishing Swift packages, as well as adding, removing, and managing package dependencies. Its support for Swift packages is built on top of the open source Swift Package Manager project.

To learn more about the API you use in your package manifest, see [`Package`](https://developer.apple.com/documentation/PackageDescription/Package). To learn more about the Swift Package Manager, see [`Swift.org`](https://developer.apple.comhttps://swift.org/package-manager/) and the open source [`Swift Package Manager repository`](https://developer.apple.comhttps://github.com/apple/swift-package-manager).

## Topics

### Package dependencies
- [Adding package dependencies to your app](adding-package-dependencies-to-your-app.md)
  Integrate package dependencies to share code between projects, or leverage code from other developers.
- [Identifying binary dependencies](identifying-binary-dependencies.md)
  Find out if a package dependency references a binary and verify the binary’s authenticity.
- [Editing a package dependency as a local package](editing-a-package-dependency-as-a-local-package.md)
  Override a package dependency and edit its content by adding it as a local package.
### Package creation
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
- [Organizing your code with local packages](organizing-your-code-with-local-packages.md)
  Simplify maintenance, promote modularity, and encourage reuse by organizing your app’s code into local Swift packages.
- [PackageDescription](../PackageDescription/PackageDescription.md)
  Create reusable code, organize it in a lightweight way, and share it across your projects and with other developers.
### Package distribution
- [Publishing a Swift package with Xcode](publishing-a-swift-package-with-xcode.md)
  Publish your Swift package privately, or share it globally with other developers.
### Continuous integration
- [Building Swift packages or apps that use them in continuous integration workflows](building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows.md)
  Build Swift packages with an existing continuous integration setup and prepare apps that consume package dependencies within an existing CI pipeline.

## See Also

- [Source editor](source-editor.md)
  Edit your source files, locate issues, and make necessary changes using the source editor.
- [Bundles and frameworks](bundles-and-frameworks.md)
  Organize code and resources in bundles and frameworks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/swift-packages)*