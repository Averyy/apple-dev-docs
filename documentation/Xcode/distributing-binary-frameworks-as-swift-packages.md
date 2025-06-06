# Distributing binary frameworks as Swift packages

**Framework**: Xcode

Make binaries available to other developers by creating Swift packages that include one or more XCFrameworks.

#### Overview

Creating a Swift package to organize and share your code makes source files available to developers who use the Swift package as a package dependency. However, you may need to make your code available as binaries to protect your intellectual property — for example, if you’re developing proprietary, closed-source libraries.

Carefully consider whether you want to distribute your code in binary form because doing so comes with drawbacks. For example, a Swift package that contains a binary is less portable because it can only support platforms that its included binaries support. In addition, binary dependencies are only available for Apple platforms, which limits the audience for your Swift package.

> **Note**: A Swift package can contain a mix of both source files and binaries. This use case is common for packages that contain source code that wraps closed-source binaries.

A Swift package can contain a mix of both source files and binaries. This use case is common for packages that contain source code that wraps closed-source binaries.

##### Package Binaries As an Xcframework Bundle

To distribute code in binary form as a Swift package, create an XCFramework bundle, or , that contains the binaries. Then, make the bundle available locally or on a server:

- When you host the binaries on a server, create a ZIP archive with the XCFramework in its root directory and make it available publicly.
- If the XCFramework is available locally and included in the package’s Git repository, you don’t need to create a compressed archive and can reference the XCFramework directly.

To learn more about creating an XCFramework bundle, see [`Creating a multiplatform binary framework bundle`](creating-a-multi-platform-binary-framework-bundle.md).

##### Declare a Binary Target in the Package Manifest

First, follow the process to create a new Swift package as described in [`Creating a standalone Swift package with Xcode`](creating-a-standalone-swift-package-with-xcode.md). Next, declare a  in your package manifest and make it part of a product, just like a target that contains source files. Ensure that the name of the binary target in the package manifest matches the artifact’s module name.

To declare a remote, or , binary target, use [`binaryTarget(name:path:)`](https://developer.apple.com/documentation/PackageDescription/Target/binaryTarget(name:path:)). To create the required [`checksum`](https://developer.apple.com/documentation/PackageDescription/Target/checksum), open the Terminal app, navigate to the root of the package, and run `swift package compute-checksum path/to/MyFramework.zip`. Xcode uses the checksum to verify that the hosted archive file matches the archive you declare in the manifest file. When developers add the package as a binary dependency to their project, and the remote archive’s checksum doesn’t match the checksum in the package manifest, Xcode displays an error.

To declare a local, or , binary target, use [`package(name:path:)`](https://developer.apple.com/documentation/PackageDescription/Package/Dependency/package(name:path:)) and don’t generate a checksum. Instead, include the `.xcframework` bundle in the package’s Git repository.

The following package manifest for the MyLibrary package declares a library product that includes two binary targets: `SomeRemoteBinaryPackage`, a remote, URL-based binary target; and `SomeLocalBinaryPackage`, a local, path-based binary target.

```swift
// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "MyLibrary",
    platforms: [
        .macOS(.v10_14), .iOS(.v13), .tvOS(.v13)
    ],
    products: [
        // Products define the executables and libraries a package produces, and make them visible to other packages.
        .library(
            name: "MyLibrary",
            targets: ["MyLibrary", "SomeRemoteBinaryPackage", "SomeLocalBinaryPackage"])
    ],
    dependencies: [
        // Dependencies declare other packages that this package depends on.
    ],
    targets: [
        // Targets are the basic building blocks of a package. A target can define a module or a test suite.
        // Targets can depend on other targets in this package, and on products in packages this package depends on.
        .target(
            name: "MyLibrary"
        ),
        .binaryTarget(
            name: "SomeRemoteBinaryPackage",
            url: "https://url/to/some/remote/xcframework.zip",
            checksum: "The checksum of the ZIP archive that contains the XCFramework."
        ),
        .package(
            name: "SomeLocalBinaryPackage",
            path: "path/to/some.xcframework"
        )
        .testTarget(
            name: "MyLibraryTests",
            dependencies: ["MyLibrary"]),
    ]
)
```

## See Also

- [Creating a standalone Swift package with Xcode](creating-a-standalone-swift-package-with-xcode.md)
  Bundle executable or shareable code into a standalone Swift package.
- [Bundling resources with a Swift package](bundling-resources-with-a-swift-package.md)
  Add resource files to your Swift package and access them in your code.
- [Localizing package resources](localizing-package-resources.md)
  Ensure that your Swift package provides localized resources for many locales.
- [Developing a Swift package in tandem with an app](developing-a-swift-package-in-tandem-with-an-app.md)
  Add your published Swift package as a local package to your app’s project and develop the package and the app in tandem.
- [Organizing your code with local packages](organizing-your-code-with-local-packages.md)
  Simplify maintenance, promote modularity, and encourage reuse by organizing your app’s code into local Swift packages.
- [PackageDescription](../PackageDescription/PackageDescription.md)
  Create reusable code, organize it in a lightweight way, and share it across your projects and with other developers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/distributing-binary-frameworks-as-swift-packages)*