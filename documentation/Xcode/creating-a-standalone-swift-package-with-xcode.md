# Creating a standalone Swift package with Xcode

**Framework**: Xcode

Bundle executable or shareable code into a standalone Swift package.

#### Overview

Swift packages are reusable components of Swift, Objective-C, Objective-C++, C, or C++ code. They can bundle resources, vend their code as binaries, or depend on other packages. Use Swift packages to bundle executable code, for example a script, as an , or create a package to vend shareable code as a . Packages that vend a library product help promote modularity in your code, make it easy to share code with others, and enable other developers to add functionality to their apps.

With Xcode, you can create a new Swift package, add code, resource files, and binaries, build the Swift package, and run its unit tests.

![Flowchart showing the development lifecycle for a Swift package.](https://docs-assets.developer.apple.com/published/ce439cc5d6ba4621ef3eb70fe9168526/creating-a-swift-package-with-xcode-1%402x.png)

##### Create a Swift Package

To create a new Swift package, open Xcode and select File > New > Package. Choose a name and select a file location. Select “Create Git repository on my Mac” to put your package under version control. On completion, the Swift package opens in Xcode and looks similar to a standard Xcode project. Xcode generates all necessary files and folders as it creates a Swift package:

- The `README.md` file resides at the root level of the package. It describes the functionality of your Swift package.
- The `Package.swift` file, or , describes the configuration for the Swift package. You can double-click it in Finder to open the package in Xcode. The package manifest uses Swift and the PackageDescription framework to define the package’s name, products, targets, dependencies on other packages, and so on.
- Source files reside in a folder named `Sources` and are scoped per [`Target`](https://developer.apple.com/documentation/PackageDescription/Target). A Swift package can contain several targets, and, as a convention, each target’s code resides in its own subfolder.
- Unit test targets reside in a folder named `Tests`, and, following the same convention as standard targets, each test target’s code resides in its own subfolder.

![Screenshot showing a newly created standalone Swift package named ExamplePackage. The Editor area shows the package’s manifest file while the Navigator area shows the package’s contents and the Utilities area displays the information about the package manifest.](https://docs-assets.developer.apple.com/published/4e21715f0e1aca7e69152ba05ec2a3d3/creating-a-swift-package-with-xcode-2%402x.png)

##### Configure Your Swift Package

Swift packages don’t use `.xcodeproj` or `.xcworkspace` but rely on their folder structure and use the package manifest for additional configuration. The following code listing shows a simple package manifest. It declares the MyLibrary target, and vends it as a library product with the same name.

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
            name: "MyLibrary",
            exclude: ["instructions.md"],
            resources: [
                .process("text.txt"),
                .process("example.png"),
                .copy("settings.plist")
            ]
        ),
        .binaryTarget(
            name: "SomeRemoteBinaryPackage",
            url: "https://url/to/some/remote/binary/package.zip",
            checksum: "The checksum of the XCFramework inside the ZIP archive."
        ),
        .binaryTarget(
            name: "SomeLocalBinaryPackage",
            path: "path/to/some.xcframework"
        )
        .testTarget(
            name: "MyLibraryTests",
            dependencies: ["MyLibrary"]),
    ]
)
```

The package manifest must begin with the string `// swift-tools-version:`, followed by a version number such as `// swift-tools-version:5.3`.

The Swift tools version declares:

- The version of the PackageDescription framework
- The Swift language compatibility version to process the manifest
- The required minimum version of the Swift tools to use the package

Each version of Swift can introduce updates to the PackageDescription framework, but the previous API version is available to packages that declare a prior Swift tools version. This behavior allows you take advantage of new releases of Swift, the Swift tools, and the PackageDescription framework, without having to update your package manifest and without losing access to existing packages.

To learn more about the `PackageDescription` framework, see [`Package`](https://developer.apple.com/documentation/PackageDescription/Package).

> **Note**: Xcode provides code completion when you edit the package manifest.

Xcode provides code completion when you edit the package manifest.

##### Add Your Code

Per convention, source files reside in a subfolder of the package’s `Sources` directory that has the same name as the target they belong to. Note how the package manifest above declares the `MyLibrary` target. Its source files reside in `Sources/MyLibrary` while source files for tests reside in `Tests/MyLibraryTests`. You can use additional subfolders to structure them. Per default, Xcode includes all valid source files inside a target’s folder. If you prefer to declare included source files explicitly, pass them using the [`sources`](https://developer.apple.com/documentation/PackageDescription/Target/sources) parameter when you initialize the [`Target`](https://developer.apple.com/documentation/PackageDescription/Target). You can also pass paths to directories.

![Screenshot showing a standalone Swift package with two added source files and two unit test files.](https://docs-assets.developer.apple.com/published/84b9475b2001d600f4672ff32d716930/creating-a-swift-package-with-xcode-3%402x.png)

To add source files to a Swift package, use workflows that you already know. For example, you can add a source file to a package by dragging it into the Project navigator, or by using the File > Add Files to  menu. Targets can contain Swift, Objective-C/C++, or C/C++ code, but an individual target can’t mix Swift with C-family languages. For example, a Swift package can have two targets, one that contains Objective-C, Objective-C++, and C code, and a second one that contains Swift code.

##### Add a Dependency on Another Swift Package

Just like apps, Swift packages can have . To declare a dependency on a remote package, use one of the functions that take the URL of the remote package as a parameter. To add a local package as a dependency, use one of the functions that take a path to the local package as a parameter. The following code snipped shows both options:

```swift
dependencies: [    
    // Dependencies declare other packages that this package depends on.
    .package(url: "https://url/of/another/package.git", from: "1.0.0"),
    .package(path: "path/to/a/local/package/", "1.0.0"..<"2.0.0")],
```

See [`Package.Dependency`](https://developer.apple.com/documentation/PackageDescription/Package/Dependency) for all possible ways to declare a package dependency. When you add the dependency, you can use its vended product as a [`Target.Dependency`](https://developer.apple.com/documentation/PackageDescription/Target/Dependency) or make it a part of your package’s [`Product`](https://developer.apple.com/documentation/PackageDescription/Product).

##### Distribute Binaries As a Swift Package

Instead of distributing a Swift package that vends source files, you can choose to distribute binaries instead. For example, creators of proprietary closed-source libraries often make them available as binaries. See [`Distributing binary frameworks as Swift packages`](distributing-binary-frameworks-as-swift-packages.md) to learn more.

##### Add Package Resources

Declare a Swift tools version of 5.3 or later in your manifest file to add asset files as package resources to your Swift package. For example, Swift packages can contain user interface components that use asset catalogs, storyboards, `.strings` files, and so on. See [`Bundling resources with a Swift package`](bundling-resources-with-a-swift-package.md) to learn more.

##### Make Your Swift Package Cross Platform Compatible

While Swift packages are platform-independent by nature and include, for example, Linux as a target platform, Swift packages can be platform-specific. Use conditional compilation blocks to handle platform-specific code and achieve cross-platform compatibility. The following example shows how to use conditional compilation blocks:

```swift
#if os(Linux)

// Code specific to Linux

#elseif os(macOS)

// Code specific to macOS

#endif

#if canImport(UIKit)

// Code specific to platforms where UIKit is available

#endif
```

In addition, you may need to define a minimum deployment target. Note how the package manifest below declares minimum deployment targets by passing them in as a value to the `platforms` parameter of the [`Package`](https://developer.apple.com/documentation/PackageDescription/Package) initializer. However, passing minimum deployment targets to the initializer doesn’t restrict the package to the listed platforms.

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
            name: "MyLibrary",
            exclude: ["instructions.md"],
            resources: [
                .process("text.txt"),
                .process("example.png"),
                .copy("settings.plist")
            ]
        ),
        .binaryTarget(
            name: "SomeRemoteBinaryPackage",
            url: "https://url/to/some/remote/binary/package.zip",
            checksum: "The checksum of the XCFramework inside the ZIP archive."
        ),
        .binaryTarget(
            name: "SomeLocalBinaryPackage",
            path: "path/to/some.xcframework"
        )
        .testTarget(
            name: "MyLibraryTests",
            dependencies: ["MyLibrary"]),
    ]
)
```

> 💡 **Tip**: If you plan to publish a Swift package that doesn’t support all platforms, consider mentioning the supported platforms in your `README.md` file. In addition, think about adding support for other platforms to grow its audience.

If you plan to publish a Swift package that doesn’t support all platforms, consider mentioning the supported platforms in your `README.md` file. In addition, think about adding support for other platforms to grow its audience.

##### Build Your Targets and Run Unit Tests

Xcode creates a scheme for each product in the package manifest. Select a scheme for the package’s build-and-run destination, and build it as you’d build an app target. Each source target usually has at least one corresponding test target. If your package contains multiple products, Xcode creates an additional scheme with the name -Package to build all targets and run all unit tests.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-a-standalone-swift-package-with-xcode)*